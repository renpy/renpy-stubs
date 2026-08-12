from _frozen_importlib import BuiltinImporter as BuiltinImporter

class PowerInfo:
    state: int
    seconds: int
    percent: int
    def __init__(self) -> None: ...

def get_power_info() -> PowerInfo: ...

POWERSTATE_CHARGED: int
POWERSTATE_CHARGING: int
POWERSTATE_NO_BATTERY: int
POWERSTATE_ON_BATTERY: int
POWERSTATE_UNKNOWN: int
