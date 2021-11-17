from odoo import models, fields, api


class User(models.Model):
    _inherit = 'res.users'

    doctor = fields.Boolean(string="Doctor", default=False, )
    receptionist = fields.Boolean(string="Receptionist", default=False)
