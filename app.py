import streamlit as st

st.set_page_config(page_title="분리수거 가이드", layout="centered")
st.title("♻️ 분리수거 가이드 앱")
st.markdown("카테고리를 선택하고, 품목 버튼을 클릭하면 상세 정보를 확인할 수 있어요!")

# --------------------------
# 데이터베이스 (아이콘만)
# --------------------------
recycle_guide = {
    "페트병": {"category": "플라스틱", "icon": "🥤", "recyclable": "✅ 재활용 가능"},
    "플라스틱 용기": {"category": "플라스틱", "icon": "🛢️", "recyclable": "✅ 재활용 가능"},
    "신문지": {"category": "종이", "icon": "📰", "recyclable": "✅ 재활용 가능"},
    "책": {"category": "종이", "icon": "📚", "recyclable": "✅ 재활용 가능"},
    "유리병": {"category": "유리", "icon": "🍾", "recyclable": "✅ 재활용 가능"},
    "음료 캔": {"category": "캔", "icon": "🥫", "recyclable": "✅ 재활용 가능"},
    "철 캔": {"category": "캔", "icon": "🛢️", "recyclable": "✅ 재활용 가능"},
    "남은 음식": {"category": "음식물", "icon": "🍚", "recyclable": "❌ 일반쓰레기"},
    "종이컵": {"category": "일반쓰레기", "icon": "☕", "recyclable": "❌ 일반쓰레기"},
    "휴대폰": {"category": "전자제품", "icon": "📱", "recyclable": "♻️ 전자제품 수거함"},
    "배터리": {"category": "전자제품", "icon": "🔋", "recyclable": "♻️ 전자제품 수거함"},
    "비닐봉지": {"category": "기타", "icon": "🛍️", "recyclable": "❌ 일반쓰레기"},
    "스티로폼": {"category": "기타", "icon": "🍦", "recyclable": "❌ 일반쓰레기"}
}

# --------------------------
# 카테고리 선택
# --------------------------
st.subheader("카테고리별 보기 📂")
category_list = ["플라스틱", "종이", "유리", "캔", "음식물", "일반쓰레기", "전자제품", "기타"]
selected_category = st.selectbox("카테고리를 선택하세요:", category_list)

# --------------------------
# 선택된 카테고리 품목 버튼 생성
# --------------------------
st.write(f"### {selected_category} 품목 목록")

category_items = [name for name, info in recycle_guide.items() if info["category"] == selected_category]

if category_items:
    for item_name in category_items:
        if st.button(f"{recycle_guide[item_name]['icon']} {item_name}"):
            # 버튼 클릭 시 상세 정보 표시
            info = recycle_guide[item_name]
            st.success(f"{info['icon']} **품목:** {item_name}")
            st.write(f"**분류:** {info['category']}")
            st.write(f"**재활용 여부:** {info['recyclable']}")
else:
    st.write("해당 카테고리에 등록된 품목이 없습니다.")
