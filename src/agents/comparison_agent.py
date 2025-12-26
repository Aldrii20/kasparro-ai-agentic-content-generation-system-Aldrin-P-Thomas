from typing import Dict
from src.agents.base_agent import BaseAgent
from src.logic_blocks.blocks_registry import (
    compare_ingredients, compare_benefits, compare_prices
)
from src.models.product_model import Product


class ComparisonAgent(BaseAgent):
    """Generates product comparison pages."""
    
    def __init__(self, name: str, comparison_product: Product):
        super().__init__(name)
        self.comparison_product = comparison_product
    
    def validate_input(self, input_data) -> bool:
        return isinstance(input_data, Product) and isinstance(self.comparison_product, Product)
    
    def execute(self, product: Product) -> Dict:
        """Generate comparison page."""
        comparison_data = {
            "title": f"{product.name} vs {self.comparison_product.name}",
            "products": [
                {
                    "name": product.name,
                    "concentration": product.concentration,
                    "skin_type": product.skin_type,
                    "price": product.price,
                },
                {
                    "name": self.comparison_product.name,
                    "concentration": self.comparison_product.concentration,
                    "skin_type": self.comparison_product.skin_type,
                    "price": self.comparison_product.price,
                },
            ],
            "ingredients_comparison": compare_ingredients(product, self.comparison_product),
            "benefits_comparison": compare_benefits(product, self.comparison_product),
            "price_comparison": compare_prices(product, self.comparison_product),
        }
        
        return comparison_data
