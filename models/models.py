from odoo import api, fields, models

class ResPartner(model.Model):
    _inherit = 'res.partner'

    company_registry = fields.Char('Company Registry', size=64)

    @api.model
    def _company_registry(self):
        return super(ResPartner, self)._company_registry() + ['company_registry']