from odoo import api, fields, models
from odoo.exceptions import *

class PenjualanReseller(models.Model):
    _name = 'rezzstore.penjualanreseller'
    _description = 'New Description'

    _rec_name = 'trx_seq'

    trx_seq = fields.Char(
        string='No. Transaksi',
        readonly=True,
        required=True,
        copy=False,
        default='New'
    )
    daftarreseller_id = fields.Many2one(
        'rezzstore.reseller', 
        string='Nama Reseller'
    )
    name = fields.Char(string='Name Konsumen')
    no_wa = fields.Char(string='No. WhatsApp Konsumen')
    email = fields.Char(string='E-Mail Konsumen')
    tgl_trx = fields.Datetime(
        string='Tanggal Transaksi',
        required=True,
        default=fields.Datetime.now()
    )
    total_bayar = fields.Integer(
        compute='_compute_totalbayar',
        string='Total Pembayaran'
    )
    detailpenjualan_ids = fields.One2many(
        comodel_name='rezzstore.detailreseller',
        inverse_name='penjualan_id',
        string='Detail Penjualan'
    )
    state = fields.Selection(
        string='Status', 
        selection=[
            ('draft', 'Draft'),
            ('confirm', 'Confirm'),
            ('done', 'Done'),
            ('cancel', 'Cancel'),
        ],
        required=True,
        readonly=True,
        default='draft')
    
    def action_confirm(self):
        self.write({'state': 'confirm'})
    
    def action_done(self):
        self.write({'state': 'done'})

    def action_cancel(self):
        self.write({'state': 'cancel'})

    def action_draft(self):
        self.write({'state': 'draft'})

    @api.model
    def create(self, vals):
        if vals.get('trx_seq', 'New') == 'New':
            vals['trx_seq'] = self.env['ir.sequence'].next_by_code('trx.res.sequence') or 'New'
        result = super(PenjualanReseller, self).create(vals)
        return result
    
    @api.depends('detailpenjualan_ids')
    def _compute_totalbayar(self):
        for rec in self:
            a = sum(self.env['rezzstore.detailreseller'].search([('penjualan_id','=',rec.id)]).mapped('subtotal'))
            rec.total_bayar = a
    
    def unlink(self):
        if self.filtered(lambda line: line.state != 'draft'):
            raise ValidationError("Tidak dapat menghapus jika status bukan Draft!")
        else:
            if self.detailpenjualan_ids:
                a=[]
                for rec in self:
                    a = self.env['rezzstore.detailreseller'].search([('penjualan_id','=',rec.id)])
                for ob in a:
                    ob.barang_id.stok += ob.qty
        record = super(PenjualanReseller,self).unlink()
    
    def write(self,vals):
        for rec in self:
            a = self.env['rezzstore.detailreseller'].search([('penjualan_id','=',rec.id)])
            for data in a:
                data.barang_id.stok += data.qty
        record = super(PenjualanReseller,self).write(vals)
        for rec in self:
            b = self.env['rezzstore.detailreseller'].search([('penjualan_id','=',rec.id)])
            for databaru in b:
                if databaru in a:
                    databaru.barang_id.stok -= databaru.qty
                else:
                    pass
        return record

class DetailReseller(models.Model):
    _name = 'rezzstore.detailreseller'
    _description = 'New Description'

    penjualan_id = fields.Many2one(
        comodel_name='rezzstore.penjualanreseller',
        string='Detail Penjualan'
    )
    barang_id = fields.Many2one(
        comodel_name='rezzstore.daftarjasa',
        string='List Jasa'
    )
    harga_satuan = fields.Integer(string='Harga Satuan')
    qty = fields.Integer(string='Quantity')
    subtotal = fields.Integer(
        compute='_compute_subtotal',
        string='Subtotal'
    )

    @api.depends('harga_satuan','qty')
    def _compute_subtotal(self):
        for rec in self:
            rec.subtotal = rec.qty * rec.harga_satuan

    @api.onchange('barang_id')
    def _onchange_barang_id(self):
        if (self.barang_id.harga_res):
            self.harga_satuan = self.barang_id.harga_res

    @api.model
    def create(self,vals):
        record = super(DetailReseller,self).create(vals)
        if record.qty:
            self.env['rezzstore.daftarjasa'].search([('id','=',record.barang_id.id)]).write({'stok' : record.barang_id.stok - record.qty})
        return record
    
    @api.constrains('qty')
    def check_qualitity(self):
       for rec in self:
            if (rec.barang_id.status != 'ready'):
                raise ValidationError("{} masih belum tersedia, status masih {}!".format(rec.barang_id.name,rec.barang_id.status))
            elif rec.qty < 1:
                raise ValidationError("Beli {} minimal 1!".format(rec.barang_id.name))
            elif (rec.barang_id.stok < rec.qty):
                raise ValidationError("Stok {} tidak mencukupi, hanya tersedia {}!".format(rec.barang_id.name,rec.barang_id.stok))