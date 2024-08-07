class Attribute:
    """
    Attribute object.

    Args:
        name (str): The name of the attribute.
        type (str): The type of the attribute.
        value (str): The value of the attribute.
    """

    __slots__ = ("name", "type", "value")


class PropertiesResponse:
    """
    Dynamic properties response object.

    All attributes are a instance of Attribute class.
    """


class RemoteObject:
    """
    Remote object class.
    """

    __slots__ = (
        "type",
        "subtype",
        "className",
        "value",
        "unserializableValue",
        "description",
        "objectId",
    )


class Tab:
    """
    A class representing a tab in the browser.
    """

    @property
    def id(self) -> str:
        """
        Get the tab id.

        Returns:
            str: The tab id.
        """
        pass

    @property
    def url(self) -> str:
        """
        Get the tab url.

        Returns:
            str: The tab url.
        """
        pass

    @property
    def title(self) -> str:
        """
        Get the tab title.

        Returns:
            str: The tab title.
        """
        pass

    @property
    def connected(self) -> bool:
        """
        Check if the tab is connected.
        If the tab is connected, it means you can execute code in it.

        Returns:
            bool: True if connected, False otherwise.
        """
        pass

    def getProperties(self, objectId: str) -> PropertiesResponse:
        """
        Get the properties of an RemoteObject.

        Args:
            objectId (str): The RemoteObject id.

        Returns:
            PropertiesResponse: The properties of the object.
        """
        pass

    def connect(self) -> None:
        """
        Connect to the tab to execute code in it.
        """
        pass

    def close(self) -> None:
        """
        Close the tab connection.
        """
        pass

    def execute(self, code: str) -> RemoteObject:
        """
        Execute javascript code in the tab.

        Args:
            code (str): The code to execute.

        Returns:
            RemoteObject: The result of the execution.
        """
        pass
