from odoo import api, fields, models

class l10n_cs(models.Model):
#    _name = 'l10n_cs.l10n_cs'
#    _description = 'l10n_cs.l10n_cs'
    _inherit = 'res.partner'

    company_registry = fields.Char('Company Registry', size=64)

