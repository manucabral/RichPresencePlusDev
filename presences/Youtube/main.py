import rpp


@rpp.extension
class Youtube(rpp.Presence):

    def __init__(self):
        self.clientId = "871582048312647198"
        self.name = "Youtube"

    def on_load(self):
        print("Loaded Youtube")

    def on_update(self, context: rpp.Runtime = None):
        print("Updated Youtube")

    def on_close(self):
        print("Closed Youtube")
