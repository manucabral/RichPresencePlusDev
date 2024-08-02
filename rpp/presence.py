from abc import ABC, abstractmethod


class Presence(ABC):
    """
    Abstract class for presence extensions.
    """

    def __init__(self):
        self.name = None
        self.version = "1.0.0"
        self.web = False
        self.clientId = None
        self.title = None
        self.details = None
        self.state = None
        self.large_image = None
        self.small_image = None
        self.small_text = "Rich Presence Plus"
        self.buttons = None
        self.start = None
        self.end = None
        self.log = None

    @abstractmethod
    def on_load(self) -> None:
        """
        Called once when the presence is loaded.

        Returns:
            None
        """
        pass

    @abstractmethod
    def on_update(self, **context) -> None:
        """
        Called every second to update the presence.

        Args:
            **context: The context of the presence.

        Context:
            runtime (Runtime): The runtime instance for interaction with the browser.

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
    def force_update(self):
        """
        Forces an update on the presence.
        Only updates if the time elapsed is greater than 15 seconds.

        Returns:
            None
        """
        pass


def extension(cls: Presence):
    """
    Decorator to register a class new presence extension.

    Args:
        cls (Presence): The presence extension class.

    Returns:
        Presence: The presence extension class.
    """
