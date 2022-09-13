from odoo import api, fields, models


class DaftarJasa(models.Model):
    _name = 'rezzstore.daftarjasa'
    _description = 'New Description'

    name = fields.Char(string='Jenis Jasa')
    stok = fields.Integer(string='Stok')
    harga_res = fields.Integer(string='Harga Reseller')
    harga_kon = fields.Integer(string='Harga Konsumen')
    daftargame_id = fields.Many2one(
        'rezzstore.daftargame', 
        string='Nama Game'
    )
    kode_jasa = fields.Char(string='Kode Jasa')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('ready', 'Ready'),
        ('not_ready', 'Not Ready')
    ],
        string='Status',
        required=True,
        readonly=True,
        default='draft'
    )