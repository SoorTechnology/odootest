# -*- coding: utf-8 -*-
{
    "name": "Sale-Invoice Report Extension",
    'author': 'Warlock Technologies Pvt Ltd.',
    "description": """Sale-Invoice Report Extension""",
    "summary": """Sale-Invoice Report Extension""",
    "version": "13.0.1.0.0",
    "support": "info@warlocktechnologies.com",
    "license": "LGPL-3",
    "category": "Accounting",
    "depends": ['web', 'sale', 'sale_management', 'account'],
    "data": [
        "report/report_templates.xml",
        "report/report_sale_order.xml",
        "report/report_invoice.xml",
    ],
    'installable': True,
}
