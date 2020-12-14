from odoo import models, fields, api


class CreateTask(models.TransientModel):
    _name = "create.task"
    task_id = fields.Char(string="Task Name", required=True)
    order_id = fields.Char(string="Order", readonly=True)
    project_id = fields.Many2one('project.project', string='Select Project', required=True)
    user_ids = fields.Many2one('res.users',
                              string='Assigned to',
                              index=True, tracking=True, required=True)
    partner_id = fields.Many2one('res.partner', string='Customer')

    deadline = fields.Date(required=True)

    res_model = fields.Char()
    res_id = fields.Integer()

    @api.model
    def default_get(self, fields):
        res = super(CreateTask, self).default_get(fields)
        res_id = self._context.get('active_id')
        res_model = self._context.get('active_model')
        res.update({'res_id': res_id, 'res_model': res_model})
        if res['res_id'] and res['res_model'] == 'sale.order':
            record = self.env[res_model].browse(res_id)
            res.update({
                'order_id': record.name,
                'partner_id': record.partner_id,
            })
        return res

    def create_task(self):
        if self.project_id:
            # print("1")
            vals = {'name': self.task_id,
                    'user_id': self.user_ids.id,
                    'partner_id': self.partner_id.id,
                    'date_deadline': self.deadline,
                    'order_id': self.order_id}
            self.project_id.write({'task_ids': [(0, 0, vals)]})
