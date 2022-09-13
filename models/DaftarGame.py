from odoo import api, fields, models


class DaftarGame(models.Model):
    _name = 'rezzstore.daftargame'
    _description = 'New Description'

    name = fields.Char(string='Nama Game')
    kode_game = fields.Char(string='Kode Game')
    jlh_jasa = fields.Char(
        compute='_compute_jlh_jasa', 
        string='Jumlah Jasa'
    )
    daftarjasa_ids = fields.One2many(
        comodel_name='rezzstore.daftarjasa', 
        inverse_name='daftargame_id', 
        string='Daftar Jasa'
    )
    daftar = fields.Char(string='Daftar Jasa')

    @api.depends('daftarjasa_ids')
    def _compute_jlh_jasa(self):
        for rec in self:
            a = self.env['rezzstore.daftarjasa'].search([('daftargame_id', '=', rec.id)]).mapped('name')
            rec.jlh_jasa = len(a)
            rec.daftar = a