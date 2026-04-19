from pydantic import BaseModel
from typing import List

class Scenario(BaseModel):
    name: str
    type: str
    steps: List[str]
    expected_result: str

class ScenarioResponse(BaseModel):
    feature: str
    scenarios: List[Scenario]