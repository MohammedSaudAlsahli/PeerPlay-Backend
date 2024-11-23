from typing import Any, Dict, Optional

from pydantic import BaseModel
from torrents import TORRENT_WEBSITES


class HtmlElement(BaseModel):
    tag: str
    class_: Optional[str] = (
        None  # Use 'class_' to avoid conflict with the reserved keyword 'class'
    )
    color: Optional[str] = None


class SupportedCategories(BaseModel):
    ALL: str
    ANIME: str
    BOOKS: str
    GAMES: str
    MOVIES: str
    MUSIC: str
    PICTURES: str
    SOFTWARE: str
    TV: str


class HtmlParser(BaseModel):
    TORRENTS: HtmlElement
    SIZE: HtmlElement
    NAME: HtmlElement
    SEEDERS: HtmlElement
    LEECHERS: HtmlElement
    MAGNET: HtmlElement
    FORMAT: Optional[HtmlElement] = None
    UPLOADER: Optional[HtmlElement] = None
    LANGUAGE: Optional[HtmlElement] = None


class TorrentWebsite(BaseModel):
    NAME: str
    BASE_URL: str
    SEARCH: str
    SUPPORTED_CATEGORIES: SupportedCategories
    HTML_PARSER: HtmlParser


class TorrentWebsites(BaseModel):
    __root__: Dict[str, TorrentWebsite]  # Allows for a dictionary of websites


if __name__ == "__main__":

    torrent_websites = TorrentWebsites(**TORRENT_WEBSITES)
    print(torrent_websites.__root__["TORRENT_GALAXY"].SUPPORTED_CATEGORIES.ANIME)
