import time
import enum
from rpp import extension, Presence, Runtime, Tab


class Query(enum.Enum):
    VIDEO_STREAM = 'Array.from(document.querySelectorAll(".video-stream")).find(element => element.duration)'
    VIDEO_TITLE = 'document.querySelector("#title > h1 > yt-formatted-string")'
    SHORT_AUTHOR = 'document.querySelectorAll("#channel-info #channel-name a")[document.querySelectorAll("#channel-info #channel-name a").length - 1]'


@extension
class Youtube(Presence):

    def __init__(self):
        super().__init__(metadataFile=True)
        self.tab = None
        self.thumbnail = "https://i.ytimg.com/vi/{videoId}/hqdefault.jpg"
        self.logo = "https://cdn3.iconfinder.com/data/icons/social-network-30/512/social-06-1024.png"

    def extractYoutubeTabs(self, tabs: list[Tab]) -> list[Tab]:
        return [
            tab
            for tab in tabs
            if "www.youtube.com" in tab.url
            or "www.youtube.com/watch" in tab.url
            or "www.youtube.com/shorts" in tab.url
        ]

    def extractVideoTitle(self) -> str:
        element = self.tab.execute(Query.VIDEO_TITLE.value)
        if not element.objectId:
            self.log.debug("Could not find title")
            return "Unknown"
        return self.tab.getProperties(element.objectId).textContent.value

    def extractVideoId(self) -> str:
        if "v=" in self.tab.url:
            videoId = self.tab.url.split("v=")[1]
            return videoId.split("&")[0] if "&" in videoId else videoId
        return "Unknown"

    def extractShortId(self) -> str:
        return self.tab.url.split("/shorts/")[1]

    def extractVideoAuthor(self) -> str:
        element = self.tab.execute('document.querySelector("#owner #text")')
        if not element.objectId:
            self.log.debug("Could not find author")
            return "Unknown"
        return self.tab.getProperties(element.objectId).textContent.value

    def extractVideoAuthorUrl(self) -> str:
        element = self.tab.execute('document.querySelector("#owner #text > a")')
        if not element.objectId:
            self.log.debug("Could not find author url")
            return "https://www.youtube.com"
        props = self.tab.getProperties(element.objectId)
        return props.href.value

    def extractVideoDuration(self) -> int:
        element = self.tab.execute(Query.VIDEO_STREAM.value)
        if not element.objectId:
            self.log.debug("Could not find duration")
            return 0
        return self.tab.getProperties(element.objectId).duration.value

    def extractVideoCurrentTime(self) -> int:
        element = self.tab.execute(Query.VIDEO_STREAM.value)
        if not element.objectId:
            self.log.debug("Could not find current time")
            return 0
        return self.tab.getProperties(element.objectId).currentTime.value

    def extractThumbnail(self, videoId: str) -> str:
        return self.thumbnail.format(videoId=videoId)

    def extractVideoPlayback(self) -> str:
        element = self.tab.execute("navigator.mediaSession")
        if not element.objectId:
            self.log.debug("Could not find playback state")
            return "unknown"
        props = self.tab.getProperties(element.objectId)
        return props.playbackState.value

    def extractShortAuthor(self) -> str:
        element = self.tab.execute(Query.SHORT_AUTHOR.value)
        if not element.objectId:
            self.log.debug("Could not find author")
            return "Unknown"
        return self.tab.getProperties(element.objectId).textContent.value

    def handleShort(self):
        shortId = self.extractShortId()
        shortThumbnail = self.extractThumbnail(shortId)
        shortAuthor = self.extractShortAuthor()
        shortAuthorUrl = "https://www.youtube.com/" + shortAuthor

        self.state = "Watching YouTube Short"
        self.details = "By " + shortAuthor
        self.large_image = shortThumbnail

        self.buttons = [
            {
                "label": "Watch Short",
                "url": self.tab.url,
            },
            {
                "label": "Author",
                "url": shortAuthorUrl,
            },
        ]
        self.log.info(f"Updating short: {shortId}, url: {self.tab.url}")

    def calculeTime(self, duration: int, currentTime: int) -> tuple[int, int]:
        startTime = time.time() - int(currentTime)
        endTime = startTime + int(duration)
        return int(startTime), int(endTime)

    def handleVideo(self):

        videoId = self.extractVideoId()
        videoTitle = self.extractVideoTitle()
        videoAuthor = self.extractVideoAuthor()
        videoAuthorUrl = self.extractVideoAuthorUrl()
        videoThumbnail = self.extractThumbnail(videoId)
        videoDuration = self.extractVideoDuration()
        videoCurrentTime = self.extractVideoCurrentTime()
        videoPlayback = self.extractVideoPlayback()

        startTime, endTime = self.calculeTime(videoDuration, videoCurrentTime)

        self.start = int(startTime)
        self.end = int(endTime)

        self.small_text = "Playing" if videoPlayback == "playing" else "Paused"
        self.small_image = "play" if videoPlayback == "playing" else "pause"

        self.details = "By " + videoAuthor
        self.state = videoTitle
        self.large_image = videoThumbnail

        self.buttons = [
            {
                "label": "Watch on YouTube",
                "url": self.tab.url,
            },
            {
                "label": "Author",
                "url": videoAuthorUrl,
            },
        ]
        self.log.info(f"Updating video: {videoTitle}, url: {self.tab.url}")

    def handleTab(self, lastTab: Tab):
        pass

    def handleBrowsing(self):
        self.state = "Browsing..."
        self.details = "Idle"
        self.large_image = self.logo

    def on_load(self):
        self.state = "Watching YouTube"
        self.details = "Idle"
        self.large_image = self.logo
        self.log.info("Started successfully")

    def on_update(self, runtime: Runtime):

        tabs = runtime.tabs()
        tabs = self.extractYoutubeTabs(runtime.tabs())

        if not tabs:
            self.log.info("No YouTube tabs found")
            return

        lastTab = tabs[0]
        if self.tab is None:
            self.tab = lastTab
            self.log.info("Setted initial tab")

        elif self.tab.url != lastTab.url:
            self.tab = lastTab
            self.log.info("New tab detected")

        else:
            self.log.debug("Tab did not change, updating time")
            videoDuration = self.extractVideoDuration()
            videoCurrentTime = self.extractVideoCurrentTime()
            startTime, endTime = self.calculeTime(videoDuration, videoCurrentTime)
            self.start = int(startTime)
            self.end = int(endTime)
            return

        self.tab.connect()

        if "/shorts/" in self.tab.url:
            self.handleShort()
        elif "/watch?" in self.tab.url:
            self.handleVideo()
        else:
            self.handleBrowsing()

    def on_close(self):
        self.log.info("Closed")
