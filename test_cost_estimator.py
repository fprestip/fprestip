import math
from cost_estimator import Item, ProjectCost

def test_project_total():
    materials = [Item("Material", 2, 10)]
    labor = [Item("Labor", 3, 15)]
    equipment = [Item("Equipment", 1, 50)]
    project = ProjectCost(
        materials=materials,
        labor=labor,
        equipment=equipment,
        overhead_percent=10,
        profit_percent=5,
    )
    subtotal = 2 * 10 + 3 * 15 + 1 * 50
    overhead = subtotal * 0.10
    expected_total = subtotal + overhead + (subtotal + overhead) * 0.05
    assert math.isclose(project.total(), expected_total)
