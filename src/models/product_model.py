from dataclasses import dataclass
from typing import List


@dataclass
class Product:
    """Represents a product with marketing attributes."""
    name: str
    concentration: str
    skin_type: List[str]
    key_ingredients: List[str]
    benefits: List[str]
    how_to_use: str
    side_effects: str
    price: str
    
    def to_dict(self) -> dict:
        """Convert product to dictionary."""
        return {
            "name": self.name,
            "concentration": self.concentration,
            "skin_type": self.skin_type,
            "key_ingredients": self.key_ingredients,
            "benefits": self.benefits,
            "how_to_use": self.how_to_use,
            "side_effects": self.side_effects,
            "price": self.price,
        }


# Fictional comparison product
COMPARISON_PRODUCT = Product(
    name="RadiantGlow Serum Pro",
    concentration="15% Vitamin C + 2% Niacinamide",
    skin_type=["All skin types"],
    key_ingredients=["Vitamin C", "Niacinamide", "Glycerin", "Ferulic Acid"],
    benefits=["Brightening", "Anti-aging", "Pore minimization"],
    how_to_use="Apply 3-4 drops morning and night after cleansing",
    side_effects="May cause slight dryness in very dry skin",
    price="₹1,299",
)
