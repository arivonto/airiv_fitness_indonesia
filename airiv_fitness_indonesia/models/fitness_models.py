from odoo import api, fields, models


class AirivFitnessTrainer(models.Model):
    _name = "airiv.fitness.trainer"
    _description = "AIRIV Fitness Trainer"
    _order = "name"

    name = fields.Char(required=True)
    partner_id = fields.Many2one("res.partner", string="Contact", ondelete="set null")
    specialty = fields.Char()
    active = fields.Boolean(default=True)
    member_ids = fields.One2many("airiv.fitness.member", "trainer_id")
    member_count = fields.Integer(compute="_compute_member_count")

    @api.depends("member_ids")
    def _compute_member_count(self):
        for trainer in self:
            trainer.member_count = len(trainer.member_ids)


class AirivFitnessMember(models.Model):
    _name = "airiv.fitness.member"
    _description = "AIRIV Fitness Member"
    _order = "name"

    name = fields.Char(required=True)
    partner_id = fields.Many2one("res.partner", string="Contact", required=True, ondelete="restrict")
    trainer_id = fields.Many2one("airiv.fitness.trainer", string="Coach", ondelete="set null")
    membership_plan_id = fields.Many2one("airiv.fitness.membership.plan", string="Membership Plan")
    membership_start = fields.Date(default=fields.Date.context_today)
    membership_end = fields.Date()
    goal = fields.Selection([
        ("strength", "Strength"), ("weight", "Weight Management"),
        ("endurance", "Endurance"), ("wellness", "General Wellness"),
    ], default="wellness", required=True)
    energy_level = fields.Selection([(str(i), str(i)) for i in range(1, 6)], default="3")
    wellness_score = fields.Integer(compute="_compute_wellness_score", store=True)
    assessment_ids = fields.One2many("airiv.fitness.assessment", "member_id")
    progress_ids = fields.One2many("airiv.fitness.progress", "member_id")
    active = fields.Boolean(default=True)

    @api.depends("energy_level", "progress_ids", "assessment_ids")
    def _compute_wellness_score(self):
        for member in self:
            energy = int(member.energy_level or 3) * 20
            consistency = min(len(member.progress_ids) * 5, 30)
            assessment = min(len(member.assessment_ids) * 5, 20)
            member.wellness_score = min(energy + consistency + assessment, 100)

    def action_log_assessment(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": "Energy Assessment",
            "res_model": "airiv.fitness.assessment",
            "view_mode": "form",
            "target": "new",
            "context": {"default_member_id": self.id},
        }


class AirivFitnessMembershipPlan(models.Model):
    _name = "airiv.fitness.membership.plan"
    _description = "AIRIV Fitness Membership Plan"
    _order = "sequence, name"

    name = fields.Char(required=True)
    sequence = fields.Integer(default=10)
    duration_days = fields.Integer(default=30, required=True)
    price = fields.Float(required=True)
    product_id = fields.Many2one("product.product", string="Odoo Product")
    active = fields.Boolean(default=True)


class AirivFitnessAssessment(models.Model):
    _name = "airiv.fitness.assessment"
    _description = "AIRIV Fitness Energy Assessment"
    _order = "date desc"

    member_id = fields.Many2one("airiv.fitness.member", required=True, ondelete="cascade")
    date = fields.Date(default=fields.Date.context_today, required=True)
    sleep_quality = fields.Selection([(str(i), str(i)) for i in range(1, 6)], default="3", required=True)
    stress_level = fields.Selection([(str(i), str(i)) for i in range(1, 6)], default="3", required=True)
    soreness_level = fields.Selection([(str(i), str(i)) for i in range(1, 6)], default="1", required=True)
    energy_level = fields.Selection([(str(i), str(i)) for i in range(1, 6)], default="3", required=True)
    recommendation = fields.Selection(compute="_compute_recommendation", selection=[
        ("full", "Full Workout"), ("light", "Light Workout"),
        ("mobility", "Mobility / Recovery"), ("rest", "Rest Day"),
    ])
    notes = fields.Text()

    @api.depends("sleep_quality", "stress_level", "soreness_level", "energy_level")
    def _compute_recommendation(self):
        for record in self:
            energy = int(record.energy_level or 3)
            stress = int(record.stress_level or 3)
            soreness = int(record.soreness_level or 1)
            sleep = int(record.sleep_quality or 3)
            if soreness >= 5 or energy == 1:
                record.recommendation = "rest"
            elif energy <= 2 or sleep <= 2 or stress >= 5:
                record.recommendation = "mobility"
            elif energy == 3 or stress == 4:
                record.recommendation = "light"
            else:
                record.recommendation = "full"


class AirivFitnessProgress(models.Model):
    _name = "airiv.fitness.progress"
    _description = "AIRIV Fitness Progress"
    _order = "date desc"

    member_id = fields.Many2one("airiv.fitness.member", required=True, ondelete="cascade")
    date = fields.Date(default=fields.Date.context_today, required=True)
    weight = fields.Float()
    body_fat = fields.Float(string="Body Fat %")
    waist = fields.Float(string="Waist (cm)")
    workout_minutes = fields.Integer()
    notes = fields.Text()
