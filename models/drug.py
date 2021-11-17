# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Drug(models.Model):
    _name = 'hospitalapp.drug'
    _description = "Drugs"

    name = fields.Char(string="Title", required=True)
