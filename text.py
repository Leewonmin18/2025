import streamlit as st
import random

st.set_page_config(page_title="🌏 여행지 & 플레이리스트 추천 앱", layout="wide")
st.title("🌏 여행지 & 플레이리스트 추천 앱 (폴더 없이 실행 가능)")

# --- 여행지 데이터 (각 도시마다 다른 이미지 + 샘플 mp3) ---
travel_data = {
    "유럽": {
        "프랑스": {
            "파리": {
                "image": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?auto=format&fit=crop&w=800&q=60",
                "description": "로맨틱한 도시",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"]
            },
            "니스": {
                "image": "https://images.unsplash.com/photo-1493558103817-58b2924bce98?auto=format&fit=crop&w=800&q=60",
                "description": "지중해 휴양지",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3"]
            }
        },
        "이탈리아": {
            "로마": {
                "image": "https://images.unsplash.com/photo-1526481280690-1741a8c6f64d?auto=format&fit=crop&w=800&q=60",
                "description": "역사와 문화의 중심",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"]
            },
            "베네치아": {
                "image": "https://images.unsplash.com/photo-1508923567004-3a6b8004f3d9?auto=format&fit=crop&w=800&q=60",
                "description": "운하의 도시",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3"]
            }
        },
        "스페인": {
            "바르셀로나": {
                "image": "https://images.unsplash.com/photo-1505678261036-a3fcc5e884ee?auto=format&fit=crop&w=800&q=60",
                "description": "가우디 건축과 해변",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3"]
            },
            "마드리드": {
                "image": "https://images.unsplash.com/photo-1501594907352-04cda38ebc29?auto=format&fit=crop&w=800&q=60",
                "description": "역사와 현대가 공존",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3"]
            }
        }
    },
    "아메리카": {
        "미국": {
            "뉴욕": {
                "image": "https://images.unsplash.com/photo-1549921296-3a7cde44b41e?auto=format&fit=crop&w=800&q=60",
                "description": "활기찬 대도시",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-7.mp3"]
            },
            "로스앤젤레스": {
                "image": "https://images.unsplash.com/photo-1490578474895-699cd4e2cf59?auto=format&fit=crop&w=800&q=60",
                "description": "해변과 영화 도시",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3"]
            }
        },
        "캐나다": {
            "토론토": {
                "image": "https://images.unsplash.com/photo-1508923567004-3a6b8004f3d9?auto=format&fit=crop&w=800&q=60",
                "description": "다문화 도시",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-9.mp3"]
            },
            "밴쿠버": {
                "image": "https://images.unsplash.com/photo-1519985176271-adb1088fa94c?auto=format&fit=crop&w=800&q=60",
                "description": "자연과 도시의 조화",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-10.mp3"]
            }
        },
        "브라질": {
            "리우데자네이루": {
                "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=800&q=60",
                "description": "열정적인 축제와 해변",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-11.mp3"]
            },
            "상파울루": {
                "image": "https://images.unsplash.com/photo-1526481280690-1741a8c6f64d?auto=format&fit=crop&w=800&q=60",
                "description": "대도시 문화 중심",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-12.mp3"]
            }
        }
    },
    "아시아": {
        "일본": {
            "도쿄": {
                "image": "https://images.unsplash.com/photo-1505678261036-a3fcc5e884ee?auto=format&fit=crop&w=800&q=60",
                "description": "활기찬 도시",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-13.mp3"]
            },
            "교토": {
                "image": "https://images.unsplash.com/photo-1501594907352-04cda38ebc29?auto=format&fit=crop&w=800&q=60",
                "description": "전통과 문화",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-14.mp3"]
            }
        },
        "태국": {
            "방콕": {
                "image": "https://images.unsplash.com/photo-1516515429574-0b05343b94e8?auto=format&fit=crop&w=800&q=60",
                "description": "화려한 도시",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-15.mp3"]
            },
            "푸켓": {
                "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=800&q=60",
                "description": "아름다운 해변 휴양지",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-16.mp3"]
            }
        }
    },
    "아프리카": {
        "남아프리카공화국": {
            "케이프타운": {
                "image": "https://images.unsplash.com/photo-1519985176271-adb1088fa94c?auto=format&fit=crop&w=800&q=60",
                "description": "아름다운 자연과 해변",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-19.mp3"]
            },
            "요하네스버그": {
                "image": "https://images.unsplash.com/photo-1505678261036-a3fcc5e884ee?auto=format&fit=crop&w=800&q=60",
                "description": "활기찬 도시",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-20.mp3"]
            }
        },
        "모로코": {
            "마라케시": {
                "image": "https://images.unsplash.com/photo-1501594907352-04cda38ebc29?auto=format&fit=crop&w=800&q=60",
                "description": "전통시장과 문화",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-21.mp3"]
            },
            "카사블랑카": {
                "image": "https://images.unsplash.com/photo-1505678261036-a3fcc5e884ee?auto=format&fit=crop&w=800&q=60",
                "description": "역사와 현대가 공존하는 도시",
                "playlist": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-22.mp3"]
            }
        }
    }
}

# --- 사이드바: 대륙 선택 ---
continent = st.sidebar.selectbox("대륙을 선택하세요", list(travel_data.keys()))

# --- 랜덤 추천 버튼 ---
if st.sidebar.button("랜덤 여행지 추천"):
    country = random.choice(list(travel_data[continent].keys()))
    city = random.choice(list(travel_data[continent][country].keys()))
    city_info = travel_data[continent][country][city]
    st.success(f"추천 여행지: {city} ({country})")
else:
    # --- 나라 선택 ---
    country_list = list(travel_data[continent].keys())
    country = st.selectbox("나라를 선택하세요", country_list)

    # --- 도시 선택 ---
    city_list = list(travel_data[continent][country].keys())
    city = st.selectbox("여행지를 선택하세요", city_list)

    # --- 여행지 정보 ---
    city_info = travel_data[continent][country][city]

# --- 여행지 정보 표시 ---
st.subheader(f"{city} 🌍")
st.write(city_info["description"])

# 이미지와 플레이리스트 컬럼 배치
col1, col2 = st.columns([2, 1])
with col1:
    st.image(city_info["image"], width=600)
with col2:
    st.write("🎵 플레이리스트")
    for idx, song_url in enumerate(city_info["playlist"], start=1):
        st.audio(song_url, format="audio/mp3")
