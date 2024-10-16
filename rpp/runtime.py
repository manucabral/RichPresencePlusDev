from .tab import Tab


def check_connection(func):
    """
    Decorator to check if the runtime is connected before calling a method.
    """
    pass


class Runtime:
    """
    Class to interact with the browser runtime.
    """

    def __init__(self, port: int):
        """
        Initialize the runtime.
        """
        pass

    def update(self) -> None:
        """
        Update the data from the browser.
        """
        pass

    @check_connection
    def tabs(self) -> list[Tab]:
        """
        Get the tabs.

        Returns:
            list[Tab]: A list of tabs
        """
        pass

    @check_connection
    def current_tab(self) -> Tab:
        """
        Get the current tab.

        Returns:
            Tab: The current tab
        """
        pass

    @check_connection
    def filter_tabs(self, url: str) -> list[Tab]:
        """
        Filter tabs by url

        Args:
            url (str): The url to filter by

        Returns:
            list[Tab]: A list of tabs that match the url
        """
        pass
