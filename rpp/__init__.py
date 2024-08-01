"""
Rich Presence Plus
------------------
A simple Discord Rich Presence manager for desktop and web apps.
"""

from .presence import Presence, extension
from .runtime import Runtime
from .tab import Tab

__title__ = "Rich Presence Plus"
__author__ = "Manuel Cabral"
__version__ = "0.0.1"
__license__ = "GPLv3"

__all__ = [
    "Presence",
    "extension",
    "Runtime",
    "Tab",
]
