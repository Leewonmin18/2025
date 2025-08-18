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
        },
        "이탈리아": {
            "로마": {
                "image": "https://images.unsplash.com/photo-1526481280690-1741a8c6f64d",
                "description": "역사와 문화의 중심",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"]
            },
            "베네치아": {
                "image": "https://images.unsplash.com/photo-1508923567004-3a6b8004f3d9",
                "description": "운하의 도시",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3"]
            }
        },
        "스페인": {
            "바르셀로나": {
                "image": "https://images.unsplash.com/photo-1505678261036-a3fcc5e884ee",
                "description": "가우디 건축과 해변",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3"]
            },
            "마드리드": {
                "image": "https://images.unsplash.com/photo-1504567961542-1e0a8a3a9b9c",
                "description": "역사와 현대가 공존",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3"]
            }
        }
    },
    "아메리카": {
        "미국": {
            "뉴욕": {
                "image": "https://images.unsplash.com/photo-1549921296-3a7cde44b41e",
                "description": "활기찬 대도시",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-7.mp3"]
            },
            "로스앤젤레스": {
                "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
                "description": "해변과 영화 도시",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3"]
            }
        },
        "캐나다": {
            "토론토": {
                "image": "https://images.unsplash.com/photo-1508923567004-3a6b8004f3d9",
                "description": "다문화 도시",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-9.mp3"]
            },
            "밴쿠버": {
                "image": "https://images.unsplash.com/photo-1519985176271-adb1088fa94c",
                "description": "자연과 도시의 조화",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-10.mp3"]
            }
        },
        "브라질": {
            "리우데자네이루": {
                "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
                "description": "열정적인 축제와 해변",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-11.mp3"]
            },
            "상파울루": {
                "image": "https://images.unsplash.com/photo-1526481280690-1741a8c6f64d",
                "description": "대도시 문화 중심",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-12.mp3"]
            }
        }
    },
    "아시아": {
        "일본": {
            "도쿄": {
                "image": "https://images.unsplash.com/photo-1505678261036-a3fcc5e884ee",
                "description": "활기찬 도시",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-13.mp3"]
            },
            "교토": {
                "image": "https://images.unsplash.com/photo-1501594907352-04cda38ebc29",
                "description": "전통과 문화",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-14.mp3"]
            }
        },
        "태국": {
            "방콕": {
                "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
                "description": "화려한 도시",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-15.mp3"]
            },
            "푸켓": {
                "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
                "description": "아름다운 해변 휴양지",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-16.mp3"]
            }
        },
        "베트남": {
            "하노이": {
                "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
                "description": "전통과 현대가 공존하는 도시",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-17.mp3"]
            },
            "호치민": {
                "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
                "description": "활기찬 경제 중심지",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-18.mp3"]
            }
        }
    },
    "아프리카": {
        "남아프리카공화국": {
            "케이프타운": {
                "image": "https://images.unsplash.com/photo-1519985176271-adb1088fa94c",
                "description": "아름다운 자연과 해변",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-19.mp3"]
            },
            "요하네스버그": {
                "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
                "description": "활기찬 도시",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-20.mp3"]
            }
        },
        "모로코": {
            "마라케시": {
                "image": "https://images.unsplash.com/photo-1501594907352-04cda38ebc29",
                "description": "전통시장과 문화",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-21.mp3"]
            },
            "카사블랑카": {
                "image": "https://images.unsplash.com/photo-1505678261036-a3fcc5e884ee",
                "description": "역사와 현대가 공존하는 도시",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-22.mp3"]
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
