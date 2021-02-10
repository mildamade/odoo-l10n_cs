# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class /mnt/extra-addons/l10n_cs(models.Model):
#     _name = '/mnt/extra-addons/l10n_cs./mnt/extra-addons/l10n_cs'
#     _description = '/mnt/extra-addons/l10n_cs./mnt/extra-addons/l10n_cs'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
