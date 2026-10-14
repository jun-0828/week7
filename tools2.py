import requests
from secret import API_KEY

BASE_URL = ("https://www.kobis.or.kr/kobisopenapi/webservice/rest/"
       "boxoffice/searchDailyBoxOfficeList.json")

def get_movie_audience(date, title):
    """
    지정한 날짜의 박스오피스에서 영화 제목을 찾아 관객 수를 반환한다.

    date: YYYYMMDD 형식의 날짜 문자열
    title: 영화 제목
    반환값: '186,587명' 형태의 문자열 또는 영화가 없다는 안내 문장
    """
    params = {"key": API_KEY, "targetDt": date}
    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()
    movies = data["boxOfficeResult"]["dailyBoxOfficeList"]

    for movie in movies:
        if movie["movieNm"] == title:
            audience = int(movie["audiCnt"])
            return f"{audience:,}명"

    return f"'{title}' 은(는) {date} 순위에 없습니다."