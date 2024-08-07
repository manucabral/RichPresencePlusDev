from abc import ABC, abstractmethod


class Presence(ABC):
    """
    Base class for creating a presence extension.
    """

    def __init__(self, metadataFile: bool = False):
        self.name = None
        self.author = "Unknown"
        self.version = "1.0.0"
        self.web = False
        self.enabled = True
        self.updateInterval = 3
        self.metadataFile = metadataFile
        self.devMode = False
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
        Called when the extension is loaded.
        """
        pass

    @abstractmethod
    def on_update(self, **context) -> None:
        """
        Called when the presence is updated.
        """
        pass

    @abstractmethod
    def on_close(self):
        """
        Called when the extension is closed.
        """
        pass

    @abstractmethod
    def force_update(self):
        """
        Forces an update to the presence.
        """
        pass


def extension(cls: Presence):
    """
    Decorator to register an new extension.
    """
    pass
