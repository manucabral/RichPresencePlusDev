from .tab import Tab
from .logger import getLogger


def update_data(func: callable) -> callable:
    """
    Decorator to update the data of the runtime instance.

    Args:
        func (function): The function to decorate.

    Returns:
        function: The decorated function.
    """


class Runtime:
    """
    A class representing the runtime of the browser.
    It is used to interact with the browser and get information about it.
    """

    def __init__(self, port: int):
        self.port = port
        self.data = []
        self.connected = False
        self.log = getLogger("Runtime")

    def update(self) -> None:
        """
        Update the runtime data.
        """
        pass

    @update_data
    def tabs(self) -> list[Tab]:
        """
        Get the tabs of the browser.

        Returns:
            list[Tab]: The list of tabs.
        """
        return self.data

    @property
    @update_data
    def current_tab(self) -> Tab:
        """
        Get the current tab of the browser.

        Returns:
            Tab: The current tab.
        """
        return self.data[0]
