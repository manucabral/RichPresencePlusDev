"""
Rich Presence Plus
------------------
A simple Discord Rich Presence manager for custom desktop or web status.
"""

from .presence import Presence
from .runtime import Runtime
from .extension import extension
from .rpc import ActivityType
from .tab import Tab

__title__ = "Rich Presence Plus"
__description__ = (
    "A simple Discord Rich Presence manager for custom desktop or web status."
)
__version__ = "0.0.5"
__author__ = "Manuel Cabral"
__license__ = "GPL-3.0"


__all__ = [
    "Presence",
    "Runtime",
    "extension",
    "ActivityType",
    "Tab",
]
