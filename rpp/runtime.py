import urllib.request
import json
from functools import wraps
from .tab import Tab


def update_data(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        self.update()
        if not self.connected:
            print("Failed to connect to the runtime")
            print(
                "Make sure the browser is running with the remote debugging port enabled"
            )
            return None
        return func(self, *args, **kwargs)

    return wrapper


class Runtime:

    def __init__(self, port: int):
        self.port = port
        self.data = []
        self.connected = False
        self.update()

    def update(self):
        try:
            with urllib.request.urlopen(
                f"http://localhost:{self.port}/json", timeout=1
            ) as url:
                data = json.loads(url.read().decode())
                if not data:
                    return []
                self.data = [Tab(**d) for d in data]
                self.connected = True
        except Exception as exc:
            self.connected = False

    @update_data
    def tabs(self) -> list[Tab]:
        return self.data

    @property
    @update_data
    def current_tab(self) -> Tab:
        return self.data[0]
