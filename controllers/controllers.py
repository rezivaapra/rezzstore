# -*- coding: utf-8 -*-
# from odoo import http


# class Rezzstore(http.Controller):
#     @http.route('/rezzstore/rezzstore', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rezzstore/rezzstore/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('rezzstore.listing', {
#             'root': '/rezzstore/rezzstore',
#             'objects': http.request.env['rezzstore.rezzstore'].search([]),
#         })

#     @http.route('/rezzstore/rezzstore/objects/<model("rezzstore.rezzstore"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rezzstore.object', {
#             'object': obj
#         })
