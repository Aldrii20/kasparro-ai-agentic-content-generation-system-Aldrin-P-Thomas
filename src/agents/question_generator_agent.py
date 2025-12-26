from typing import List, Dict
from src.agents.base_agent import BaseAgent
from src.models.product_model import Product


class QuestionGeneratorAgent(BaseAgent):
    """Generates categorized questions for products."""
    
    QUESTION_TEMPLATES = {
        "Informational": [
            "What is the {ingredient} concentration in {product}?",
            "What are the key ingredients in {product}?",
            "What are the main benefits of {product}?",
            "What is the price of {product}?",
        ],
        "Usage": [
            "How should I apply {product}?",
            "When should I use {product}?",
            "How many drops of {product} should I use?",
            "Can {product} be used with other products?",
        ],
        "Safety": [
            "Is {product} safe for sensitive skin?",
            "What are the side effects of {product}?",
            "Are there any warnings for {product}?",
            "Will {product} cause allergies?",
        ],
        "Purchase": [
            "Where can I buy {product}?",
            "Is {product} worth the price?",
            "Does {product} have a guarantee?",
            "What is the shelf life of {product}?",
        ],
        "Comparison": [
            "How does {product} compare to other serums?",
            "Why choose {product}?",
            "Is {product} the best option in its price range?",
        ],
    }
    
    def validate_input(self, input_data) -> bool:
        return isinstance(input_data, Product) and input_data.name
    
    def execute(self, product: Product) -> List[Dict]:
        """Generate 15+ categorized questions."""
        questions = []
        main_ingredient = product.key_ingredients if product.key_ingredients else "active"
        
        for category, templates in self.QUESTION_TEMPLATES.items():
            for template in templates:
                question = template.format(
                    product=product.name,
                    ingredient=main_ingredient,
                )
                questions.append({
                    "category": category,
                    "question": question,
                })
        
        return questions[:15]
