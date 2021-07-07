class Student():

    def __init__(self, math_power, english_power):
        self.math_power = math_power
        self.english_power = english_power
        self.math_score = None
        self.english_score = None
        self.grade = None
        print("[Student][init] power : math={} english={}".format(self.math_power, self.english_power))
