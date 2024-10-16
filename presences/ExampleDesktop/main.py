"""
A simple example of a desktop presence.
No uses runtime (no browser connection required).
"""

import rpp


@rpp.extension
class ExampleDesktop(rpp.Presence):
    def __init__(self):
        super().__init__()
        self.client_id = "your_app_id_here"
        self.version = "1.0.0"
        self.author = "Unknown"
        self.web = False

    def on_load(self):
        self.log.info("Loaded")

    def on_update(self, **context):
        self.log.info("Updated")

    def on_close(self):
        self.log.info("Closed")
