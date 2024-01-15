from odoo import models, fields

class ProjectTask(models.Model):
    _inherit = 'project.task'

    name_projet = fields.Char(string="Nom Projet")
