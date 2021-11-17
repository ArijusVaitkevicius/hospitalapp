# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Appointment(models.Model):
    _name = 'hospitalapp.appointment'
    _description = "Appointments"

    receptionist_id = fields.Many2one('hospitalapp.receptionist', string="Receptionist")

    date = fields.Datetime(string="Date and time")

    doctor_id = fields.Many2one('hospitalapp.doctor', string="Doctor")
    patient_id = fields.Many2one('hospitalapp.patient', string="Patient")
