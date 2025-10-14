"""
memory_agent.py
Stores and retrieves past insights to maintain continuity.
Handles corrupted or missing JSON files gracefully.
"""

import json
import os

class MemoryAgent:
    def __init__(self, memory_file="research_memory.json"):
        self.memory_file = memory_file
        self.memory = self.load_memory()

    def load_memory(self):
        """Load memory from JSON file, or return empty dict if file is missing/corrupted"""
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, "r") as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print(f"Warning: {self.memory_file} is corrupted. Starting with empty memory.")
                return {}
        return {}

    def save_memory(self):
        """Save memory to JSON file safely"""
        try:
            with open(self.memory_file, "w") as f:
                json.dump(self.memory, f, indent=4)
        except TypeError as e:
            print(f"Error saving memory: {e}")

    def store_insights(self, company, insights):
        """Store insights for a company"""
        self.memory[company] = insights
        self.save_memory()

    def retrieve_insights(self, company):
        """Retrieve insights for a company"""
        return self.memory.get(company, None)


# Example usage
if __name__ == "__main__":
    memory = MemoryAgent()
    memory.store_insights("AAPL", {"summary": "Positive trend"})
    print(memory.retrieve_insights("AAPL"))
