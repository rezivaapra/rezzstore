from odoo import api, fields, models
from odoo.exceptions import *

class GantiHarga(models.TransientModel):
    _name = 'rezzstore.gantiharga'

    def default_jasa_id(self):
        active_ids = self.env.context.get("active_ids")
        if active_ids:
            return self.env["rezzstore.daftarjasa"].browse(active_ids[0])
        return self.env["rezzstore.daftarjasa"]

    jasa_id = fields.Many2one(
        string='Nama Jasa',
        comodel_name='rezzstore.daftarjasa',
        required=True,
        default=default_jasa_id
    )
    jenis = fields.Selection([
        ('harga_kon', 'Harga Konsumen'),
        ('harga_res', 'Harga Reseller')
    ], string='Jenis Harga',
       required=True,
       default='harga_kon'
    )
    harga = fields.Integer(string='Update Harga')
    
    @api.constrains('harga')
    def check_qualitity(self):
       for rec in self:
            if (rec.harga <= 0):
                raise ValidationError("Harga {} tidak boleh {}!".format(rec.jasa_id.name,rec.harga))

    def button_ganti_harga(self):
        for rec in self:
            self.env['rezzstore.daftarjasa'].search([('id', '=', rec.jasa_id.id)]) .write({rec.jenis : rec.harga})
        return {
            'type': 'ir.actions.client', 
            'tag': 'reload'
        }