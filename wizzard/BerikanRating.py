from odoo import api, fields, models
from odoo.exceptions import *

class BerikanRating(models.TransientModel):
    _name = 'rezzstore.rating'
    
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
            if (rec.nama_id.state != 'done'):
                raise ValidationError("Status {} tidak bisa dibari rating karena status masih {} bro, tunggu statusnya jadi Done ya!".format(rec.nama_id.trx_seq,rec.nama_id.state))
            elif (rec.nama_id.rating != '0'):
                raise ValidationError("Anda tidak dapat merubah rating transaksi {} yang sudah direkam, rating yang sudah diberikan {}!".format(rec.nama_id.trx_seq,rec.nama_id.rating))
            elif (rec.rating == '0'):
                raise ValidationError("Mohon berikan rating {} setidaknya bintang 1, karena rating transaksi ini sudah {}!".format(rec.nama_id.trx_seq,rec.nama_id.rating))

    def button_berikan_rating(self):
        for rec in self:
            self.env['rezzstore.penjualankonsumen'].search([('id', '=', rec.nama_id.id)]).write({'rating' : rec.rating})
        return {
            'type': 'ir.actions.client', 
            'tag': 'reload'
        }