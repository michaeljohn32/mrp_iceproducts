# -*- coding: utf-8 -*-
from openerp import http

# class MrpIceproducts(http.Controller):
#     @http.route('/mrp_iceproducts/mrp_iceproducts/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mrp_iceproducts/mrp_iceproducts/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mrp_iceproducts.listing', {
#             'root': '/mrp_iceproducts/mrp_iceproducts',
#             'objects': http.request.env['mrp_iceproducts.mrp_iceproducts'].search([]),
#         })

#     @http.route('/mrp_iceproducts/mrp_iceproducts/objects/<model("mrp_iceproducts.mrp_iceproducts"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mrp_iceproducts.object', {
#             'object': obj
#         })