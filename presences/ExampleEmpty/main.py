"""
Empty presence example.
No uses runtime.
"""

import rpp


@rpp.extension
class ExampleEmpty(rpp.Presence):
    def __init__(self):
        super().__init__()
        self.client_id = "your_app_id_here"
        self.version = "1.0.0"
        self.author = "Unknown"

    def on_load(self):
        self.log.info("Loaded")

    def on_update(self, **context):
        self.log.info("Updated")

    def on_close(self):
        self.log.info("Closed")
