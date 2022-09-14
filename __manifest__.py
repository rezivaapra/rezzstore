# -*- coding: utf-8 -*-
{
    'name': "rezzstore",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'report_xlsx'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/daftar_game.xml',
        'views/daftar_jasa.xml',
        'views/daftar_reseller.xml',
        'views/penjualan_reseller.xml',
        'data/trx_res_sequence.xml',
        'views/penjualan_konsumen.xml',
        'data/trx_kon_sequence.xml',
        'wizzard/ganti_status.xml',
        'wizzard/tambah_stok.xml',
        'wizzard/ganti_harga.xml',
        'wizzard/cancel_reseller.xml',
        'wizzard/cancel_konsumen.xml',
        'wizzard/berikan_rating.xml',
        'wizzard/reset_rating.xml',
        'report/report.xml',
        'report/print_faktur_reseller.xml',
        'report/print_faktur_konsumen.xml',
        'report/print_reseller.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
