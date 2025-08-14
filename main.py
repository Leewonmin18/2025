import streamlit as st

# ===== MBTI별 취미 추천 데이터 =====
hobby_recommendations = {
    "INTJ": [
        {"hobby": "체스", "icon": "♟️", "desc": "전략과 분석을 즐기는 보드게임"},
        {"hobby": "독서", "icon": "📚", "desc": "깊이 있는 지식과 통찰을 쌓는 활동"},
        {"hobby": "코딩", "icon": "💻", "desc": "논리와 창의성을 결합한 문제 해결"}
    ],
    "INTP": [
        {"hobby": "퍼즐 맞추기", "icon": "🧩", "desc": "복잡한 문제 해결에서 오는 성취감"},
        {"hobby": "과학 실험", "icon": "🔬", "desc": "새로운 지식을 탐구하는 즐거움"},
        {"hobby": "블로그 글쓰기", "icon": "✍️", "desc": "아이디어와 생각을 공유"}
    ],
    "ENTJ": [
        {"hobby": "비즈니스 플랜 작성", "icon": "📈", "desc": "목표와 전략을 설계하는 즐거움"},
        {"hobby": "토론", "icon": "💬", "desc": "논리적 사고와 설득력을 키우는 활동"},
        {"hobby": "리더십 워크숍", "icon": "🏆", "desc": "리더십 스킬을 강화하는 모임"}
    ],
    "ENTP": [
        {"hobby": "창업 아이디어 기획", "icon": "🚀", "desc": "새로운 가능성을 찾고 실행"},
        {"hobby": "즉흥 연기", "icon": "🎭", "desc": "창의력과 유머 감각을 발휘"},
        {"hobby": "팟캐스트 진행", "icon": "🎤", "desc": "사람들과 이야기 나누기"}
    ],
    "INFJ": [
        {"hobby": "일기 쓰기", "icon": "📓", "desc": "감정과 생각을 정리"},
        {"hobby": "사진 촬영", "icon": "📷", "desc": "세상을 예술적으로 기록"},
        {"hobby": "명상", "icon": "🧘‍♀️", "desc": "마음을 차분하게 하는 활동"}
    ],
    "INFP": [
        {"hobby": "그림 그리기", "icon": "🎨", "desc": "감정을 시각적으로 표현"},
        {"hobby": "노래 만들기", "icon": "🎵", "desc": "감성을 음악에 담기"},
        {"hobby": "자원봉사", "icon": "🤝", "desc": "다른 사람을 돕는 기쁨"}
    ],
    "ENFJ": [
        {"hobby": "동아리 활동", "icon": "🤝", "desc": "사람들과 협력하는 즐거움"},
        {"hobby": "연극 공연", "icon": "🎭", "desc": "팀워크와 창의성을 발휘"},
        {"hobby": "퍼실리테이션", "icon": "📋", "desc": "모임을 이끌고 소통"}
    ],
    "ENFP": [
        {"hobby": "여행", "icon": "✈️", "desc": "새로운 경험과 사람 만나기"},
        {"hobby": "댄스", "icon": "💃", "desc": "자유롭게 에너지를 발산"},
        {"hobby": "유튜브 촬영", "icon": "📹", "desc": "창의적인 콘텐츠 제작"}
    ],
    "ISTJ": [
        {"hobby": "가계부 작성", "icon": "📒", "desc": "체계적인 재정 관리"},
        {"hobby": "정원 가꾸기", "icon": "🌱", "desc": "꾸준함이 필요한 취미"},
        {"hobby": "등산", "icon": "🥾", "desc": "규칙적인 운동과 자연 탐방"}
    ],
    "ISFJ": [
        {"hobby": "베이킹", "icon": "🧁", "desc": "정성과 시간을 들여 완성"},
        {"hobby": "사진 앨범 만들기", "icon": "📖", "desc": "추억을 소중하게 보관"},
        {"hobby": "손편지 쓰기", "icon": "💌", "desc": "마음을 전하는 글쓰기"}
    ],
    "ESTJ": [
        {"hobby": "동호회 운영", "icon": "📅", "desc": "조직적이고 효율적인 모임 관리"},
        {"hobby": "마라톤", "icon": "🏃‍♂️", "desc": "목표를 향한 꾸준한 도전"},
        {"hobby": "재테크 공부", "icon": "💹", "desc": "경제적 목표 달성"}
    ],
    "ESFJ": [
        {"hobby": "파티 기획", "icon": "🎉", "desc": "사람들과 함께하는 즐거움"},
        {"hobby": "요리", "icon": "🍲", "desc": "맛있는 음식으로 행복 전달"},
        {"hobby": "플로리스트 활동", "icon": "💐", "desc": "꽃으로 감성 표현"}
    ],
    "ISTP": [
        {"hobby": "자동차 정비", "icon": "🚗", "desc": "기계 구조 이해와 수리"},
        {"hobby": "캠핑", "icon": "🏕️", "desc": "야외에서의 자유와 모험"},
        {"hobby": "드론 조종", "icon": "🚁", "desc": "기술과 재미를 결합"}
    ],
    "ISFP": [
        {"hobby": "사진 촬영", "icon": "📷", "desc": "감각적인 순간 포착"},
        {"hobby": "악기 연주", "icon": "🎸", "desc": "음악으로 감정 표현"},
        {"hobby": "캘리그라피", "icon": "🖌️", "desc": "아름다운 글씨 쓰기"}
    ],
    "ESTP": [
        {"hobby": "서핑", "icon": "🏄‍♂️", "desc": "스릴 넘치는 파도 타기"},
        {"hobby": "스카이다이빙", "icon": "🪂", "desc": "하늘에서 느끼는 자유"},
        {"hobby": "락 클라이밍", "icon": "🧗", "desc": "도전과 체력 강화"}
    ],
    "ESFP": [
        {"hobby": "노래방", "icon": "🎤", "desc": "흥과 끼를 발산"},
        {"hobby": "댄스파티", "icon": "🕺", "desc": "에너지를 함께 나누는 즐거움"},
        {"hobby": "여행 브이로그", "icon": "📹", "desc": "추억을 영상으로 남기기"}
    ]
}

# ===== Streamlit 앱 UI =====
st.set_page_config(page_title="MBTI 취미 추천기", page_icon="🎯", layout="centered")
st.title("🎯 MBTI 기반 취미 추천기")
st.markdown("당신의 MBTI에 맞는 취미를 추천해드립니다.  
**MBTI를 선택**하고 버튼을 눌러보세요!")

# MBTI 선택
mbti = st.selectbox(
    "당신의 MBTI를 선택하세요",
    sorted(hobby_recommendations.keys())
)

# 추천 버튼 클릭 시 결과 출력
if st.button("✨ 취미 추천 받기"):
    st.subheader(f"🔍 {mbti} 유형 추천 취미")
    for rec in hobby_recommendations.get(mbti, []):
        st.markdown(
            f"""
            <div style="background-color:#f9f9f9; padding:15px; border-radius:10px; margin-bottom:10px;">
                <h4>{rec['icon']} {rec['hobby']}</h4>
                <p>{rec['desc']}</p>
            </div>
            """, 
            unsafe_allow_html=True
        )

st.markdown("---")
st.markdown("📌 **Tip:** MBTI는 참고용이며, 실제 취미 선택은 개인의 관심과 환경을 종합적으로 고려해야 합니다.")
