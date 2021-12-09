# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'CRM Custom',
    'version': '12.0.0.0.1',
    'category': 'Extra Tools',
    'summary': 'Module for custom attributes in CRM',
    'sequence': '1',
    'author': "Tatiany Mori",
    'depends': [
        'crm'
    ],
    'data': [
        'security/crm_security.xml',
        'security/ir.model.access.csv',

        'views/crm_lead_views.xml',
    ],
    'demo': [],
    'css': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
