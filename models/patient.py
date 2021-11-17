# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Patient(models.Model):
    _name = 'hospitalapp.patient'
    _description = "Patients"

    name = fields.Char(string="Name", required=True)
    surname = fields.Char(string='Surname')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone number')
    identity_number = fields.Char(string='Personal identity number')

    general_practitioner_id = fields.Many2one('hospitalapp.doctor', string="General practitioner")
    diagnosis_ids = fields.One2many('hospitalapp.diagnosis', 'patient_id', string="Diagnosis")
