{
    'name': 'GCC Invoice Layout Customization',
    'version': '18.0.1.0.0',
    'category': 'Accounting',
    'summary': 'Custom Invoice Layout for GCC (Arabic & English) - Tax Invoice Format',
    'description': """
        This module customizes the Odoo invoice report to match the GCC Tax Invoice format.
        Features:
        - Custom layout matching the approved design
        - Arabic and English support
        - Custom Arabic font support
        - QR Code integration
        - Dual-language invoice headers
    """,
    'author': 'Your Company',
    'license': 'OPL-1',
    'depends': [
        'account',
        'sale',
    ],
    'data': [
        'report/invoice_template.xml',
        'report/invoice_report.xml',
    ],
    'assets': {
        'web.report_assets_common': [
            'gcc_invoice_layout/static/src/css/invoice_report.css',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}