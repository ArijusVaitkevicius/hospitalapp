# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Doctor(models.Model):
    _name = 'hospitalapp.doctor'
    _description = "Doctors"

    name = fields.Char(string="Name", required=True)
    surname = fields.Char(string='Surname')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone number')

    doctor_type_ids = fields.Many2many('hospitalapp.doctor_type', string='Doctor types')

