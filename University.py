class University():
    def __init__(self):
        print("[University][init] done")

    def JudgeMath(self, math_power):
        score = math_power * 0.1
        print("[University][JudgeMath] power={} score={}".format(math_power, score))
        return score

    def JudgeEnglish(self, english_power):
        score = english_power * 0.1
        print("[University][JudgeEnglish] power={} score={}".format(english_power, score))
        return score

    def judgeFinal(self, math, english):
        grade = None
        if math >= 100 and english >= 90:
            grade = "優"
        elif math >= 80 and english >= 60:
            grade = "良"
        else:
            grade = "不可"
        print("[University][judgeFinal] math={} english={} grade={}".format(math, english, grade))
        return grade