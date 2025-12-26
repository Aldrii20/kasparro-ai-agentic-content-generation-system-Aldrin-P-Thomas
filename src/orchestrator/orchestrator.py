import json
import os
from typing import Dict, Any, List
from src.agents.base_agent import BaseAgent
from src.models.product_model import Product


class Orchestrator:
    """Coordinates multi-agent execution."""
    
    def __init__(self, name: str = "Orchestrator"):
        self.name = name
        self.agents: List[BaseAgent] = []
        self.results: Dict[str, Any] = {}
        self.execution_log: List[Dict] = []
    
    def register_agent(self, agent: BaseAgent) -> None:
        """Register an agent for execution."""
        self.agents.append(agent)
    
    def execute_sequential(self, input_data: Product) -> Dict:
        """Execute agents one by one."""
        for agent in self.agents:
            result = agent.run(input_data)
            self.results[agent.name] = result
            self.execution_log.append(agent.get_status())
        
        return self.results
    
    def save_results(self, output_dir: str = "output") -> None:
        """Save results to JSON files."""
        os.makedirs(output_dir, exist_ok=True)
        
        for agent_name, result in self.results.items():
            if result is not None:
                filename = f"{output_dir}/{agent_name.lower().replace(' ', '')}.json"
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(result, f, indent=2, ensure_ascii=False)
                print(f" Saved: {filename}")
    
    def get_execution_log(self) -> List[Dict]:
        """Get execution log."""
        return self.execution_log
