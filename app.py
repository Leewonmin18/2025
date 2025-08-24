import streamlit as st

st.set_page_config(page_title="분리수거 가이드", layout="centered")
st.title("♻️ 분리수거 가이드 앱")

# --------------------------
# 데이터베이스 (예시)
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
# 검색 기능
# --------------------------
st.subheader("품목 검색")
item = st.text_input("검색할 품목을 입력하세요:")

if item:
    guide = recycle_guide.get(item)
    if guide:
        st.write(f"**품목:** {item} {guide['icon']}")
        st.write(f"**분류:** {guide['category']}")
        st.write(f"**재활용 여부:** {guide['recyclable']}")
    else:
        st.warning("해당 품목 정보가 없습니다.")

# --------------------------
# 카테고리별 보기
# --------------------------
st.subheader("카테고리별 보기")
category_list = ["플라스틱", "종이", "유리", "캔", "음식물", "일반쓰레기", "전자제품", "기타"]
selected_category = st.selectbox("카테고리를 선택하세요:", category_list)

st.write(f"### {selected_category} 품목")
for name, info in recycle_guide.items():
    if info["category"] == selected_category:
        st.write(f"{info['icon']} {name} - {info['recyclable']}")
