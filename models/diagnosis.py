# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Diagnosis(models.Model):
    _name = 'hospitalapp.diagnosis'
    _description = "Diagnosis"

    date = fields.Date(string="Date", default=fields.Date.today)
    diagnosis = fields.Text(string="Diagnosis")
    patient_id = fields.Many2one('hospitalapp.patient', string="Patient")
    prescription_id = fields.Many2one('hospitalapp.prescription', string="Prescription")


