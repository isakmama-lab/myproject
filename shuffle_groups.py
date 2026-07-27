"""
학생 조 편성 프로그램
Python 3.12

기능
1. 학생을 수준별(리더, 상, 중, 하)로 균형 있게 배치
2. 각 수준별 학생은 랜덤으로 섞은 후 배치
3. 깍뚜기는 마지막에 랜덤으로 한 조에 추가
4. 출력 시에는 학생 이름만 표시
5. 출력 직전에 각 조의 학생 순서를 다시 섞음
6. Y를 입력하면 다시 추첨
"""

import random

# ==========================================
# 학생 명단 (예시)
# 자유롭게 수정해서 사용하세요.
# ==========================================

students = [
    ("이준수", "리더"),
    ("최혜영", "리더"),
    ("오지원", "리더"),
    ("성경수", "리더"),

    ("박근수", "상"),
    ("김원일", "상"),
    ("송현준", "상"),
    ("김시내", "상"),

    ("김국진", "중"),
    ("백현숙", "중"),
    ("고길웅", "중"),
    ("서경난", "중"),

    ("김선영", "하"),
    ("김환석", "하"),
    ("김경근", "하"),
    ("김다빈", "하"),

    ("이원호", "깍뚜기")
]


# ==========================================
# 학생을 수준별로 분류
# ==========================================
def group_students_by_level(student_list):
    """
    학생들을 수준별로 분류한다.
    """
    groups = {
        "리더": [],
        "상": [],
        "중": [],
        "하": [],
        "깍뚜기": []
    }

    for name, level in student_list:
        groups[level].append(name)

    return groups


# ==========================================
# 조 편성
# ==========================================
def make_teams(student_list):
    """
    학생들을 4개의 조로 배치한다.
    """

    team_names = ["A조", "B조", "C조", "D조"]

    teams = {team: [] for team in team_names}

    level_groups = group_students_by_level(student_list)

    # --------------------------------------
    # 깍뚜기를 제외한 수준별 배치
    # --------------------------------------
    for level in ["리더", "상", "중", "하"]:

        students = level_groups[level]

        # 같은 수준끼리 랜덤 섞기
        random.shuffle(students)

        # A → B → C → D 순환 배치
        for index, student in enumerate(students):
            team = team_names[index % len(team_names)]
            teams[team].append(student)

    # --------------------------------------
    # 깍뚜기 추가
    # --------------------------------------
    if level_groups["깍뚜기"]:
        kkakdugi = level_groups["깍뚜기"][0]

        selected_team = random.choice(team_names)

        teams[selected_team].append(kkakdugi)

    return teams


# ==========================================
# 결과 출력
# ==========================================
def print_teams(teams):
    """
    조 편성 결과 출력
    """

    print("\n")
    print("=" * 35)
    print("        조 편성 결과")
    print("=" * 35)

    for team in teams:

        # 출력 직전에 학생 순서를 다시 섞는다.
        members = teams[team][:]
        random.shuffle(members)

        print(f"\n{team} ({len(members)}명)")
        print("-" * 35)

        for student in members:
            print(student)

    print("\n" + "=" * 35)


# ==========================================
# 메인 함수
# ==========================================
def main():

    while True:

        teams = make_teams(students)

        print_teams(teams)

        answer = input("\n다시 추첨하시겠습니까? (Y/N) : ").strip().upper()

        if answer != "Y":
            print("\n프로그램을 종료합니다.")
            break


# ==========================================
# 프로그램 시작
# ==========================================
if __name__ == "__main__":
    main()