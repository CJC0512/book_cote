# 모든 출석번호를 담은 리스트
all_students = set(range(1, 31))

# 제출한 학생들의 출석번호를 입력받아 세트에 저장
# submitted_students = {1, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}

# 제출한 학생들의 출석번호를 입력받아 세트에 저장
submitted_students = set(int(input()) for _ in range(28))

# 제출하지 않은 학생들의 출석번호를 구함
missing_students = sorted(all_students - submitted_students)

# 결과 출력
print(missing_students[0])
print(missing_students[1])

