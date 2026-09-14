# AIRIV Active Wellness

[![Odoo 18](https://img.shields.io/badge/Odoo-18.0-714B67)](https://www.odoo.com/) [![License LGPL-3](https://img.shields.io/badge/license-LGPL--3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0.html) [![AIRIV](https://img.shields.io/badge/AIRIV-Active%20Wellness-0F766E)](https://airiv.id)

Human-centered fitness and wellness operations for Odoo 18: members, trainers, membership plans, energy-aware assessments, explainable wellness scoring, and progress journeys.

## Core Capabilities & Architecture

- Member and trainer profiles with active membership periods.
- Membership plans, durations, benefits, and ownership context.
- Energy-aware assessments with an explainable wellness score.
- Progress milestones, check-ins, coaching notes, and next actions.

The module connects member and plan context to an AIRIV wellness assessment and progress journey layer. Scores support coaching review and are not medical diagnoses.

## Feature & Workflow Automation

1. Configure membership plans, trainers, assessment fields, and access groups.
2. Register a member and assign an active plan and trainer.
3. Record energy-aware assessment inputs and review the score explanation.
4. Track milestones, check-ins, coaching notes, and next actions.

## Technical Specifications

- Odoo: `18.0.1.1.0`, Community Edition compatible
- License: LGPL-3
- Dependencies: `base`, `contacts`, `product`, `airiv_os_core`
- Main domain: members, trainers, plans, assessments, scores, and progress
- Store assets: `static/description/icon.png`, `banner.png`, and fragment-safe `index.html`

## Installation Guidance

Clone branch `18.0` into the Odoo addons path, install dependencies, restart Odoo, update the Apps list, and install the module. Configure plans and assessment policy before use.

## Configuration Checklist

- Confirm membership periods, benefits, and trainer ownership.
- Verify member identity, contact context, and active plan.
- Review assessment inputs and score explanation before coaching decisions.
- Record milestones, check-ins, notes, and next actions.

## Repository Layout

```text
airiv_fitness_indonesia/
  models/                 Fitness and wellness models
  data/                   Demo and reference data
  views/                  Member and operations views
  security/               Access rules
  static/description/     Apps Store assets
  __manifest__.py         Odoo metadata
```

## Contact Info

- Author: AIRIV
- Website: https://airiv.id
- GitHub: https://github.com/arivonto
- Repository: https://github.com/arivonto/airiv_fitness_indonesia
- Odoo series: `18.0`

## Quality Gate

The repository includes the standard-library Apps Store audit and GitHub Actions validation for manifest metadata, required assets, XML-safe description markup, repository hygiene, and module structure.
