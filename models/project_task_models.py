# -*- coding: utf-8 -*-

from odoo import models, fields, _


class CustomProjectTask(models.Model):
    _inherit = "project.task"

    total_fixed_prod = fields.Monetary(
        string='Total FPV', 
        compute='_suma_fixed_prod_value',
        readonly=True
    )

    
    def _suma_fixed_prod_value(self):
        for rec in self:
            val = 0.0
            for vstask in self.env['project.task'].search([('parent_id', 'child_of', rec.id)]):
                if vstask:
                    val += vstask.fixed_production_value
                rec.total_fixed_prod = val
  
