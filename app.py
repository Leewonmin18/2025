import streamlit as st

st.set_page_config(page_title="분리수거 가이드", page_icon="♻", layout="centered")
st.title("♻ 분리수거 가이드 앱")
st.caption("검색창에 품목을 입력하면 재질/배출 방법을 안내합니다.")

recycle_guide = {
    "페트병": {"category": "플라스틱", "icon": "🥤", "recyclable": "✅ 재활용 가능", "info": "뚜껑/라벨 제거, 내용물 비우고 헹군 뒤 압축."},
    "유리병": {"category": "유리", "icon": "🍾", "recyclable": "✅ 재활용 가능", "info": "뚜껑 분리, 이물질 제거 후 배출."},
    "신문지": {"category": "종이", "icon": "📰", "recyclable": "✅ 재활용 가능", "info": "끈으로 묶어 배출."},
    "캔": {"category": "금속", "icon": "🥫", "recyclable": "✅ 재활용 가능", "info": "내용물 비우고 헹군 뒤 배출."},
    "스티로폼": {"category": "플라스틱", "icon": "📦", "recyclable": "♻ 조건부", "info": "깨끗한 포장재만 가능, 오염되면 일반쓰레기."},
    "플라스틱컵": {"category": "플라스틱", "icon": "🥤", "recyclable": "✅ 재활용 가능", "info": "내용물 비우고 헹군 뒤 배출."},
    "종이컵": {"category": "종이", "icon": "☕", "recyclable": "♻ 지역별 상이", "info": "내부 코팅으로 불가한 곳 많음(지침 확인)."}
}

st.divider()
query = st.text_input("🔎 품목 이름을 입력하세요 (예: 페트병, 유리병, 종이컵)")

if query:
    key = query.strip()
    info = recycle_guide.get(key)
    if info:
        st.success(f"{info['icon']} **{key}**")
        st.write(f"- **재질**: {info['category']}")
        st.write(f"- **재활용 여부**: {info['recyclable']}")
        st.write(f"- **배출 방법**: {info['info']}")
    else:
        st.warning("해당 품목 정보가 없어요. 이름을 바꿔서 다시 검색해 보세요.")

st.divider()
st.caption("Tip: 정확한 이름으로 검색하면 더 잘 찾아요. 데이터는 코드 상단의 `recycle_guide` 딕셔너리에 쉽게 추가할 수 있어요.")
