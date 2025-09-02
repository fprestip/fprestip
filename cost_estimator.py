from dataclasses import dataclass
from typing import List

@dataclass
class Item:
    """Represents a cost item with a quantity and a unit cost."""
    name: str
    quantity: float
    unit_cost: float

    def total(self) -> float:
        """Return the total cost for the item."""
        return self.quantity * self.unit_cost

@dataclass
class ProjectCost:
    """Estimate cost of a construction project using first principles."""
    materials: List[Item]
    labor: List[Item]
    equipment: List[Item]
    overhead_percent: float = 0.0
    profit_percent: float = 0.0

    def total_materials(self) -> float:
        return sum(item.total() for item in self.materials)

    def total_labor(self) -> float:
        return sum(item.total() for item in self.labor)

    def total_equipment(self) -> float:
        return sum(item.total() for item in self.equipment)

    def subtotal(self) -> float:
        return self.total_materials() + self.total_labor() + self.total_equipment()

    def overhead(self) -> float:
        return self.subtotal() * self.overhead_percent / 100

    def profit(self) -> float:
        return (self.subtotal() + self.overhead()) * self.profit_percent / 100

    def total(self) -> float:
        return self.subtotal() + self.overhead() + self.profit()

if __name__ == "__main__":
    # Example usage
    materials = [
        Item("Concrete", 100, 120),
        Item("Steel", 50, 300),
    ]
    labor = [
        Item("Carpenter", 80, 40),
        Item("Electrician", 60, 50),
    ]
    equipment = [
        Item("Crane", 10, 500),
    ]
    project = ProjectCost(
        materials=materials,
        labor=labor,
        equipment=equipment,
        overhead_percent=10,
        profit_percent=5,
    )
    print(f"Total project cost: ${project.total():.2f}")
