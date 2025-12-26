from typing import Dict
from src.agents.base_agent import BaseAgent
from src.agents.question_generator_agent import QuestionGeneratorAgent
from src.logic_blocks.blocks_registry import get_block
from src.models.product_model import Product


class FAQAgent(BaseAgent):
    """Generates FAQ pages with Q&A pairs."""
    
    def validate_input(self, input_data) -> bool:
        return isinstance(input_data, Product)
    
    def execute(self, product: Product) -> Dict:
        """Generate FAQ page structure."""
        
        question_gen = QuestionGeneratorAgent("QuestionGen")
        questions = question_gen.run(product)
        
        faq_data = {
            "page_title": f"{product.name} - FAQ",
            "product_name": product.name,
            "faqs": [],
        }
        
        
        for q_item in questions:
            category = q_item["category"]
            question = q_item["question"]
            
            if category == "Informational":
                answer = get_block("concentration").apply(product)
            elif category == "Usage":
                answer = get_block("usage").apply(product)
            elif category == "Safety":
                answer = get_block("warnings").apply(product)
            elif category == "Purchase":
                answer = get_block("price").apply(product)
            else:
                answer = get_block("benefits").apply(product)
            
            faq_data["faqs"].append({
                "category": category,
                "question": question,
                "answer": answer,
            })
        
        return faq_data
