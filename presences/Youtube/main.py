import rpp
import time


@rpp.extension
class Youtube(rpp.Presence):

    def __init__(self):
        super().__init__()
        self.version = "1.0.0"
        self.clientId = 1113646725408772176
        self.name = "Youtube"
        self.thumbnail = "https://i.ytimg.com/vi/{videoId}/hqdefault.jpg"

    def on_load(self):
        self.log.info("Started successfully")
        self.state = "Idle"
        self.details = "Idle"

    def filter_tabs(self, tabs):
        return [tab for tab in tabs if "youtube.com" in tab.url]

    def on_update(self, runtime: rpp.Runtime):
        tabs = runtime.tabs()
        print(tabs)
        if not tabs:
            return
        tabs = self.filter_tabs(tabs)
        if not tabs:
            return
        tab = tabs[0]
        title = tab.execute(
            "document.querySelector('#title > h1 > yt-formatted-string').textContent"
        )
        videoId = tab.url.split("v=")
        if len(videoId) < 2:
            return
        videoId = videoId[1]
        author = tab.execute('document.querySelector("#owner #text").textContent')
        authorUrl = tab.execute('document.querySelector("#owner #text > a").href')
        thumbnail = self.thumbnail.format(videoId=videoId)
        playback = tab.execute("navigator.mediaSession.playbackState")
        self.small_text = "Playing" if playback == "playing" else "Paused"
        self.small_image = "play" if playback == "playing" else "pause"
        self.state = "By " + author
        self.details = title
        self.large_image = thumbnail
        self.buttons = [
            {"label": "Watch on Youtube", "url": tab.url},
            {"label": "View Channel", "url": authorUrl},
        ]
        print(f"Updated Youtube to {title}")
        time.sleep(5)

    def on_close(self):
        self.log.info("Closed")
