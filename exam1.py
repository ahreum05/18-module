# 모듈 사용법 1
import my_module1
my_module1.my_func()
print('-' * 20)

# 모듈 사용법 2
import my_module1 as my
my.my_func()
print('-' * 20)

import numpy as np
import matplotlib.pyplot as plt

# 모듈 사용법 3
from my_module1 import my_func
my_func()
print('-' * 20)

# 모듈 사용법 4
# => 권장되지 않음
from my_module1 import my_func as my
my()
print('-' * 20)



