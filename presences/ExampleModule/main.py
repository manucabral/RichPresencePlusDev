"""
A simple example using modules.
No uses runtime.
"""

import rpp
from .module1 import say_hello_module1
from .module2 import say_hello_module2


@rpp.extension
class ExampleModule(rpp.Presence):
    def __init__(self):
        super().__init__()
        self.client_id = "your_app_id_here"
        self.version = "1.0.0"
        self.author = "Unknown"

    def on_load(self):
        self.log.info("Loaded")

    def on_update(self, **context):
        self.log.info("Updated")
        say_hello_module1()
        say_hello_module2()

    def on_close(self):
        self.log.info("Closed")
