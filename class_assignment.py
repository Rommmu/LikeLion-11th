# 클래스 구현
class Student:
    def __init__(self, name, schoolNum, semester, subject):
        self.name = name
        self.schoolNum = schoolNum
        self.semester = semester
        self.subject = subject

    # 포매팅 사용해서 출력
    def print_name(self):
        print(f'이름은 {self.name}입니다.')
    
    # 문자열 슬라이싱 해서 학부 알아내야함 포매팅 사용해서 출력
    # 출력하면 안되고 리턴해야함
    def print_schoolNum(self):
        if (self.schoolNum[5:6] == '1'): return f"학번은 {self.schoolNum}로 인문융합자율학부 소속입니다."
        elif (self.schoolNum[5:6] == '2'): return f"학번은 {self.schoolNum}로 사회융합자율학부 소속입니다."
        elif (self.schoolNum[5:6] == '3'): return f"학번은 {self.schoolNum}로 미디어융합자율학부 소속입니다."
        elif (self.schoolNum[5:6] == '4'): return f"학번은 {self.schoolNum}로 아이티융합자율학부 소속입니다."
        else: return "오류입니다."

    # 입력받은 정수따라 출력 달리하기
    def print_semester(self):
        if (self.semester < 4 and self.semester >= 1):
            print(f'{self.semester}학기차인 {self.name}은 아직 전공선택 전입니다.')
        elif (self.semester >= 4):
            print(f'{self.name}은(는) {self.semester}학기차로 전공선택을 마쳤습니다.')
        else:
            print("오류입니다.")

    def print_subject(self):
        return f'{self.subject}를 수강합니다.'

def subject_info(**kwargs):
    print("자세한 수강목록입니다.")
    for key, value in kwargs.items():
        print(f'과목명: {key} / 과목명의 길이: {value}')

while True:
    Class_name = input("객체 명을 입력하시오. (단, 영문으로) : ")
    if (Class_name == "종료"):
        break
    name = input("이름을 입력하시오. (단, 한글로): ")
    schoolNum = input("학번을 입력하시오: ")
    semester = int(input("학기을 입력하시오. (단, 숫자로): "))
    
    # 빈 리스트와 딕셔너리 생성
    subjectList = []
    subjectDic = {}

    #세 과목 이상이라 최소 3개로 햇어용
    for i in range(3):
        subjectItem = input("과목을 입력하시오. : ")
        # 리스트에 추가
        subjectList.append(subjectItem)
        # 딕셔너리에 추가 key = 과목 : value = 과목 길이
        subjectDic[subjectItem] = len(subjectItem)
    
    # 인스턴스 생성
    Class_name = Student(name, schoolNum, semester, subjectList)
    # 가독성을 위한 한 줄
    # 이거 무조건 여기 있어야 함
    print()
    
    # 메서드 다 부르기
    Class_name.print_name()
    print(Class_name.print_schoolNum())
    Class_name.print_semester()
    print(Class_name.print_subject())
    # 가독성을 위한 한 줄
    ## 이거 무조건 여기 있어야 함
    print()
    # 딕셔너리 출력
    subject_info(**subjectDic)
    # 가독성을 위한 한 줄
    print()