# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class customaddons/test_advance(models.Model):
#     _name = 'customaddons/test_advance.customaddons/test_advance'
#     _description = 'customaddons/test_advance.customaddons/test_advance'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
