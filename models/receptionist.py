# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Receptionist(models.Model):
    _name = 'hospitalapp.receptionist'
    _description = "Receptionists"

    name = fields.Char(string="Name", required=True)
    surname = fields.Char(string='Surname')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone number')
