from src.models.product_model import Product, COMPARISON_PRODUCT
from src.agents.faq_agent import FAQAgent
from src.agents.product_page_agent import ProductPageAgent
from src.agents.comparison_agent import ComparisonAgent
from src.orchestrator.orchestrator import Orchestrator



GLOWBOOST = Product(
    name="GlowBoost Vitamin C Serum",
    concentration="10% Vitamin C",
    skin_type=["Oily", "Combination"],
    key_ingredients=["Vitamin C", "Hyaluronic Acid"],
    benefits=["Brightening", "Fades dark spots"],
    how_to_use="Apply 2–3 drops in the morning before sunscreen",
    side_effects="Mild tingling for sensitive skin",
    price="₹699",
)


def main():
    """Main orchestration pipeline."""
    print(" Starting content generation...")
    
    
    orchestrator = Orchestrator("ContentOrchestrator")
    
    
    orchestrator.register_agent(FAQAgent("FAQAgent"))
    orchestrator.register_agent(ProductPageAgent("ProductPageAgent"))
    orchestrator.register_agent(ComparisonAgent("ComparisonAgent", COMPARISON_PRODUCT))
    
    
    orchestrator.execute_sequential(GLOWBOOST)
    
     
    orchestrator.save_results("output")
    

    print("\n Execution Summary:")
    for status in orchestrator.get_execution_log():
        print(f"  {status['agent']}: {status['status']}")
    
    print("\n Content generation complete!")


if __name__ == "__main__":
    main()
