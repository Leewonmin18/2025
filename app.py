import streamlit as st

# --------------------------
# 데이터베이스 (예시)
# --------------------------
recycle_guide = {
    "페트병": {
        "category": "플라스틱",
        "icon": "🥤",
        "recyclable": "✅ 재활용 가능",
        "guide": "내용물을 비우고 라벨 제거 후 압착하여 투명봉투에 담아 배출합니다."
    },
    "종이컵": {
        "category": "종이",
        "icon": "☕",
        "recyclable": "♻️ 재활용 가능 (세척 필수)",
        "guide": "내용물을 비우고 헹군 후 다른 종이류와 분리하여 배출합니다."
    },
    "비닐봉지": {
        "category": "비닐",
        "icon": "🛍️",
        "recyclable": "♻️ 재활용 가능 (이물질 제거)",
        "guide": "음식물, 스티커 등을 제거 후 배출합니다. 제거가 어렵다면 종량제 봉투에 버립니다."
    },
    "캔": {
        "category": "금속",
        "icon": "🥫",
        "recyclable": "✅ 재활용 가능",
        "guide": "내용물을 비우고 헹군 후 압착하여 배출합니다."
    },
    "유리병": {
        "category": "유리",
        "icon": "🍾",
        "recyclable": "✅ 재활용 가능",
        "guide": "뚜껑을 분리하고 내용물을 비운 후 배출합니다."
    },
    "폐건전지": {
        "category": "특수폐기물",
        "icon": "🔋",
        "recyclable": "⚠️ 전용 수거함 배출",
        "guide": "전용 수거함에 배출합니다."
    },
    "형광등": {
        "category": "특수폐기물",
        "icon": "💡",
        "recyclable": "⚠️ 전용 수거함 배출",
        "guide": "깨지지 않도록 주의하며 전용 수거함에 배출합니다."
    },
}

# --------------------------
# Streamlit 앱 구성
# --------------------------
st.title("♻️ 분리수거 가이드 앱")

st.header("1. 재활용품 배출 요령")
st.markdown("""
- **내용물 비우기**: 음식물, 내용물을 남기지 않고 완전히 비웁니다.  
- **깨끗하게 헹구기**: 음식물, 이물질이 남지 않도록 물로 헹군 뒤 말립니다.  
- **재질별 분리**: 플라스틱, 캔, 유리, 종이 등 재질별로 구분합니다.  
- **수거함 배출**: 투명한 비닐봉투 또는 지정된 수거함에 종류별로 담아 배출합니다.  
""")

st.header("2. 재활용품 종류별 분리 방법")
st.markdown("""
- **종이류**: 젖지 않게 반듯하게 펴서 묶어 배출  
- **종이팩(우유팩 등)**: 헹군 후 종이팩 전용 수거함 배출  
- **비닐류**: 이물질 제거 후 배출, 제거 불가 시 종량제 봉투 배출  
- **플라스틱**: 내용물을 비우고 투명 봉투에 배출  
- **캔/병류**: 내용물을 비우고 헹군 뒤 배출  
- **폐건전지/폐형광등**: 전용 수거함 배출 (깨진 경우 신문지로 감싸기)  
- **백열등**: 종량제 봉투에 배출 (재활용 불가)  
""")

st.header("3. 주의사항")
st.markdown("""
- **이물질**: 음식물, 스티커 등 제거 어려운 경우 종량제 봉투 배출  
- **혼합 배출 금지**: 재활용품과 일반쓰레기를 혼합하지 않습니다.  
- **투명 봉투 사용**: 내용물이 보이는 투명 봉투에 담아야 합니다.  
- **대형 폐가전**: 인터넷/콜센터(1599-0903)로 신청 후 무상 방문 수거 서비스 이용 가능  
""")

st.header("4. 품목별 분리수거 검색")
query = st.text_input("검색할 품목을 입력하세요:")

if query:
    # 입력한 검색어와 부분 일치하는 항목 찾기 (대소문자 구분 없음)
    results = [name for name in recycle_guide if query.lower() in name.lower()]
    
    if results:
        for item in results:
            info = recycle_guide[item]
            st.success(f"{info['icon']} **{item}**")
            st.write(f"**분류:** {info['category']}")
            st.write(f"**재활용 여부:** {info['recyclable']}")
            st.write(f"**배출 요령:** {info['guide']}")
            st.markdown("---")
    else:
        st.warning("검색 결과가 없습니다. 다른 키워드를 입력해보세요.")

st.header("5. 카테고리별 품목 보기")
categories = set(item["category"] for item in recycle_guide.values())
for category in categories:
    with st.expander(f"📂 {category}"):
        for item_name, info in recycle_guide.items():
            if info["category"] == category:
                st.write(f"{info['icon']} **{item_name}** - {info['recyclable']}")
                st.caption(info["guide"])
