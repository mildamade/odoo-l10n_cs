# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2018 - 2021 Optimal4 s.r.o. (<https://www.optimal4.cz>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Czech - Accounting',
    'version': '2.1',
    'category': 'Localization/Account Charts',
    'description': """
This is the Czech Odoo localisation necessary to run Odoo accounting for Czech businesses with:
============================================================================================================
    - a Chart Of Accounts for Czech Republic
    - VAT tax structure with VATs year 2021
    """,
    'author': 'Optimal4',
    'price': '0',
    'currency': 'EUR',
    'website': 'https://www.odoo.co.cz/odoo-l10n-cs',
    'depends': ['account', 'base_iban', 'base_vat', 'l10n_multilang'],
    'data': [
        'data/l10n_cs_cz_chart_template.xml',
        'data/account_data.xml',
#        'data/account_tax_data.xml',
#        'data/account_fiscal_position_data.xml',
#        'views\partner_view.xml',

#        'data/account_chart_template_data.yml',
    ],
    'demo' : ['demo/demo.xml'],
 
	}
