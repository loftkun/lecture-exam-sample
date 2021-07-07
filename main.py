from Student import Student
from University import University

if __name__ == "__main__":
    u = University()
    a = Student(1000, 1000)

    # 試験を受ける
    a.math_score = u.JudgeMath(a.math_power)
    a.english_score = u.JudgeEnglish(a.english_power)

    # 合否判定
    a.grade = u.judgeFinal(a.math_score, a.english_score)