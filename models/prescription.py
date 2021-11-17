# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Prescription(models.Model):
    _name = 'hospitalapp.prescription'
    _description = "Prescriptions"

    date = fields.Date(string="Date", default=fields.Date.today)

    doctor_id = fields.Many2one('hospitalapp.doctor', string="Doctor")
    patient_id = fields.Many2one('hospitalapp.patient', string="Patient")

    expiration = fields.Date(string="Expiration date")



