from typing import Callable, Dict, List
from src.models.product_model import Product


class LogicBlock:
    """Reusable content transformation."""
    
    def __init__(self, name: str, transform_func: Callable):
        self.name = name
        self.transform_func = transform_func
    
    def apply(self, product: Product) -> str:
        """Apply transformation to product."""
        return self.transform_func(product)


# INDIVIDUAL BLOCKS

def extract_benefits(product: Product) -> str:
    """Transform benefits into marketing copy."""
    benefits_text = ", ".join(product.benefits)
    return f"Benefits: {benefits_text}."


def extract_usage(product: Product) -> str:
    """Extract usage instructions."""
    return f"How to use: {product.how_to_use}"


def extract_warnings(product: Product) -> str:
    """Extract side effects as warnings."""
    return f"Side effects: {product.side_effects}"


def extract_ingredients(product: Product) -> str:
    """Format key ingredients."""
    ingredients_text = ", ".join(product.key_ingredients)
    return f"Key ingredients: {ingredients_text}."


def extract_concentration(product: Product) -> str:
    """Format concentration info."""
    return f"Concentration: {product.concentration}"


def extract_price(product: Product) -> str:
    """Format price."""
    return f"Price: {product.price}"


def extract_skin_type(product: Product) -> str:
    """Format skin type compatibility."""
    skin_types = ", ".join(product.skin_type)
    return f"Suitable for: {skin_types}."


# COMPARISON BLOCKS

def compare_ingredients(p1: Product, p2: Product) -> Dict:
    """Compare ingredients between products."""
    set1 = set(p1.key_ingredients)
    set2 = set(p2.key_ingredients)
    
    return {
        "product1_name": p1.name,
        "product1_ingredients": p1.key_ingredients,
        "product2_name": p2.name,
        "product2_ingredients": p2.key_ingredients,
        "shared": list(set1 & set2),
        "unique_to_product1": list(set1 - set2),
        "unique_to_product2": list(set2 - set1),
    }


def compare_benefits(p1: Product, p2: Product) -> Dict:
    """Compare benefits between products."""
    set1 = set(p1.benefits)
    set2 = set(p2.benefits)
    
    return {
        "product1_name": p1.name,
        "product1_benefits": p1.benefits,
        "product2_name": p2.name,
        "product2_benefits": p2.benefits,
        "shared_benefits": list(set1 & set2),
    }


def compare_prices(p1: Product, p2: Product) -> Dict:
    """Compare price positioning."""
    return {
        "product1": {"name": p1.name, "price": p1.price},
        "product2": {"name": p2.name, "price": p2.price},
    }


# REGISTRY

BLOCKS_REGISTRY = {
    "benefits": LogicBlock("benefits", extract_benefits),
    "usage": LogicBlock("usage", extract_usage),
    "warnings": LogicBlock("warnings", extract_warnings),
    "ingredients": LogicBlock("ingredients", extract_ingredients),
    "concentration": LogicBlock("concentration", extract_concentration),
    "price": LogicBlock("price", extract_price),
    "skin_type": LogicBlock("skin_type", extract_skin_type),
}


def get_block(name: str) -> LogicBlock:
    """Retrieve block by name."""
    if name not in BLOCKS_REGISTRY:
        raise ValueError(f"Block '{name}' not found")
    return BLOCKS_REGISTRY[name]
