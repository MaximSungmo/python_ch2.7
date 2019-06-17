import mymod
import mymod2

# 중복되는 module 이 import 되어도 중복 import 하지 않는다.

print(mymod.add(10, 20))
print(mymod.subtract(10, 20))
print(mymod.multiply(10, 20))
print(mymod.divide(10, 20))
print(mymod2.power(10, 20))
