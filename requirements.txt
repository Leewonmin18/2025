import streamlit as st

# --------------------------
# 앱 제목
# --------------------------
st.title("♻ 분리수거 가이드 앱")

st.write("검색창에 품목 이름을 입력하면 어떤 재질로 분리해야 하는지 알려드립니다!")

# --------------------------
# 분리수거 데이터
# --------------------------
recycle_guide = {
    "페트병": {
        "category": "플라스틱",
        "icon": "🥤",
        "recyclable": "✅ 재활용 가능",
        "info": "뚜껑과 라벨을 제거한 후 배출하세요."
    },
    "유리병": {
        "category": "유리",
        "icon": "🍾",
        "recyclable": "✅ 재활용 가능",
        "info": "뚜껑을 제거하고 깨끗이 헹군 후 배출하세요."
    },
    "신문지": {
        "category": "종이",
        "icon": "📰",
        "recyclable": "✅ 재활용 가능",
        "info": "끈으로 묶거나 상자에 넣어 배출하세요."
    },
    "캔": {
        "category": "금속",
        "icon": "🥫",
        "recyclable": "✅ 재활용 가능",
        "info": "내용물을 비운 후 배출하세요."
    },
    "스티로폼": {
        "category": "플라스틱",
        "icon": "📦",
        "recyclable": "❌ 재활용 불가",
        "info": "지역 재활용 규정을 확인하세요."
    },
    "플라스틱컵": {
        "category": "플라스틱",
        "icon": "🥤",
        "recyclable": "✅ 재활용 가능",
        "info": "내용물을 비우고 깨끗이 헹군 후 배출하세요."
    },
    "종이컵": {
        "category": "종이",
        "icon": "☕",
        "recyclable": "❌ 재활용 불가",
        "info": "종이컵은 종이류로 분리수거가 불가합니다."
    }
}

# --------------------------
# 검색창
# --------------------------
item = st.text_input("🔍 품목 이름을 입력하세요:")

if item:
    item_lower = item.strip()
    if item_lower in recycle_guide:
        info = recycle_guide[item_lower]
        st.write(f"{info['icon']} **{item_lower}**")
        st.write(f"- 재질: {info['category']}")
        st.write(f"- 재활용 여부: {info['recyclable']}")
        st.write(f"- 안내: {info['info']}")
    else:
        st.warning("⚠ 해당 품목 정보가 없습니다. 다른 이름으로 검색해보세요.")

# --------------------------
# 사용 팁
# --------------------------
st.write("---")
st.write("💡 팁: 정확한 검색을 위해 일반적으로 쓰이는 이름을 입력하세요. 예: '페트병', '유리병', '신문지'")
