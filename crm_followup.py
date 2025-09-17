from odoo import models, fields

class CrmLeadFollowUp(models.Model):
    _inherit = 'crm.lead'

    followup_date = fields.Date(string="Follow-up Date")
    next_action = fields.Selection([
        ('call', 'Call'),
        ('email', 'Email'),
        ('meeting', 'Meeting'),
        ('demo', 'Demo'),
    ], string="Next Action")
