import rpp


@rpp.extension
class Example(rpp.Presence):

    def __init__(self):
        super().__init__()
        self.clientId = 11111111111111111
        self.name = "Example"
        self.version = "1.0.0"

    def on_load(self):
        self.log.info("Started successfully")

    def on_update(self, **kwargs):
        self.log.info("Updating")

    def on_close(self):
        self.log.info("Closed")
