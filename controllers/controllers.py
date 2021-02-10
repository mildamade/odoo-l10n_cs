# -*- coding: utf-8 -*-
# from odoo import http


# class /mnt/extra-addons/l10nCs(http.Controller):
#     @http.route('//mnt/extra-addons/l10n_cs//mnt/extra-addons/l10n_cs/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//mnt/extra-addons/l10n_cs//mnt/extra-addons/l10n_cs/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/mnt/extra-addons/l10n_cs.listing', {
#             'root': '//mnt/extra-addons/l10n_cs//mnt/extra-addons/l10n_cs',
#             'objects': http.request.env['/mnt/extra-addons/l10n_cs./mnt/extra-addons/l10n_cs'].search([]),
#         })

#     @http.route('//mnt/extra-addons/l10n_cs//mnt/extra-addons/l10n_cs/objects/<model("/mnt/extra-addons/l10n_cs./mnt/extra-addons/l10n_cs"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/mnt/extra-addons/l10n_cs.object', {
#             'object': obj
#         })
