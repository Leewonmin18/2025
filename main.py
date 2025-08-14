import streamlit as st

# MBTI별 직업 추천 데이터
job_recommendations = {
    "INTJ": ["전략 컨설턴트", "데이터 과학자", "연구원", "변호사"],
    "INTP": ["프로그래머", "이공계 연구원", "UX 디자이너", "발명가"],
    "ENTJ": ["경영 컨설턴트", "프로젝트 매니저", "기업가", "변호사"],
    "ENTP": ["창업가", "마케터", "언론인", "광고 기획자"],
    "INFJ": ["심리상담사", "작가", "교사", "사회운동가"],
    "INFP": ["예술가", "소설가", "작곡가", "사회복지사"],
    "ENFJ": ["강사", "정치가", "홍보전문가", "심리상담사"],
    "ENFP": ["방송인", "광고기획자", "작가", "기자"],
    "ISTJ": ["회계사", "행정직", "엔지니어", "군인"],
    "ISFJ": ["간호사", "교사", "사회복지사", "비서"],
    "ESTJ": ["경영자", "공무원", "군인", "팀장"],
    "ESFJ": ["간호사", "영업직", "HR담당자", "서비스 매니저"],
    "ISTP": ["엔지니어", "항공정비사", "응급구조사", "스포츠 코치"],
    "ISFP": ["디자이너", "사진작가", "요리사", "음악가"],
    "ESTP": ["영업직", "이벤트 플래너", "운동선수", "기업가"],
    "ESFP": ["배우", "뮤지션", "이벤트 코디네이터", "방송인"]
}

# 앱 제목
st.title("💼 MBTI 기반 직업 추천기")

# MBTI 입력
mbti = st.selectbox(
    "당신의 MBTI를 선택하세요",
    sorted(job_recommendations.keys())
)

# 추천 버튼
if st.button("직업 추천 받기"):
    recommendations = job_recommendations.get(mbti, [])
    st.subheader(f"{mbti} 유형 추천 직업")
    for job in recommendations:
        st.write(f"- {job}")

# 추가 기능: 설명 표시
st.markdown("---")
st.markdown("📌 **Tip:** MBTI는 참고용이며, 실제 진로는 성향, 가치관, 경험 등을 종합적으로 고려해야 합니다.")

