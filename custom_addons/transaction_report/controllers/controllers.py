# -*- coding: utf-8 -*-
from odoo import http

# class Leadreport(http.Controller):
#     @http.route('/transaction_report/transaction_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/transaction_report/transaction_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('transaction_report.listing', {
#             'root': '/transaction_report/transaction_report',
#             'objects': http.request.env['transaction_report.transaction_report'].search([]),
#         })

#     @http.route('/transaction_report/transaction_report/objects/<model("transaction_report.transaction_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('transaction_report.object', {
#             'object': obj
#         })