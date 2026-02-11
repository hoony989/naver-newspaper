import json
import os
from ultrawork_skeleton.plan import PlanManager

def test_plan_manager_persistence(tmp_path, monkeypatch):
    # Point to a temp directory for state.json
    temp_dir = tmp_path
    state_file = temp_dir / "naver-state.json"
    pm = PlanManager()
    pm.state_path = str(state_file)
    pm.add_plan("demo", "demo plan", [{"wave": 2}])
    assert state_file.exists()
    data = json.loads(state_file.read_text())
    assert "plans" in data and "demo" in data["plans"]
