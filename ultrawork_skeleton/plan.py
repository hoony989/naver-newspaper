from typing import List, Dict, Any
import json
import os

class PlanManager:
    def __init__(self):
        self.plans: Dict[str, Dict[str, Any]] = {}
        self.state_path = os.path.join(os.path.dirname(__file__), "state.json")

    def _persist(self):
        try:
            with open(self.state_path, "w") as f:
                json.dump({"plans": self.plans}, f)
        except Exception:
            pass

    def save_state(self, state: Dict[str, Any]):
        with open(self.state_path, "w") as f:
            json.dump(state, f)

    def load_state(self) -> Dict[str, Any]:
        try:
            with open(self.state_path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def add_plan(self, name: str, description: str, waves: List[Dict[str, Any]]):
        self.plans[name] = {"description": description, "waves": waves}
        self._persist()
        return self.plans[name]

    def get_plan(self, name: str):
        return self.plans.get(name)

    def list_plans(self) -> List[str]:
        return list(self.plans.keys())
