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
    아래의 <b>분리수거 가이드</b>를 참고하고, 검색 또는 카테고리별로 확인해보세요!
    </p>
    """,
    unsafe_allow_html=True
)
st.markdown("---")

# --------------------------
# 재활용품 배출 가이드
# --------------------------
st.header("1. 재활용품 배출 요령")
st.write("- **내용물 비우기:** 음식물, 내용물 등을 남기지 않고 완전히 비웁니다.")
st.write("- **깨끗하게 헹구기:** 음식물, 이물질 등이 남지 않도록 물로 깨끗이 헹궈 말립니다.")
st.write("- **재질별 분리:** 플라스틱, 캔, 유리, 종이 등 재질별로 분리합니다.")
st.write("- **재질별 수거함 배출:** 투명한 비닐봉투나 지정된 수거함에 종류별로 담아 배출합니다.")

st.header("2. 재활용품 종류별 분리 방법")
st.subheader("📄 종이류")
st.write("신문지, 책자, 종이팩 등은 물에 젖지 않게 반듯하게 펴서 묶어 배출합니다.")

st.subheader("🥛 종이팩 (우유팩 등)")
st.write("내용물을 비우고 헹군 뒤, 종이팩 전용 수거함에 배출합니다.")

st.subheader("🛍️ 비닐류")
st.write("음식물, 스티커 등의 이물질을 헹궈서 제거하고 배출합니다. 이물질 제거가 어려우면 종량제 봉투에 담아 배출합니다.")

st.subheader("🧴 플라스틱")
st.write("내용물을 비우고 헹군 뒤, 투명 봉투에 담아 배출합니다.")

st.subheader("🥫 캔류/병류")
st.write("내용물을 비우고 헹군 뒤, 투명 봉투에 담아 배출합니다.")

st.subheader("🔋 폐건전지/폐형광등")
st.write("깨지지 않게 주의하며 전용수거함에 배출합니다. 깨진 경우 신문지로 감싸 배출합니다.")

st.subheader("💡 백열등")
st.write("재활용이 안 되므로 종량제 봉투에 담아 버립니다.")

st.header("3. 주의사항")
st.write("- **이물질:** 재활용품에 음식물, 스티커 등 제거하기 어려운 이물질이 묻어 있으면 재활용이 불가하므로 종량제 봉투에 버려야 합니다.")
st.write("- **혼합 배출 금지:** 재활용품과 일반쓰레기를 혼합하지 않도록 합니다.")
st.write("- **투명 봉투 사용:** 재활용품은 내용물이 확인 가능한 투명 봉투에 담아 배출해야 합니다.")
st.write("- **대형 폐가전:** 인터넷 또는 콜센터(1599-0903)로 신청하여 무상 방문 수거 서비스를 이용할 수 있습니다.")

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
    "플라스틱 포크": {"category": "플라스틱", "icon": "🍴", "recyclable": "❌ 일반쓰레기"},

    # 종이
    "신문지": {"category": "종이", "icon": "📰", "recyclable": "✅ 재활용 가능"},
    "책": {"category": "종이", "icon": "📚", "recyclable": "✅ 재활용 가능"},
    "종이봉투": {"category": "종이", "icon": "🛍️", "recyclable": "✅ 재활용 가능"},
    "종이상자": {"category": "종이", "icon": "📦", "recyclable": "✅ 재활용 가능"},
    "노트": {"category": "종이", "icon": "📒", "recyclable": "✅ 재활용 가능"},
    "포장지": {"category": "종이", "icon": "🎁", "recyclable": "✅ 재활용 가능"},
    "영수증": {"category": "종이", "icon": "🧾", "recyclable": "❌ 일반쓰레기"},

    # 유리
    "유리병": {"category": "유리", "icon": "🍾", "recyclable": "✅ 재활용 가능"},
    "유리컵": {"category": "유리", "icon": "🥂", "recyclable": "❌ 일반쓰레기"},
    "유리조각": {"category": "유리", "icon": "🔹", "recyclable": "❌ 일반쓰레기"},
    "와인병": {"category": "유리", "icon": "🍷", "recyclable": "✅ 재활용 가능"},
    "깨진 거울": {"category": "유리", "icon": "🪞", "recyclable": "❌ 일반쓰레기"},

    # 캔
    "음료 캔": {"category": "캔", "icon": "🥫", "recyclable": "✅ 재활용 가능"},
    "철 캔": {"category": "캔", "icon": "🛢️", "recyclable": "✅ 재활용 가능"},
    "알루미늄 캔": {"category": "캔", "icon": "🥫", "recyclable": "✅ 재활용 가능"},
    "통조림 캔": {"category": "캔", "icon": "🥫", "recyclable": "✅ 재활용 가능"},

    # 음식물
    "남은 음식": {"category": "음식물", "icon": "🍚", "recyclable": "❌ 일반쓰레기"},
    "과일 껍질": {"category": "음식물", "icon": "🍊", "recyclable": "❌ 일반쓰레기"},
    "커피 찌꺼기": {"category": "음식물", "icon": "☕", "recyclable": "❌ 일반쓰레기"},
    "채소 찌꺼기": {"category": "음식물", "icon": "🥬", "recyclable": "❌ 일반쓰레기"},
    "생선 뼈": {"category": "음식물", "icon": "🐟", "recyclable": "❌ 일반쓰레기"},

    # 일반쓰레기
    "종이컵": {"category": "일반쓰레기", "icon": "☕", "recyclable": "❌ 일반쓰레기"},
    "일회용 라이터": {"category": "일반쓰레기", "icon": "🔥", "recyclable": "❌ 일반쓰레기"},
    "고무장갑": {"category": "일반쓰레기", "icon": "🧤", "recyclable": "❌ 일반쓰레기"},
    "휴지": {"category": "일반쓰레기", "icon": "🧻", "recyclable": "❌ 일반쓰레기"},
    "면봉": {"category": "일반쓰레기", "icon": "🧴", "recyclable": "❌ 일반쓰레기"},
    "종이 티슈": {"category": "일반쓰레기", "icon": "🧻", "recyclable": "❌ 일반쓰레기"},

    # 전자제품
    "휴대폰": {"category": "전자제품", "icon": "📱", "recyclable": "♻️ 전자제품 수거함"},
    "배터리": {"category": "전자제품", "icon": "🔋", "recyclable": "♻️ 전자제품 수거함"},
    "이어폰": {"category": "전자제품", "icon": "🎧", "recyclable": "♻️ 전자제품 수거함"},
    "충전기": {"category": "전자제품", "icon": "🔌", "recyclable": "♻️ 전자제품 수거함"},
    "노트북": {"category": "전자제품", "icon": "💻", "recyclable": "♻️ 전자제품 수거함"},
    "TV": {"category": "전자제품", "icon": "📺", "recyclable": "♻️ 대형 폐가전 수거"},

    # 비닐
    "비닐봉지": {"category": "비닐", "icon": "🛍️", "recyclable": "❌ 일반쓰레기"},
    "비닐랩": {"category": "비닐", "icon": "🍱", "recyclable": "❌ 일반쓰레기"},
    "비닐포장재": {"category": "비닐", "icon": "📦", "recyclable": "❌ 일반쓰레기"},
    "비닐장판": {"category": "비닐", "icon": "🟩", "recyclable": "❌ 일반쓰레기"},
    "비닐컵": {"category": "비닐", "icon": "🥤", "recyclable": "❌ 일반쓰레기"},

    # 의류
    "셔츠": {"category": "의류", "icon": "👕", "recyclable": "♻️ 의류 수거함"},
    "청바지": {"category": "의류", "icon": "👖", "recyclable": "♻️ 의류 수거함"},
    "코트": {"category": "의류", "icon": "🧥", "recyclable": "♻️ 의류 수거함"},
    "신발": {"category": "의류", "icon": "👟", "recyclable": "♻️ 의류 수거함"},
    "모자": {"category": "의류", "icon": "🧢", "recyclable": "♻️ 의류 수거함"},

    # 기타
    "스티로폼": {"category": "기타", "icon": "🍦", "recyclable": "❌ 일반쓰레기"},
    "고철": {"category": "기타", "icon": "⚙️", "recyclable": "❌ 일반쓰레기"},
    "버튼 전지": {"category": "기타", "icon": "🔋", "recyclable": "❌ 일반쓰레기"}
}

# --------------------------
# 검색 기능 추가
# --------------------------
st.subheader("검색 기능 🔍")
query = st.text_input("검색할 품목을 입력하세요:")

if query:
    results = [name for name in recycle_guide if query in name]
    if results:
        for item in results:
            info = recycle_guide[item]
            st.success(f"{info['icon']} **품목:** {item}")
            st.write(f"**분류:** {info['category']}")
            st.write(f"**재활용 여부:** {info['recyclable']}")
    else:
        st.warning("검색 결과가 없습니다.")

st.markdown("---")

# --------------------------
# 카테고리 선택
# --------------------------
st.subheader("카테고리별 보기 📂")
category_list = ["플라스틱", "종이", "유리", "캔", "음식물", "일반쓰레기", "전자제품", "비닐", "의류", "기타"]
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
