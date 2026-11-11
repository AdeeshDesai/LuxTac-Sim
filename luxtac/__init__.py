"""LuxTac normal-force tactile sensor for IsaacGym / TacSL.

Deployed into isaacgymenvs/tacsl_sensors/luxtac by scripts/deploy.sh.
"""

from .luxtac_cfg import (
    LuxTacSensorCfg,
    SPRING_CFG_DEEP,
    SPRING_CFG_SHALLOW,
)

__all__ = [
    "LuxTacSensorCfg",
    "SPRING_CFG_DEEP",
    "SPRING_CFG_SHALLOW",
    "LuxTacFieldSensor",
]


def __getattr__(name):
    # Deferred so `import luxtac` works without isaacgym present (the config and
    # viz modules are pure numpy/torch and useful on their own).
    if name == "LuxTacFieldSensor":
        from .luxtac_sensor import LuxTacFieldSensor
        return LuxTacFieldSensor
    raise AttributeError(name)
