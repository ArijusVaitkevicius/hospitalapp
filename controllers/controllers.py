# -*- coding: utf-8 -*-
# from odoo import http


# class Hospitalapp(http.Controller):
#     @http.route('/hospitalapp/hospitalapp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hospitalapp/hospitalapp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hospitalapp.listing', {
#             'root': '/hospitalapp/hospitalapp',
#             'objects': http.request.env['hospitalapp.hospitalapp'].search([]),
#         })

#     @http.route('/hospitalapp/hospitalapp/objects/<model("hospitalapp.hospitalapp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hospitalapp.object', {
#             'object': obj
#         })
