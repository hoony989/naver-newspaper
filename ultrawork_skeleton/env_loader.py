import os
from typing import Dict, Any

from typing import Optional

class EnvLoader:
    def __init__(self, source: Optional[str] = None):
        self.source = source

    def load_env(self) -> Dict[str, Any]:
        env = dict(os.environ)
        if self.source:
            if os.path.exists(self.source):
                with open(self.source, "r") as f:
                    for line in f:
                        line = line.strip()
                        if not line or line.startswith("#") or "=" not in line:
                            continue
                        k, v = line.split("=", 1)
                        env[k.strip()] = v.strip()
        return env

    def validate_env(self, schema: Dict[str, Any]) -> bool:
        env = self.load_env()
        for k in schema.keys():
            if k not in env:
                return False
        return True
