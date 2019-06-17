# Local
# Enclosing Function(내포한 함수)
# Global
# Bulit in

a = 1 # G
b = 300
# f()함수 내부의 b값을 없애면 g()함수에서 최종적으로 찾을 때 Global에서 탐색
def f():
    # b = 200
    # g()함수 내부의 b 값을 없애면 Local에서 찾을 수 없으므로 Enclosing에서 탐색
    def g():
        # b = 100
        # print(b)
        print(__name__) # Bulit in
    g()
    # print(b)
# print(a)
# print(b)

# main함수일때만 실행, 만일 다른 곳에서 사용한다고 하면 name은 legb로 나올테니
# 함수 실행하지 않음
if __name__ == '__main__':
    f()
