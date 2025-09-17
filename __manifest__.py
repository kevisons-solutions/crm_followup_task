{
    'name': 'CRM Follow-up Task',
    'version': '16.0.1.0.0',
    'summary': 'Add follow-up fields to CRM Leads',
    'category': 'CRM',
    'author': 'Kevisons Solutions Pvt Ltd',
    'website': 'https://www.kevisons.com',
    'depends': ['crm'],
    'data': [
        'security/ir.model.access.csv',
        'views/crm_followup_views.xml',
    ],
    'installable': True,
    'application': False,
}
