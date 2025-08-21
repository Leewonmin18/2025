import streamlit as st
import difflib

# --------------------------
# 데이터베이스 (확장)
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
    },
    "신문지": {
        "category": "종이",
        "icon": "📰",
        "recyclable": "✅ 재활용 가능",
        "guide": "끈이나 스테이플러 제거 후 묶어서 배출",
        "warning": "⚠️ 음식물이 묻은 신문지는 재활용 불가",
        "image": "https://cdn-icons-png.flaticon.com/512/1047/1047717.png"
    },
    "커피컵": {
        "category": "플라스틱/종이 혼합",
        "icon": "☕",
        "recyclable": "♻️ 일부 재활용 가능",
        "guide": "뚜껑 제거 후 컵은 일반쓰레기, 플라스틱 뚜껑은 재활용 가능",
        "warning": "⚠️ 컵 안에 내용물이 남아 있으면 재활용 불가",
        "image": "https://cdn-icons-png.flaticon.com/512/1047/1047720.png"
    },
    "전자제품": {
        "category": "전자/금속",
        "icon": "💻",
        "recyclable": "♻️ 재활용 가능",
        "guide": "전자제품 전용 수거함이나 판매점에 반납",
        "warning": "⚠️ 배터리 제거 후 반납",
        "image": "https://cdn-icons-png.flaticon.com/512/1047/1047725.png"
    },
    "휴지": {
        "category": "종이",
        "icon": "🧻",
        "recyclable": "❌ 재활용 불가",
        "guide": "일반쓰레기로 배출",
        "warning": "⚠️ 음식물이나 물기가 묻으면 재활용 불가",
        "image": "https://cdn-icons-png.flaticon.com/512/1047/1047740.png"
    }
}

# --------------------------
# Streamlit UI
# --------------------------
st.set_page_config(page_title="분리수거 가이드", page_icon="♻️", layout="centered")
st.title("♻️ 분리수거 가이드 앱")
st.write("🔍 분리수거 방법을 알고 싶은 품목을 검색하거나 선택하세요!")

# --------------------------
# 검색 기능
# --------------------------
query = st.text_input("품목 이름을 입력하세요")

# 유사 매칭
matched_items = []
if query:
    matched_items = difflib.get_close_matches(query, recycle_guide.keys(), n=10, cutoff=0.3)
else:
    matched_items = list(recycle_guide.keys())

# --------------------------
# 여러 품목 선택
# --------------------------
selected_items = st.multiselect(
    "품목을 선택하세요",
    options=matched_items
)

# --------------------------
# 결과 출력 (카드형 UI)
# --------------------------
for item in selected_items:
    data = recycle_guide[item]
    st.markdown("---")  # 구분선

    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(data["image"], width=100)
    with col2:
        st.subheader(f"{data['icon']} {item}")
        st.markdown(f"**📂 분류**: {data['category']}")
        st.markdown(f"**♻️ 재활용 여부**: {data['recyclable']}")
        st.success(f"📌 방법: {data['guide']}")
        st.warning(f"{data['warning']}")

