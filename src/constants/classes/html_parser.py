import requests
from bs4 import BeautifulSoup


class HtmlParser:
    def __init__(
        self,
        url,
        class_for_torrents: str,
        # class_for_torrent_name: str,
        # class_for_torrent_size: str,
        # class_for_seeders: str,
        # class_for_leechers: str,
        # class_for_magnet: str,
        # class_for_file_format: str,
        # class_for_uploader: str,
    ) -> None:
        self.url: str = url
        self.class_for_torrents: str = class_for_torrents
        # self.class_for_torrent_name: str = class_for_torrent_name
        # self.class_for_torrent_size: str = class_for_torrent_size
        # self.class_for_seeders: str = class_for_seeders
        # self.class_for_leechers: str = class_for_leechers
        # self.class_for_magnet: str = class_for_magnet
        # self.class_for_file_format: str = class_for_file_format
        # self.class_for_uploader: str = class_for_uploader

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

    def get_torrents(self) -> list:
        print("get_torrents def")
        for row in self._html_parser.find_all("div", class_=self.class_for_torrents):
            return [row]

    def get_torrent_info(self, torrent) -> dict:
        print("get_torrent_info def")


if __name__ == "__main__":
    a = HtmlParser(
        url="https://torrentgalaxy.mx/torrents.php?search=batman#results",
        class_for_torrents="tgxtablerow",
    ).get_torrent_info()
    print(a)
