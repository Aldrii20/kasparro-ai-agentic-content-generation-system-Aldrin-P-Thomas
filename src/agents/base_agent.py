from abc import ABC, abstractmethod
from typing import Any, Dict
from enum import Enum


class AgentStatus(Enum):
    """Status of agent execution."""
    IDLE = "idle"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


class BaseAgent(ABC):
    """Abstract base class for all agents."""
    
    def __init__(self, name: str):
        self.name = name
        self.status = AgentStatus.IDLE
        self.input_data = None
        self.output_data = None
        self.error = None
    
    @abstractmethod
    def validate_input(self, input_data: Any) -> bool:
        """Validate input before execution."""
        pass
    
    @abstractmethod
    def execute(self, input_data: Any) -> Any:
        """Execute agent logic."""
        pass
    
    def run(self, input_data: Any) -> Any:
        """Run agent with error handling."""
        self.status = AgentStatus.RUNNING
        self.input_data = input_data
        
        try:
            if not self.validate_input(input_data):
                self.status = AgentStatus.FAILED
                self.error = f"Validation failed for {self.name}"
                return None
            
            self.output_data = self.execute(input_data)
            self.status = AgentStatus.COMPLETED
            return self.output_data
        
        except Exception as e:
            self.status = AgentStatus.FAILED
            self.error = str(e)
            return None
    
    def get_status(self) -> Dict:
        """Return agent status."""
        return {
            "agent": self.name,
            "status": self.status.value,
            "error": self.error,
        }
