from odoo import models, fields, api


class SaleOrderInherit(models.Model):
    _inherit = "sale.order"
    task_count = fields.Integer(compute='compute_count')
    design_file = fields.Binary(string="Design File", readonly=True)

    def compute_count(self):
        for record in self:
            record.task_count = self.env['project.task'].search_count(
                [('order_id', '=', self.name)])

    def create_task_form(self):
        return {
            'name': "Create Task",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'create.task',
            'target': 'new'
        }

    def get_tasks(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Tasks',
            'view_mode': 'tree',
            'res_model': 'project.task',
            'domain': [('order_id', '=', self.name)],
            'context': "{'create': False}"
        }

