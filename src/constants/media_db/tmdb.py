TMDB = {
    "BASE_URL": "https://api.themoviedb.org/3/",
    "IMAGE_URL": "https://image.tmdb.org/t/p/",
    "IMAGE_SIZE": {
        "POSTER": "w600_and_h900_bestv2/",
        "BACKDROP": "w1920_and_h800_multi_faces/",
    },
    "MOVIES_ENDPOINTS": {
        "POPULAR": "movie/popular?language=en-US",
        "TOP_RATED": "movie/top_rated?language=en-US",
        "DETAILS": "movie/{movie_id}?language=en-US",
        "CREDITS": "movie/{movie_id}/credits?language=en-US",
        "EXTERNAL_ID": "movie/{movie_id}/external_ids",
        "IMAGES": "movie/{movie_id}/images",
    },
}
