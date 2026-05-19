from typing import List, Dict, Any, TypedDict, Annotated
import operator

class EmergencyState(TypedDict):
    # Core User Context
    user_id: str
    raw_incident_report: str
    
    # Unified append-only execution log track
    messages: Annotated[List[Dict[str, Any]], operator.add]
    
    # Enriched contextual metadata
    current_location: Dict[str, Any]
    weather_conditions: Dict[str, Any]
    nearest_hospitals: List[Dict[str, Any]]
    
    # Infrastructure & Safety tracking gates
    alert_payload: Dict[str, Any]
    human_approved: bool
    session_token_count: int
    execution_depth: int
    next_step: str