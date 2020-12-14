# -*- coding: utf-8 -*-
# from odoo import http


# class Customaddons/testAdvance(http.Controller):
#     @http.route('/customaddons/test_advance/customaddons/test_advance/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/customaddons/test_advance/customaddons/test_advance/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('customaddons/test_advance.listing', {
#             'root': '/customaddons/test_advance/customaddons/test_advance',
#             'objects': http.request.env['customaddons/test_advance.customaddons/test_advance'].search([]),
#         })

#     @http.route('/customaddons/test_advance/customaddons/test_advance/objects/<model("customaddons/test_advance.customaddons/test_advance"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('customaddons/test_advance.object', {
#             'object': obj
#         })
