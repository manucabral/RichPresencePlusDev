"""
A simple example of a presence using metadata file.
"""

import rpp


@rpp.extension
class ExampleMetadata(rpp.Presence):
    def __init__(self):
        super().__init__(metadata_file=True)
        self.web = False

    def on_load(self):
        self.log.info("Loaded")

    def on_update(self, **context):
        self.log.info("Updated")

    def on_close(self):
        self.log.info("Closed")
