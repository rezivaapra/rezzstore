from odoo import api, fields, models
from odoo.exceptions import *

class ResetRating(models.TransientModel):
    _name = 'rezzstore.reset'
    
    nama_id = fields.Many2one(
        string='No. Transaksi',
        comodel_name='rezzstore.penjualankonsumen',
        required=True,
    )
    rating = fields.Selection(
        string='Berikan Rating', 
        selection=[
            ('0', 'Very Low'),
            ('1', 'Low'),
            ('2', 'Normal'),
            ('3', 'High'),
            ('4', 'Very High'),
            ('5', 'Excellent'),
        ],
        required=True,
        default='0'
    )
    @api.constrains('rating')
    def check_qualitity(self):
       for rec in self:
            if (rec.nama_id.rating == rec.rating):
                raise ValidationError("Rating {} sudah {} bro, tidak ada reset yang terjadi!".format(rec.nama_id.trx_seq,rec.nama_id.rating))

    def button_reset_rating(self):
        for rec in self:
            self.env['rezzstore.penjualankonsumen'].search([('id', '=', rec.nama_id.id)]).write({'rating' : rec.rating})
        return {
            'type': 'ir.actions.client', 
            'tag': 'reload'
        }