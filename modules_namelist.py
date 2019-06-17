import mod_a
import mod_b
import mymod
import mymod2
import sys

# module이름에 대한 key값이 나옴
for key in sys.modules.keys():
    print(key)