# 다른 프로젝트 디렉토리에 있는 module을 사용하기 위한 방법

# path를 추가하여 동적으로 import 실행하는 방식, python_modules는 modules이 생성되는 공간이다.
import sys
# sys.path.append('\cafe24\PycharmProjects\python_modules')
# 상대 경로로 지정
# sys.path.append('..\python_modules')
# 동적으로 진행되므로 문법 체크 시 에러가 발생함
import mymath

print(mymath.pi)
print(mymath.add(10, 20))
print(mymath.area_circle(10))

# pycharm 환경 변수로 설정하는 방법
'''
pycharm setting에서 project로 interpreter, show all, edit, python_modules 추가
'''

