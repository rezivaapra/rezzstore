from odoo import api, fields, models


class DaftarReseller(models.Model):
    _name = 'rezzstore.reseller'
    _description = 'New Description'

    name = fields.Char(string='Nama Reseller')
    tgl_join = fields.Datetime(
        string='Tanggal Bergabung',
        required=True,
        default=fields.Datetime.now()
    )
    no_hp = fields.Char(string='No. Handphone')
    email = fields.Char(string='Alamat E-Mail')
    penjualan_ids = fields.One2many(
        comodel_name='rezzstore.penjualanreseller', 
        inverse_name='daftarreseller_id', 
        string='Daftar Jasa'
    )