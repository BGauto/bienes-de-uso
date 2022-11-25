# -*- coding: utf-8 -*-
# from odoo import http


# class ProductFixedAssets(http.Controller):
#     @http.route('/product_fixed_assets/product_fixed_assets/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_fixed_assets/product_fixed_assets/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_fixed_assets.listing', {
#             'root': '/product_fixed_assets/product_fixed_assets',
#             'objects': http.request.env['product_fixed_assets.product_fixed_assets'].search([]),
#         })

#     @http.route('/product_fixed_assets/product_fixed_assets/objects/<model("product_fixed_assets.product_fixed_assets"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_fixed_assets.object', {
#             'object': obj
#         })
