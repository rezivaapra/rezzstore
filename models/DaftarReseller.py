from odoo import api, fields, models


class DaftarReseller(models.Model):
    _name = 'rezzstore.reseller'
    _description = 'New Description'

    name = fields.Char(
        string='Nama Reseller',
        required=True
    )
    gender = fields.Selection([
        ('lakilaki', 'Laki-Laki'),
        ('perempuan', 'Perempuan'),
    ], 
        string='Jenis Kelamin',
        required=True
    )
    tgl_lahir = fields.Date(string='Tanggal Lahir')
    tgl_join = fields.Datetime(
        string='Tanggal Bergabung',
        required=True,
        default=fields.Datetime.now()
    )
    no_hp = fields.Char(string='No. Handphone')
    email = fields.Char(string='Alamat E-Mail')
    alamat = fields.Char(string='Alamat')
    foto = fields.Image('Foto Diri')
    penjualan_ids = fields.One2many(
        comodel_name='rezzstore.penjualanreseller', 
        inverse_name='daftarreseller_id', 
        string='Daftar Jasa'
    )