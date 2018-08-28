# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (C) 2018 - Milda Dvorak, milda.dvorak@optimal4.cz

{
    'name' : 'Czech - Accounting',
    'version' : '0.1',
    'author' : 'Milda Dvorak (Optimal 4 s.r.o.)',
    'website': 'http://www.optimal4.cz',
    'category': 'Localization',
    'description': """
This is the module to manage the accounting chart and taxes for Czech in Odoo.
==================================================================================

Full accounts for czech accounting. Basic VAT for local, Import/Export EU and other world. 
Modul for ver. odoo 11.0. Base on old Poland and Czech accounting modules. Thank you.
    """,
    'depends' : [
        'account',
        'base_iban',
        'base_vat',
    ],
    'data': [
              'data/l10n_cs_chart_data.xml',
              'data/account_data.xml',
              'data/account_tax_data.xml',
              'data/account_fiscal_position_data.xml',
              'data/res_country_state_data.xml',
              'data/account_chart_template_data.yml'
    ],
    'post_init_hook': '_preserve_tag_on_taxes',
}
