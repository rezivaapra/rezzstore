from odoo import api, fields, models
from odoo.exceptions import *

class CancelKonsumen(models.TransientModel):
    _name = 'rezzstore.cancelkonsumen'
    
    nama_id = fields.Many2one(
        string='No. Transaksi',
        comodel_name='rezzstore.penjualankonsumen',
        required=True,
    )
    
    @api.constrains('nama_id')
    def check_qualitity(self):
       for rec in self:
            if (rec.nama_id.state == 'cancel'):
                raise ValidationError("Status {} sudah {} bro!".format(rec.nama_id.trx_seq,rec.nama_id.state))
            elif (rec.nama_id.state != 'done'):
                raise ValidationError("Status {} masih {} hanya bisa dicancel jika statusnya done!".format(rec.nama_id.trx_seq,rec.nama_id.state))

    def button_cancel_konsumen(self):
        for rec in self:
            self.env['rezzstore.penjualankonsumen'].search([('id', '=', rec.nama_id.id)]) .write({'state': 'cancel'})
        return {
            'type': 'ir.actions.client', 
            'tag': 'reload'
        }