from odoo import models, fields, api
from odoo.exceptions import ValidationError 

class ToDoList(models.Model):
    _name = "todo.task"
    _description = "Todo Task"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    task_name = fields.Char(required=1, tracking=1)
    user_id = fields.Many2one(comodel_name="res.partner", required=1, tracking=1)
    desc = fields.Char(tracking=1)
    due_date = fields.Date(required=1, tracking=1)
    estimated_time = fields.Float(
        tracking=1, help="Estimated effort required to complete this task (in hours)."
    )
    total_hours = fields.Float(compute="_compute_total_hours", default=0.0)

    line_ids = fields.One2many(
        comodel_name="todo.task.line", inverse_name="todo_list_id"
    )

    active = fields.Boolean(default=1)
    is_late = fields.Boolean()

    status = fields.Selection(
        [
            ("new", "New"),
            ("in_progress", "In Progress"),
            ("completed", "Completed"),
            ("closed", "Closed"),
        ],
        default="new",
        required=1,
        tracking=1,
    )

    _sql_constraints = [
        ("unique_name", "UNIQUE(task_name)", "This task is already exist."), 
    ]

    def action_new(self):
        for rec in self:
            rec.status = "new"

    def action_in_progress(self):
        for rec in self:
            rec.status = "in_progress"

    def action_completed(self):
        for rec in self:
            rec.status = "completed"

    def action_closed(self):
        for rec in self:
            rec.status = "closed"

    def check_due_date(self):
        todo_task_ids = self.search([])
        for rec in todo_task_ids:
            if rec.due_date and rec.due_date < fields.date.today():
                rec.is_late = 1
            else:
                rec.is_late = 0

    @api.depends("line_ids","line_ids.hours")
    def _compute_total_hours(self):
        for rec in self:
            rec.total_hours = 0
            for line in rec.line_ids:
                rec.total_hours += line.hours

    @api.constrains("total_hours", "estimated_time")
    def _check_estimated_time(self):
        for rec in self:
            if rec.total_hours > rec.estimated_time:
                raise ValidationError("Total hours exceed the Estimated time")


class ToDoListLine(models.Model):
    _name = "todo.task.line"

    date = fields.Date(required=1)
    hours = fields.Float(required=1)
    description = fields.Char(required=1)

    todo_list_id = fields.Many2one(comodel_name="todo.task")

    @api.model
    def write(self, vals):
        result = super().write(vals)
        for rec in self.mapped('todo_list_id'):
            rec._check_estimated_time()
        return result
