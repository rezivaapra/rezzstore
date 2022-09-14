from odoo import api, fields, models
from odoo.exceptions import *

class TambahStok(models.TransientModel):
    _name = 'rezzstore.tambahstok'

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
    stok = fields.Integer(string='Banyak Stok')
    
    @api.constrains('stok')
    def check_qualitity(self):
       for rec in self:
            if (rec.stok < 0):
                raise ValidationError("Mau ngurangin stok {} bro? masa mau ditambah {}".format(rec.jasa_id.name,rec.stok))

    def button_tambah_stok(self):
        for rec in self:
            self.env['rezzstore.daftarjasa'].search([('id', '=', rec.jasa_id.id)]).write({'stok': rec.jasa_id.stok + rec.stok})
        return {
            'type': 'ir.actions.client', 
            'tag': 'reload'
        }