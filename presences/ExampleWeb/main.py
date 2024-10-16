"""
A simple example of a web presence.
Uses runtime (browser connection required).
"""

import rpp


@rpp.extension
class ExampleWeb(rpp.Presence):
    def __init__(self):
        super().__init__()
        self.client_id = "your_app_id_here"
        self.version = "1.0.0"
        self.author = "Unknown"
        self.web = True

    def on_load(self):
        self.log.info("Loaded")

    def on_update(self, runtime: rpp.Runtime):
        tabs = runtime.tabs()
        self.log.info(f"Tabs: {len(tabs)}")

    def on_close(self):
        self.log.info("Closed")
