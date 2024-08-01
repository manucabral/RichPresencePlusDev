class Tab:
    """
    A class representing a tab in the browser.
    """

    def __init__(self, **kwargs: dict) -> None:
        self.__id = kwargs.get("id", None)
        self.__url = kwargs.get("url", "about:blank")
        self.__title = kwargs.get("title", "Unknown")

    @property
    def id(self) -> str:
        """
        Get the id of the tab.
        """
        return self.__id

    @property
    def url(self) -> str:
        """
        Get the url of the tab.
        """
        return self.__url

    @property
    def title(self) -> str:
        """
        Get the title of the tab.
        """
        return self.__title

    def execute(self, code: str) -> str:
        """
        Execute javascript code in the tab.

        Args:
            code (str): The code to execute.

        Returns:
            str: The result of the code execution.
        """
        pass
