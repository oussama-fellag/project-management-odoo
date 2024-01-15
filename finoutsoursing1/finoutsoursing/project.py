from odoo import models, fields

class project(models.Model):
    _inherit = 'project.task.type'
    media_comments = fields.Text()
