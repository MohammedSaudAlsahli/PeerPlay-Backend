TORRENT_WEBSITES = {
    "TORRENT_GALAXY": {
        "NAME": "Torrentgalaxy",
        "BASE_URL": "https://torrentgalaxy.mx/",
        "SEARCH": "torrents.php?search=",
        "SUPPORTED_CATEGORIES": {
            "ALL": "",
            "ANIME": "c28=1/",
            "BOOKS": "c13=1&c19=1&c12=1&c14=1&c15=1/",
            "GAMES": "c43=1&c10=1/",
            "MOVIES": "c3=1&c46=1&c45=1&c42=1&c4=1&c1=1/",
            "MUSIC": "c22=1&c26=1&c23=1&c25=1&c24=1/",
            "PICTURES": "c37=1/",
            "SOFTWARE": "c20=1&c21=1&c18=1/",
            "TV": "c41=1&c5=1&c11=1&c6=1&c7=1/",
        },
        "HTML_PARSER": {
            "TORRENTS": {
                "tag": "div",
                "class": "tgxtablerow",
            },
            "SIZE": {
                "tag": "span",
                "class": "badge badge-secondary",
            },
            "NAME": {
                "tag": "a",
                "class": "txlight",
            },
            "SEEDERS": {
                "tag": "font",
                "color": "green",
            },
            "LEECHERS": {
                "tag": "font",
                "color": "#ff0000",
            },
            "MAGNET": {
                "tag": "a",
                "role": "button",
            },
            "FORMAT": {},
            "UPLOADER": {},
            "LANGUAGE": {},
        },
    }
}
