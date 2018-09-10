from odoo import api, fields, models, _

class Partner(model.Model):
    _inherit = 'res.partner'

    company_registry = fields.Char('Company Registry')

    @api.model
    def _company_registry(self):
        return super(Partner, self)._company_registry() + ['company_registry']