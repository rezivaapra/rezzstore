from odoo import api, fields, models
from odoo.exceptions import *

class GantiStatus(models.TransientModel):
    _name = 'rezzstore.gantistatus'

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
    status = fields.Selection([
        ('ready', 'Ready'),
        ('not_ready', 'Not Ready')
    ], string='Status',
       required=True,
       default='ready')
    
    
    @api.constrains('status')
    def check_qualitity(self):
       for rec in self:
            if (rec.status == rec.jasa_id.status):
                raise ValidationError("Status {} sudah {} bro!".format(rec.jasa_id.name,rec.jasa_id.status))
    
    def button_ganti_status(self):
        for rec in self:
            self.env['rezzstore.daftarjasa'].search([('id', '=', rec.jasa_id.id)]).write({'status': rec.status})
        return {
            'type': 'ir.actions.client', 
            'tag': 'reload'
        }