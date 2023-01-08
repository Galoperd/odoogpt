# -*- coding: utf-8 -*-
{
    'name': 'OdooGPT',
    'summary': 'Make OdooBot finally useful',
    'description': """Make OdooBot useful by adding GPT intelligence 🧠""",
    'license': 'LGPL-3',
    'version': '0.0.4',
    'category': 'Productivity/Discuss',
    'author': 'thespino',
    'website': 'https://github.com/thespino',

    'depends': [
        'mail_bot',
    ],
    'external_dependencies': {
        'python': [
            'openai'
        ]
    },

    'data': [
        'security/ir.model.access.csv',

        'views/res_config_settings.xml',
        'views/odoogpt_openai_model.xml',
        'views/odoogpt_openai_interaction.xml',

        'wizard/odoogpt_openai_model_select_wizard.xml',

        'views/menu.xml',
    ],

    'assets': {
        'mail.assets_messaging': [
            'odoogpt/static/src/models/*.js',
        ],
    },

    'installable': True,
    'auto_install': False,
    'application': False,
}