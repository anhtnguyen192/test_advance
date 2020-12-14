from odoo import models, fields, api


class SaleOrderInherit(models.Model):
    _inherit = "sale.order"
    design_file = fields.Binary(string="Design File", readonly=True)

    def create_task_form(self):
        return {
            'name': "Create Task",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'create.task',
            'target': 'new'
        }


class ProjectTaskInherit(models.Model):
    _inherit = "project.task"
    design_file = fields.Binary(string="Design File")
    order_id = fields.Char()
    current_user = fields.Many2one('res.users', 'Current User', default=lambda self: self.env.uid)

    is_1x = fields.Boolean(
        string='1x', default=False)
    is_2x = fields.Boolean(
        string='2x', default=True)
    is_3x = fields.Boolean(
        string='3x', default=True)
    is_uid_assigned = fields.Boolean(
        string="uA", compute="is_current_user_assigned"
    )

    def is_current_user_assigned(self):
        if self.user_id == self.current_user:
            self.is_uid_assigned = True
        else:
            self.is_uid_assigned = False

    def accept_task(self):
        if self.stage_id:
            self.is_1x = True
            self.is_2x = False
            self.stage_id = self.env.ref('test_advance.project_stage_1x').id

    def send_for_approval(self):
        if self.stage_id:
            self.is_2x = True
            self.is_3x = False
            self.stage_id = self.env.ref('test_advance.project_stage_2x').id


    def accept_task_result(self):
        if self.stage_id:
            self.is_3x = True
            self.stage_id = self.env.ref('test_advance.project_stage_3x').id
            order = self.env['sale.order'].search([])
            for rec in order:
                if rec.name == self.order_id:
                    rec.design_file = self.design_file

    def decline_task_result(self):
        if self.stage_id:
            self.is_2x = False
            self.is_3x = True
            self.stage_id = self.env.ref('test_advance.project_stage_1x').id

