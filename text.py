import streamlit as st

st.set_page_config(page_title="🌏 여행지 & 플레이리스트 추천 앱", layout="wide")
st.title("🌏 여행지 & 플레이리스트 추천 앱 (폴더 없이 실행 가능)")

# --- 여행지 데이터 (URL 이미지 + 샘플 mp3) ---
travel_data = {
    "유럽": {
        "프랑스": {
            "파리": {
                "image": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34",
                "description": "로맨틱한 도시",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"]
            },
            "니스": {
                "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
                "description": "지중해 휴양지",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3"]
            }
        }
    },
    "아메리카": {
        "미국": {
            "뉴욕": {
                "image": "https://images.unsplash.com/photo-1549921296-3a7cde44b41e",
                "description": "활기찬 대도시",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"]
            },
            "로스앤젤레스": {
                "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
                "description": "해변과 영화 도시",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3"]
            }
        }
    },
    "(동남)아시아": {
        "일본": {
            "도쿄": {
                "image": "https://images.unsplash.com/photo-1505678261036-a3fcc5e884ee",
                "description": "활기찬 도시",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3"]
            },
            "교토": {
                "image": "https://images.unsplash.com/photo-1501594907352-04cda38ebc29",
                "description": "전통과 문화",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3"]
            }
        }
    },
    "아프리카": {
        "남아프리카공화국": {
            "케이프타운": {
                "image": "https://images.unsplash.com/photo-1519985176271-adb1088fa94c",
                "description": "아름다운 자연과 해변",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-7.mp3"]
            }
        }
    }
}

# --- 사이드바: 대륙 선택 ---
continent = st.sidebar.selectbox("대륙을 선택하세요", list(travel_data.keys()))

# --- 나라 선택 ---
country = st.selectbox("나라를 선택하세요", list(travel_data[continent].keys()))

# --- 도시 선택 ---
city = st.selectbox("여행지를 선택하세요", list(travel_data[continent][country].keys()))

# --- 여행지 정보 ---
city_info = travel_data[continent][country][city]

st.subheader(f"{city} 🌍")
st.write(city_info["description"])

# 이미지 표시 (URL)
st.image(city_info["image"], use_column_width=True)

# --- 여행지별 플레이리스트 ---
st.write("🎵 플레이리스트")
for idx, song_url in enumerate(city_info["playlist"], start=1):
    st.audio(song_url, format="audio/mp3")
