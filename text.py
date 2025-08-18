import streamlit as st
import random
import os

st.set_page_config(page_title="🌏 여행지 & 플레이리스트 추천 앱", layout="wide")
st.title("🌏 여행지 & 플레이리스트 추천 앱 (로컬 이미지 + 다운로드 링크)")

# --- 여행지 데이터 (모든 도시별 로컬 이미지 + 샘플 mp3 + 추천 이미지 다운로드 링크) ---
travel_data = {
    "유럽": {
        "프랑스": {
            "파리": {
                "image":"images/paris.jpg",
                "description":"로맨틱한 도시",
                "playlist":["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"],
                "download":"https://pixabay.com/photos/eiffel-tower-paris-france-landmark-2083685/"
            },
            "니스": {
                "image":"images/nice.jpg",
                "description":"지중해 휴양지",
                "playlist":["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3"],
                "download":"https://pixabay.com/photos/nice-france-city-sea-summer-3106013/"
            }
        },
        "이탈리아": {
            "로마": {
                "image":"images/rome.jpg",
                "description":"역사와 문화의 중심",
                "playlist":["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"],
                "download":"https://pixabay.com/photos/rome-colosseum-italy-landmark-2068272/"
            },
            "베네치아": {
                "image":"images/venice.jpg",
                "description":"운하의 도시",
                "playlist":["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3"],
                "download":"https://pixabay.com/photos/venice-italy-canal-city-architecture-2716905/"
            }
        },
        "스페인": {
            "바르셀로나": {
                "image":"images/barcelona.jpg",
                "description":"가우디 건축과 해변",
                "playlist":["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3"],
                "download":"https://pixabay.com/photos/barcelona-spain-city-cityscape-2326255/"
            },
            "마드리드": {
                "image":"images/madrid.jpg",
                "description":"역사와 현대가 공존",
                "playlist":["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3"],
                "download":"https://pixabay.com/photos/madrid-spain-cityscape-3081400/"
            }
        }
    },
    "아메리카": {
        "미국": {
            "뉴욕": {
                "image":"images/newyork.jpg",
                "description":"활기찬 대도시",
                "playlist":["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-7.mp3"],
                "download":"https://pixabay.com/photos/new-york-city-cityscape-usa-1845531/"
            },
            "로스앤젤레스": {
                "image":"images/losangeles.jpg",
                "description":"해변과 영화 도시",
                "playlist":["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3"],
                "download":"https://pixabay.com/photos/los-angeles-skyline-california-4705210/"
            }
        },
        "캐나다": {
            "토론토": {
                "image":"images/toronto.jpg",
                "description":"다문화 도시",
                "playlist":["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-9.mp3"],
                "download":"https://pixabay.com/photos/toronto-canada-city-cityscape-2046460/"
            },
            "밴쿠버": {
                "image":"images/vancouver.jpg",
                "description":"자연과 도시의 조화",
                "playlist":["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-10.mp3"],
                "download":"https://pixabay.com/photos/vancouver-canada-cityscape-1725752/"
            }
        },
        "브라질": {
            "리우데자네이루": {
                "image":"images/riodejaneiro.jpg",
                "description":"열정적인 축제와 해변",
                "playlist":["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-11.mp3"],
                "download":"https://pixabay.com/photos/rio-de-janeiro-brazil-cityscape-2150585/"
            },
            "상파울루": {
                "image":"images/saopaulo.jpg",
                "description":"대도시 문화 중심",
                "playlist":["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-12.mp3"],
                "download":"https://pixabay.com/photos/sao-paulo-brazil-city-3323379/"
            }
        }
    },
    "아시아": {
        "일본": {
            "도쿄": {
                "image":"images/tokyo.jpg",
                "description":"활기찬 도시",
                "playlist":["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-13.mp3"],
                "download":"https://pixabay.com/photos/tokyo-japan-city-skyline-3447601/"
            },
            "교토": {
                "image":"images/kyoto.jpg",
                "description":"전통과 문화",
                "playlist":["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-14.mp3"],
                "download":"https://pixabay.com/photos/kyoto-japan-temple-travel-2081572/"
            }
        },
        "태국": {
            "방콕": {
                "image":"images/bangkok.jpg",
                "description":"화려한 도시",
                "playlist":["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-15.mp3"],
                "download":"https://pixabay.com/photos/bangkok-thailand-city-bridge-1751291/"
            },
            "푸켓": {
                "image":"images/phuket.jpg",
                "description":"아름다운 해변 휴양지",
                "playlist":["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-16.mp3"],
                "download":"https://pixabay.com/photos/phuket-thailand-beach-sea-ocean-2408231/"
            }
        },
        "베트남": {
            "하노이": {
                "image":"images/hanoi.jpg",
                "description":"전통과 현대가 공존하는 도시",
                "playlist":["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-17.mp3"],
                "download":"https://pixabay.com/photos/hanoi-vietnam-city-building-2027713/"
            },
            "호치민": {
                "image":"images/hochiminh.jpg",
                "description":"활기찬 경제 중심지",
                "playlist":["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-18.mp3"],
                "download":"https://pixabay.com/photos/hochiminh-vietnam-city-urban-2465834/"
            }
        }
    },
    "아프리카": {
        "남아프리카공화국": {
            "케이프타운": {
                "image":"images/capetown.jpg",
                "description":"아름다운 자연과 해변",
                "playlist":["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-19.mp3"],
                "download":"https://pixabay.com/photos/cape-town-south-africa-cityscape-2103786/"
            },
            "요하네스버그": {
                "image":"images/johannesburg.jpg",
                "description":"활기찬 도시",
                "playlist":["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-20.mp3"],
                "download":"https://pixabay.com/photos/johannesburg-skyline-cityscape-2344523/"
            }
        },
        "모로코": {
            "마라케시": {
                "image":"images/marrakech.jpg",
                "description":"전통시장과 문화",
                "playlist":["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-21.mp3"],
                "download":"https://pixabay.com/photos/marrakesh-morocco-market-architecture-2110070/"
            },
            "카사블랑카": {
                "image":"images/casablanca.jpg",
                "description":"역사와 현대가 공존하는 도시",
                "playlist":["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-22.mp3"],
                "download":"https://pixabay.com/photos/casablanca-morocco-city-architecture-2103802/"
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
    if os.path.exists(city_info["image"]):
        st.image(city_info["image"], width=600)
    else:
        st.warning(f"이미지가 존재하지 않습니다. 아래 링크에서 다운로드 후 images 폴더에 넣어주세요:\n{city_info['download']}")
with col2:
    st.write("🎵 플레이리스트")
    for idx, song_url in enumerate(city_info["playlist"], start=1):
        st.audio(song_url, format="audio/mp3")
