from pydantic import BaseModel, RootModel


class SupportedCategories(BaseModel):
    ALL: str | None
    ANIME: str | None
    BOOKS: str | None
    GAMES: str | None
    MOVIES: str | None
    MUSIC: str | None
    PICTURES: str | None
    SOFTWARE: str | None
    TV: str | None


class HtmlParser(BaseModel):
    TORRENTS: dict | None
    SIZE: dict | None
    NAME: dict | None
    SEEDERS: dict | None
    LEECHERS: dict | None
    MAGNET: dict | None
    FORMAT: dict | None
    UPLOADER: dict | None
    LANGUAGE: dict | None


class TorrentWebsite(BaseModel):
    NAME: str | None
    BASE_URL: str | None
    SEARCH: str | None
    SUPPORTED_CATEGORIES: SupportedCategories | None
    HTML_PARSER: HtmlParser | None


class TorrentWebsites(RootModel[dict[str, TorrentWebsite]]): ...


# if __name__ == "__main__":

#     torrent_websites = TorrentWebsites(**TORRENT_WEBSITES)
#     print(torrent_websites.root["TORRENT_GALAXY"].BASE_URL)
