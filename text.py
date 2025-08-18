import streamlit as st
import random

# 대륙별 여행지 데이터
travel_spots = {
    "유럽": [
        {
            "name": "파리, 프랑스",
            "desc": "낭만의 도시, 에펠탑과 루브르 박물관이 있는 여행지",
            "img": "https://upload.wikimedia.org/wikipedia/commons/a/a8/Tour_Eiffel_Wikimedia_Commons.jpg",
            "playlist": [
                ("La Vie en Rose - Édith Piaf", "https://www.youtube.com/watch?v=kFzViYkZAz4"),
                ("Sous le ciel de Paris - Yves Montand", "https://www.youtube.com/watch?v=zz6A0jZ5p5I")
            ]
        },
        {
            "name": "런던, 영국",
            "desc": "빅벤, 런던아이, 버킹엄 궁전이 있는 클래식한 도시",
            "img": "https://upload.wikimedia.org/wikipedia/commons/7/7e/London_Eye_Twilight_April_2006.jpg",
            "playlist": [
                ("London Calling - The Clash", "https://www.youtube.com/watch?v=EfK-WX2pa8c"),
                ("Waterloo Sunset - The Kinks", "https://www.youtube.com/watch?v=N_MqfF0WBsU")
            ]
        },
        {
            "name": "베를린, 독일",
            "desc": "베를린 장벽과 현대 문화가 공존하는 예술의 도시",
            "img": "https://upload.wikimedia.org/wikipedia/commons/f/f6/Berlin_Brandenburg_Gate_at_night.jpg",
            "playlist": [
                ("Heroes - David Bowie", "https://www.youtube.com/watch?v=lXgkuM2NhYI"),
                ("99 Luftballons - Nena", "https://www.youtube.com/watch?v=La4Dcd1aUcE")
            ]
        },
        {
            "name": "로마, 이탈리아",
            "desc": "콜로세움과 바티칸, 고대 로마의 중심지",
            "img": "https://upload.wikimedia.org/wikipedia/commons/5/5a/Colosseum_in_Rome%2C_Italy_-_April_2007.jpg",
            "playlist": [
                ("Arrivederci Roma - Renato Rascel", "https://www.youtube.com/watch?v=Jk9g6HgkD6U"),
                ("Volare - Domenico Modugno", "https://www.youtube.com/watch?v=t4IjJav7xbg")
            ]
        }
    ],
    "아시아": [
        {
            "name": "도쿄, 일본",
            "desc": "전통과 현대가 공존하는 도시, 도쿄 타워와 시부야 스크램블 교차로",
            "img": "https://upload.wikimedia.org/wikipedia/commons/5/50/Tokyo_Tower_and_around_Skyscrapers.jpg",
            "playlist": [
                ("Plastic Love - Mariya Takeuchi", "https://www.youtube.com/watch?v=3bNITQR4Uso"),
                ("Stay With Me - Miki Matsubara", "https://www.youtube.com/watch?v=Ns-h54fJ7Yw")
            ]
        },
        {
            "name": "방콕, 태국",
            "desc": "화려한 사원과 맛있는 길거리 음식이 가득한 도시",
            "img": "https://upload.wikimedia.org/wikipedia/commons/a/a6/Grand_Palace_Bangkok_Thailand.jpg",
            "playlist": [
                ("One Night in Bangkok - Murray Head", "https://www.youtube.com/watch?v=rgYuCg-9TTg"),
                ("Sabai Sabai - Stamp Apiwat", "https://www.youtube.com/watch?v=cmxSrlG9XJk")
            ]
        }
    ],
    "아메리카": [
        {
            "name": "뉴욕, 미국",
            "desc": "자유의 여신상과 타임스퀘어가 있는 세계적인 도시",
            "img": "https://upload.wikimedia.org/wikipedia/commons/4/47/New_york_times_square-terabass.jpg",
            "playlist": [
                ("Empire State of Mind - Alicia Keys", "https://www.youtube.com/watch?v=QsZlY0Vz4-o"),
                ("New York, New York - Frank Sinatra", "https://www.youtube.com/watch?v=le1QF9djDdc")
            ]
        },
        {
            "name": "리우데자네이루, 브라질",
            "desc": "삼바와 축구, 코파카바나 해변으로 유명한 도시",
            "img": "https://upload.wikimedia.org/wikipedia/commons/7/7c/Rio_de_Janeiro_City.jpg",
            "playlist": [
                ("The Girl from Ipanema - Astrud Gilberto", "https://www.youtube.com/watch?v=UJkxFhFRFDA"),
                ("Mas Que Nada - Sergio Mendes", "https://www.youtube.com/watch?v=BrZBiqK0p9E")
            ]
        }
    ],
    "아프리카": [
        {
            "name": "카이로, 이집트",
            "desc": "피라미드와 스핑크스로 유명한 고대 문명의 도시",
            "img": "https://upload.wikimedia.org/wikipedia/commons/e/e3/Kheops-Pyramid.jpg",
            "playlist": [
                ("Enta Omri - Umm Kulthum", "https://www.youtube.com/watch?v=TWIs5tP6Wks"),
                ("Habibi Ya Nour El Ain - Amr Diab", "https://www.youtube.com/watch?v=Z3UHfi9dXK0")
            ]
        }
    ],
    "오세아니아": [
        {
            "name": "시드니, 호주",
            "desc": "오페라 하우스와 아름다운 해변이 있는 도시",
            "img": "https://upload.wikimedia.org/wikipedia/commons/c/c6/Sydney_Opera_House_-_Dec_2008.jpg",
            "playlist": [
                ("Down Under - Men at Work", "https://www.youtube.com/watch?v=XfR9iY5y94s"),
                ("Great Southern Land - Icehouse", "https://www.youtube.com/watch?v=wmc0JGc7eyw")
            ]
        }
    ]
}

# 앱 제목
st.title("🌍 랜덤 여행지 추천 앱")
st.write("대륙을 선택한 후, 버튼을 눌러 랜덤 여행지를 추천받으세요!")

# 대륙 선택
continent = st.selectbox("대륙을 선택하세요", list(travel_spots.keys()))

# 버튼 클릭 시 랜덤 여행지 선택
if st.button("여행지 추천 받기"):
    spot = random.choice(travel_spots[continent])
    st.subheader(spot["name"])
    st.write(spot["desc"])
    st.image(spot["img"], use_container_width=True)

    st.markdown("🎶 어울리는 플레이리스트:")
    for song, url in spot["playlist"]:
        st.write(f"- [{song}]({url})")
