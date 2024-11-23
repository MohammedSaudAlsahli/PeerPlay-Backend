import requests
from bs4 import BeautifulSoup
from torrents import TORRENT_WEBSITES


class HtmlParser:
    def __init__(
        self,
        base_url,
        class_for_torrents: list,
        # search_query: str,
        # class_for_torrent_name: str,
        # class_for_torrent_size: str,
        # class_for_seeders: str,
        # class_for_leechers: str,
        # class_for_magnet: str,
        # class_for_file_format: str,
        # class_for_uploader: str,
        # class_for_language: str
    ) -> None:
        self.base_url: str = base_url
        self.class_for_torrents: list = class_for_torrents
        # self.search_query = search_query
        # self.class_for_torrent_name: str = class_for_torrent_name
        # self.class_for_torrent_size: str = class_for_torrent_size
        # self.class_for_seeders: str = class_for_seeders
        # self.class_for_leechers: str = class_for_leechers
        # self.class_for_magnet: str = class_for_magnet
        # self.class_for_file_format: str = class_for_file_format
        # self.class_for_uploader: str = class_for_uploader
        # self.class_for_language: str = class_for_language

    @property
    def _html(self) -> dict:
        print("_html def")

        response = requests.get(self.url)
        if response.status_code != 200:
            raise Exception(
                f"Failed to fetch the page. Status code: {response.status_code}"
            )
        return response.text

    @property
    def _html_parser(self) -> BeautifulSoup:
        print("_html_parser def")

        return BeautifulSoup(self._html, "html.parser")

    def _get_torrents(self) -> list:
        print("_get_torrents def")

        return self._html_parser.find_all(
            self.class_for_torrents[0],
            class_=self.class_for_torrents[1],
        )

    def get_torrent_info(self) -> dict:
        print("get_torrent_info def")

        torrents_info = []
        for torrent in self._get_torrents():
            green_font = torrent.find("font", color="green")
            torrents_info.append(
                {"green_font": green_font.text if green_font else None}
            )
        print(torrents_info)


if __name__ == "__main__":
    a = HtmlParser(
        url="https://torrentgalaxy.mx/torrents.php?search=batman#results",
        class_for_torrents="tgxtablerow",
    ).get_torrent_info()
    print(a)
