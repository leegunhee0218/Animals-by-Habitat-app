import streamlit as st

# 1. 리스트(list) 활용: 8개 서식지 목록과 5가지 척추동물 분류 목록
habitats = [
    "열대우림", "초원(사바나)", "사막", "온대림(숲)",
    "툰드라", "바다", "민물(강과 호수)", "산악 지대"
]
animal_classes = ["포유류", "파충류", "양서류", "조류", "어류"]


# 2. 함수(def) 활용 1: 서식지에 따른 기후 설명과 동물 데이터를 반환하는 함수
def get_habitat_info(selected):
    # 3. 선택구조(if-elif-else) 활용
    if selected == "열대우림":
        climate = "일 년 내내 기온이 높고 비가 매우 많이 내려 습도가 높습니다. 지구상에서 생물 다양성이 가장 풍부하고 울창한 숲이 형성되는 환경입니다."
        animals = {
            "포유류": ["재규어", "오랑우탄", "나무늘보"],
            "파충류": ["아나콘다", "초록나무비단뱀", "카멜레온"],
            "양서류": ["독화살개구리", "붉은눈청개구리", "아마존뿔개구리"],
            "조류": ["투칸(큰부리새)", "금강앵무", "부채머리수리"],
            "어류": ["피라냐", "아로와나", "네온테트라"]
        }
    elif selected == "초원(사바나)":
        climate = "기온이 높고 비가 많이 내리는 우기와 비가 거의 오지 않는 건기가 뚜렷하게 나타납니다. 키 큰 풀과 드문드문 자라는 나무가 넓게 펼쳐져 있습니다."
        animals = {
            "포유류": ["사자", "아프리카코끼리", "기린"],
            "파충류": ["나일악어", "블랙맘바", "레오파드육지거북"],
            "양서류": ["아프리카황소개구리", "사바나두꺼비", "갈대개구리"],
            "조류": ["타조", "뱀잡이수리", "대머리황새"],
            "어류": ["폐어(프로토프테루스)", "아프리카메기", "틸라피아"]
        }
    elif selected == "사막":
        climate = "강수량이 극도로 적고 건조하며, 낮에는 매우 뜨겁고 밤에는 기온이 급격히 떨어져 일교차가 큽니다. 식물이 자라기 어려워 모래와 바위가 많습니다."
        animals = {
            "포유류": ["단봉낙타", "사막여우", "미어캣"],
            "파충류": ["방울뱀", "사막뿔도마뱀", "사막거북"],
            "양서류": ["사막비개구리", "쟁기발두꺼비", "콜로라도강두꺼비"],
            "조류": ["길달리기새", "사막수리부엉이", "선인장굴뚝새"],
            "어류": ["데스밸리 펍피시", "사막 송사리", "오아시스 잉어"]
        }
    elif selected == "온대림(숲)":
        climate = "봄, 여름, 가을, 겨울의 사계절 변화가 뚜렷하고 강수량이 적당합니다. 계절에 따라 잎이 떨어지는 활엽수와 침엽수가 어우러져 자랍니다."
        animals = {
            "포유류": ["반달가슴곰", "청설모", "고라니"],
            "파충류": ["유혈목이", "도마뱀", "남생이"],
            "양서류": ["청개구리", "두꺼비", "도롱뇽"],
            "조류": ["딱따구리", "참새", "수리부엉이"],
            "어류": ["송어", "피라미", "은어"]
        }
    elif selected == "툰드라":
        climate = "일 년 중 대부분이 영하의 기온을 유지하며 땅속이 얼어있는 영구동토층이 존재합니다. 짧은 여름 동안에만 이끼와 작은 풀들이 자랍니다."
        animals = {
            "포유류": ["북극곰", "순록(카리부)", "북극여우"],
            "파충류": ["서식 종 없음(극저온 환경)", "변온동물 생존 불가", "-"],
            "양서류": ["숲개구리(일부 경계 지역)", "시베리아도롱뇽", "-"],
            "조류": ["흰올빼미", "뇌조", "북극제비갈매기"],
            "어류": ["북극곤들매기", "북극대구", "빙어"]
        }
    elif selected == "바다":
        climate = "지구 표면의 약 70%를 차지하는 염분(소금기)이 있는 거대한 물 환경입니다. 수심과 위도에 따라 수온과 빛의 양이 크게 달라집니다."
        animals = {
            "포유류": ["대왕고래", "큰돌고래", "해달"],
            "파충류": ["푸른바다거북", "바다이구아나", "바다뱀"],
            "양서류": ["서식 종 없음(염분 환경)", "피부 삼투압 조절 불가", "-"],
            "조류": ["황제펭귄", "알바트로스", "갈매기"],
            "어류": ["백상아리", "참다랑어", "흰동가리"]
        }
    elif selected == "민물(강과 호수)":
        climate = "염분이 거의 없는 담수 환경으로, 흐르는 강물과 고여 있는 호수·연못을 포함합니다. 육지 생태계와 밀접하게 연결되어 수질과 계절의 영향을 받습니다."
        animals = {
            "포유류": ["수달", "비버", "하마"],
            "파충류": ["붉은귀거북", "자라", "강악어"],
            "양서류": ["참개구리", "무당개구리", "맹꽁이"],
            "조류": ["왜가리", "물총새", "청둥오리"],
            "어류": ["잉어", "메기", "쏘가리"]
        }
    else:  # 산악 지대
        climate = "해발 고도가 높아질수록 기온이 낮아지고 기압이 떨어지며 바람이 강하게 붑니다. 고도에 따라 기후와 식생이 수직적으로 변하는 특징이 있습니다."
        animals = {
            "포유류": ["눈표범", "산양", "알파카"],
            "파충류": ["살모사", "산도마뱀", "무자치"],
            "양서류": ["꼬리치레도롱뇽", "계곡산개구리", "물두꺼비"],
            "조류": ["검독수리", "안데스콘도르", "잣까마귀"],
            "어류": ["산천어", "열목어", "금강모치"]
        }

    return climate, animals


# 2. 함수(def) 활용 2: 선택된 동물 분류의 대표 동물 3마리를 출력하는 함수
def display_animals(animal_class, animal_list):
    st.subheader(f"🐾 {animal_class} 대표 동물 3마리")
    # 4. 반복구조(for) 활용 1: 리스트에 담긴 동물 3마리를 순서대로 출력
    for i in range(len(animal_list)):
        st.write(f"**{i + 1}.** {animal_list[i]}")


# --- 웹앱 화면 구성 ---
st.title("[서식지별 기후환경 및 주요 서식 동물]")

# 웹페이지 새로고침 시에도 상태가 유지되도록 세션 초기화
if "analyzed" not in st.session_state:
    st.session_state.analyzed = False
if "selected_habitat" not in st.session_state:
    st.session_state.selected_habitat = habitats[0]
if "selected_class" not in st.session_state:
    st.session_state.selected_class = None

# 서식지 드롭다운 선택
choice = st.selectbox("서식지 선택 :", habitats)

# [분석하기] 버튼 클릭 시 상태 저장
if st.button("분석하기"):
    st.session_state.analyzed = True
    st.session_state.selected_habitat = choice
    st.session_state.selected_class = None  # 서식지를 새로 분석하면 동물 선택 초기화

# [분석하기]를 누른 후 화면 표시
if st.session_state.analyzed:
    current_habitat = st.session_state.selected_habitat
    climate_desc, current_animals = get_habitat_info(current_habitat)

    # 기후 환경 텍스트 출력
    st.info(f"**{current_habitat}**의 기후 환경은 {climate_desc}")

    st.write("### 척추동물 분류 선택")
    cols = st.columns(5)  # 5개의 버튼을 가로로 나란히 배치

    # 4. 반복구조(for) 활용 2: 5가지 척추동물 분류 버튼을 반복문으로 생성
    for idx in range(len(animal_classes)):
        a_class = animal_classes[idx]
        with cols[idx]:
            if st.button(a_class, use_container_width=True):
                st.session_state.selected_class = a_class

    # 분류 버튼이 눌렸다면 해당 동물 3마리 출력
    if st.session_state.selected_class:
        st.divider()
        chosen_class = st.session_state.selected_class
        display_animals(chosen_class, current_animals[chosen_class])
