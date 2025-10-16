import json
import os
from datetime import datetime

class MemoryAgent:
    def __init__(self, file_path="memory.json"):
        self.file_path = file_path
        self.memory = self.load_memory()

    def load_memory(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return {}
        return {}

    def save_memory(self):
        with open(self.file_path, "w") as f:
            json.dump(self.memory, f, indent=4)

    def store_insights(self, company, insights):
        insights["timestamp"] = datetime.now().isoformat()
        self.memory[company] = insights
        self.save_memory()

    def get_insights(self, company):
        return self.memory.get(company, None)
