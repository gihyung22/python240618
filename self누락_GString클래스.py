# 전역변수
strName = "Not Class Member"

class DemoString:
    def __init__(self):
        # 멤버변수
        self.strName = "" 
    def set(self, msg):
        self.strName = msg
    def print(self):
        # 파이썬은 모호한 것보다 명시적인 것이 좋다. self.strName 인데  self 누락시에는 어떻게 될까?
        print(strName)

# 인스턴스를 생성
d = DemoString()
d.set("First Message")
d.print()
