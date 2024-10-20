from enum import Enum


class ActivityType(Enum):
    """
    Available activity types for the RPC.
    """

    PLAYING = 0
    LISTENING = 2
    WATCHING = 3
    COMPETING = 5
