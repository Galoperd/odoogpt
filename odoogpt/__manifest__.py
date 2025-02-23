# -*- coding: utf-8 -*-
{
    'name': 'OdooGPT',
    'summary': 'Make OdooBot finally useful. Integrate with OpenAI ChatGPT (GPT-3)',
    'description': """Make OdooBot useful by adding OpenAI GPT-3 intelligence 🧠""",
    'license': 'LGPL-3',
    'version': '15.0.1.0.0',
    'category': 'Productivity/Discuss',
    'author': 'thespino',
    'website': 'https://odoogpt.thespino.dev',

    'depends': [
        'base',
        'base_setup',
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
        'views/odoogpt_openai_log.xml',
        'views/odoogpt_openai_file.xml',
        'views/odoogpt_openai_fine_tune.xml',

        'wizard/odoogpt_openai_model_select_wizard.xml',
        'wizard/odoogpt_openai_file_create_wizard.xml',
        'wizard/odoogpt_openai_fine_tune_create_wizard.xml',

        'views/menu.xml',
    ],

    'assets': {
        'web.assets_backend': [
            'odoogpt/static/src/models/messaging_initializer.js',
        ],
    },

    'images': [
        'static/description/cover/odoogpt.png',
    ],

    'installable': True,
    'auto_install': False,
    'application': False,
}
