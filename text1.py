import streamlit as st

# --------------------------
# 데이터베이스 (예시)
# --------------------------
recycle_guide = {
    "페트병": {
        "category": "플라스틱",
        "icon": "🥤",
        "recyclable": "✅ 재활용 가능",
        "guide": "라벨 제거 후 내용물 비우고 압축해서 배출",
        "warning": "⚠️ 이물질이 남아 있으면 재활용 불가",
        "image": "https://cdn-icons-png.flaticon.com/512/1047/1047711.png"
    },
    "우유팩": {
        "category": "종이",
        "icon": "🥛",
        "recyclable": "✅ 재활용 가능",
        "guide": "물로 헹군 후 펼쳐서 건조, 종이팩 전용 수거함에 배출",
        "warning": "⚠️ 일반 종이류와 섞이면 안 됨",
        "image": "https://cdn-icons-png.flaticon.com/512/1047/1047719.png"
    },
    "스티로폼": {
        "category": "플라스틱",
        "icon": "📦",
        "recyclable": "♻️ 일부 재활용 가능",
        "guide": "깨끗한 스티로폼만 재활용 가능, 오염된 것은 일반쓰레기",
        "warning": "⚠️ 음식물이나 이물질이 묻어 있으면 재활용 불가",
        "image": "https://cdn-icons-png.flaticon.com/512/1047/1047732.png"
    },
    "유리병": {
        "category": "유리",
        "icon": "🍾",
        "recyclable": "✅ 재활용 가능",
        "guide": "뚜껑 제거 후 색상별로 분리 배출",
        "warning": "⚠️ 깨진 유리는 신문지 등에 싸서 일반쓰레기로",
        "image": "https://cdn-icons-png.flaticon.com/512/1047/1047735.png"
    },
    "캔": {
        "category": "금속",
        "icon": "🥫",
        "recyclable": "✅ 재활용 가능",
        "guide": "내용물 비우고 압착해서 배출",
        "warning": "⚠️ 페인트·유해물질 캔은 별도 폐기",
        "image": "https://cdn-icons-png.flaticon.com/512/1047/1047729.png"
    },
    "비닐봉지": {
        "category": "플라스틱",
        "icon": "🛍️",
        "recyclable": "✅ 재활용 가능",
        "guide": "깨끗한 비닐만 재활용 가능, 이물질 있으면 일반쓰레기",
        "warning": "⚠️ 음식물이 묻은 비닐은 재활용 불가",
        "image": "https://cdn-icons-png.flaticon.com/512/1047/1047708.png"
    }
}

# --------------------------
# Streamlit UI
# --------------------------
st.set_page_config(page_title="분리수거 가이드", page_icon="♻️", layout="centered")

st.title("♻️ 분리수거 가이드 앱")
st.write("🔍 분리수거 방법을 알고 싶은 품목을 검색하거나 선택하세요!")

# 자동완성 (selectbox)
item = st.selectbox(
    "품목을 선택하거나 입력하세요",
    options=[""] + list(recycle_guide.keys()),  # 빈칸 + 품목 목록
    index=0
)

# 결과 출력
if item and item in recycle_guide:
    data = recycle_guide[item]

    st.subheader(f"{data['icon']} {item} 분리수거 방법")

    # 아이콘 + 이미지 출력
    st.image(data["image"], width=120)

    # 세부 정보
    st.markdown(f"**📂 분류**: {data['category']}")
    st.markdown(f"**♻️ 재활용 여부**: {data['recyclable']}")
    st.success(f"📌 방법: {data['guide']}")
    st.warning(f"{data['warning']}")
