import streamlit as st

# --------------------------
# 페이지 설정
# --------------------------
st.set_page_config(
    page_title="♻️ 분리수거 가이드 앱",
    layout="centered",
    page_icon="♻️"
)

# --------------------------
# 앱 제목 & 설명
# --------------------------
st.markdown("<h1 style='text-align:center; color:green;'>♻️ 분리수거 가이드 앱</h1>", unsafe_allow_html=True)
st.markdown(
    """
    <p style='text-align:center; color:gray; font-size:18px;'>
    품목별로 재활용 정보를 확인하고, 올바른 분리수거 방법을 안내합니다.<br>
    아래 카테고리에서 선택하고, 버튼을 클릭하면 상세 정보를 볼 수 있어요!
    </p>
    """,
    unsafe_allow_html=True
)
st.markdown("---")

# --------------------------
# 데이터베이스 (재분류 + 확장)
# --------------------------
recycle_guide = {
    # 플라스틱
    "페트병": {"category": "플라스틱", "icon": "🥤", "recyclable": "✅ 재활용 가능"},
    "플라스틱 용기": {"category": "플라스틱", "icon": "🛢️", "recyclable": "✅ 재활용 가능"},
    "플라스틱 빨대": {"category": "플라스틱", "icon": "🥤", "recyclable": "❌ 일반쓰레기"},
    "플라스틱 장난감": {"category": "플라스틱", "icon": "🧸", "recyclable": "❌ 일반쓰레기"},
    "플라스틱 컵": {"category": "플라스틱", "icon": "🥛", "recyclable": "✅ 재활용 가능"},
    "플라스틱 뚜껑": {"category": "플라스틱", "icon": "🛢️", "recyclable": "✅ 재활용 가능"},
    "작은 플라스틱 부품": {"category": "플라스틱", "icon": "🔧", "recyclable": "❌ 일반쓰레기"},

    # 종이
    "신문지": {"category": "종이", "icon": "📰", "recyclable": "✅ 재활용 가능"},
    "책": {"category": "종이", "icon": "📚", "recyclable": "✅ 재활용 가능"},
    "종이봉투": {"category": "종이", "icon": "🛍️", "recyclable": "✅ 재활용 가능"},
    "종이상자": {"category": "종이", "icon": "📦", "recyclable": "✅ 재활용 가능"},
    "노트": {"category": "종이", "icon": "📒", "recyclable": "✅ 재활용 가능"},
    "포장지": {"category": "종이", "icon": "🎁", "recyclable": "✅ 재활용 가능"},

    # 유리
    "유리병": {"category": "유리", "icon": "🍾", "recyclable": "✅ 재활용 가능"},
    "유리컵": {"category": "유리", "icon": "🥂", "recyclable": "❌ 일반쓰레기"},
    "유리조각": {"category": "유리", "icon": "🔹", "recyclable": "❌ 일반쓰레기"},
    "와인병": {"category": "유리", "icon": "🍷", "recyclable": "✅ 재활용 가능"},

    # 캔
    "음료 캔": {"category": "캔", "icon": "🥫", "recyclable": "✅ 재활용 가능"},
    "철 캔": {"category": "캔", "icon": "🛢️", "recyclable": "✅ 재활용 가능"},
    "알루미늄 캔": {"category": "캔", "icon": "🥫", "recyclable": "✅ 재활용 가능"},

    # 음식물
    "남은 음식": {"category": "음식물", "icon": "🍚", "recyclable": "❌ 일반쓰레기"},
    "과일 껍질": {"category": "음식물", "icon": "🍊", "recyclable": "❌ 일반쓰레기"},
    "커피 찌꺼기": {"category": "음식물", "icon": "☕", "recyclable": "❌ 일반쓰레기"},
    "채소 찌꺼기": {"category": "음식물", "icon": "🥬", "recyclable": "❌ 일반쓰레기"},

    # 일반쓰레기
    "종이컵": {"category": "일반쓰레기", "icon": "☕", "recyclable": "❌ 일반쓰레기"},
    "일회용 라이터": {"category": "일반쓰레기", "icon": "🔥", "recyclable": "❌ 일반쓰레기"},
    "고무장갑": {"category": "일반쓰레기", "icon": "🧤", "recyclable": "❌ 일반쓰레기"},
    "휴지": {"category": "일반쓰레기", "icon": "🧻", "recyclable": "❌ 일반쓰레기"},
    "면봉": {"category": "일반쓰레기", "icon": "🧴", "recyclable": "❌ 일반쓰레기"},

    # 전자제품
    "휴대폰": {"category": "전자제품", "icon": "📱", "recyclable": "♻️ 전자제품 수거함"},
    "배터리": {"category": "전자제품", "icon": "🔋", "recyclable": "♻️ 전자제품 수거함"},
    "이어폰": {"category": "전자제품", "icon": "🎧", "recyclable": "♻️ 전자제품 수거함"},
    "충전기": {"category": "전자제품", "icon": "🔌", "recyclable": "♻️ 전자제품 수거함"},

    # 비닐
    "비닐봉지": {"category": "비닐", "icon": "🛍️", "recyclable": "❌ 일반쓰레기"},
    "비닐랩": {"category": "비닐", "icon": "🍱", "recyclable": "❌ 일반쓰레기"},
    "비닐포장재": {"category": "비닐", "icon": "📦", "recyclable": "❌ 일반쓰레기"},
    "비닐장판": {"category": "비닐", "icon": "🟩", "recyclable": "❌ 일반쓰레기"},
    "비닐컵": {"category": "비닐", "icon": "🥤", "recyclable": "❌ 일반쓰레기"},

    # 기타
    "스티로폼": {"category": "기타", "icon": "🍦", "recyclable": "❌ 일반쓰레기"},
    "고철": {"category": "기타", "icon": "⚙️", "recyclable": "❌ 일반쓰레기"},
    "버튼 전지": {"category": "기타", "icon": "🔋", "recyclable": "❌ 일반쓰레기"}
}

# --------------------------
# 카테고리 선택
# --------------------------
st.subheader("카테고리별 보기 📂")
category_list = ["플라스틱", "종이", "유리", "캔", "음식물", "일반쓰레기", "전자제품", "비닐", "기타"]
selected_category = st.selectbox("카테고리를 선택하세요:", category_list)

st.markdown(f"### 🟢 {selected_category} 품목 목록")

# --------------------------
# 선택된 카테고리 품목 버튼 생성
# --------------------------
category_items = [name for name, info in recycle_guide.items() if info["category"] == selected_category]

if category_items:
    for item_name in category_items:
        col1, col2 = st.columns([1, 5])
        with col1:
            st.markdown(f"{recycle_guide[item_name]['icon']}", unsafe_allow_html=True)
        with col2:
            if st.button(f"{item_name}"):
                info = recycle_guide[item_name]
                st.success(f"{info['icon']} **품목:** {item_name}")
                st.write(f"**분류:** {info['category']}")
                st.write(f"**재활용 여부:** {info['recyclable']}")
else:
    st.info("해당 카테고리에 등록된 품목이 없습니다.")

st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:gray;'>앱 제작: 원민 ♻️</p>",
    unsafe_allow_html=True
)
