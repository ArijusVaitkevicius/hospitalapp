# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PrescriptionLine(models.Model):
    _name = 'hospitalapp.prescription_line'
    _description = "Prescription lines"

    prescription_id = fields.Many2one('hospitalapp.prescription', string="Prescription")
    drugs_id = fields.Many2one('hospitalapp.drug', string="Drugs")

    qty = fields.Integer(string="Quantity")
