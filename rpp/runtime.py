from .tab import Tab


def check_connection(func: callable):
    """
    Decorator to check if the runtime is connected to the browser
    """


class Runtime:
    """
    A class representing the runtime of the browser.
    It is used to interact with the browser and get information about it.
    """

    def update(self):
        """
        Update the runtime data (tabs).
        """
        pass

    @check_connection
    def tabs(self) -> list[Tab]:
        """
        Get all the tabs opened in the browser.
        """
        pass

    @check_connection
    def current_tab(self) -> Tab:
        """
        Get the current tab opened in the browser.
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
