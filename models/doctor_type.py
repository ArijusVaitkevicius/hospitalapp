# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DoctorType(models.Model):
    _name = 'hospitalapp.doctor_type'
    _description = "Doctor types"

    name = fields.Char(string="Title", required=True)
