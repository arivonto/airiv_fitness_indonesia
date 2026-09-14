{
    "name": "AIRIV Active Wellness",
    "version": "18.0.1.1.0",
    "category": "Services/Fitness",
    "summary": "Adaptive fitness, wellness scoring, membership, and progress journeys",
    "description": """
AIRIV Active Wellness turns Odoo into a human-centered fitness platform.

The first release provides members, trainers, membership plans, energy-aware
assessments, wellness scoring, and progress tracking.
""",
    "author": "AIRIV",
    "website": "https://airiv.id",
    "license": "LGPL-3",
    "images": ["static/description/banner.png"],
    "depends": ["base", "contacts", "product", "airiv_os_core"],
    "data": [
        "security/ir.model.access.csv",
        "data/fitness_data.xml",
        "views/fitness_views.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}
