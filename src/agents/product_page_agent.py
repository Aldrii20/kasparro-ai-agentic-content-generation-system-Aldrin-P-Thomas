from typing import Dict
from src.agents.base_agent import BaseAgent
from src.logic_blocks.blocks_registry import get_block
from src.models.product_model import Product


class ProductPageAgent(BaseAgent):
    """Generates product description pages."""
    
    def validate_input(self, input_data) -> bool:
        return isinstance(input_data, Product)
    
    def execute(self, product: Product) -> Dict:
        """Generate product page."""
        page_data = {
            "product_name": product.name,
            "concentration": product.concentration,
            "price": product.price,
            "skin_type": product.skin_type,
            "summary": f"{product.name} is a premium serum for skin brightening and rejuvenation.",
            "benefits": product.benefits,
            "ingredients": product.key_ingredients,
            "usage": product.how_to_use,
            "side_effects": product.side_effects,
            "full_description": self._build_full_description(product),
        }
        
        return page_data
    
    def _build_full_description(self, product: Product) -> str:
        """Build comprehensive description using logic blocks."""
        parts = [
            get_block("concentration").apply(product),
            get_block("skin_type").apply(product),
            get_block("benefits").apply(product),
            get_block("ingredients").apply(product),
            get_block("usage").apply(product),
            get_block("warnings").apply(product),
        ]
        return " | ".join(parts)
