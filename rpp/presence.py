from abc import ABC, abstractmethod
from .runtime import Runtime


class Presence(ABC):
    """
    Abstract class for a presence extension.
    """

    name = None
    version = "1.0.0"
    usingWeb = False
    clientId = None
    title = None
    details = None
    state = None
    large_image = None
    large_text = None
    small_image = None
    small_text = None
    start = None
    end = None

    @abstractmethod
    def on_load(self) -> None:
        """
        Called once when the presence is loaded.

        Returns:
            None
        """
        pass

    @abstractmethod
    def on_update(self, context: Runtime = None) -> None:
        """
        Called every second to update the presence.

        Args:
            context: The runtime context.

        Returns:
            None
        """
        pass

    @abstractmethod
    def on_close(self):
        """
        Called once when the presence is closed.

        Returns:
            None
        """
        pass

    @abstractmethod
    def force_update(self) -> None:
        """
        Forces an update on the presence.
        Only updates if the time elapsed is greater than 15 seconds.

        Returns:
            None
        """
        pass


def extension(cls: Presence) -> Presence:
    """
    Decorator to register a new presence extension.

    :param cls: The presence class to register.
    :return: The registered class.
    """
    pass
