from m1 import module01
from m1.module01 import m1_fn2

from m2 import module02 as m2

import  module04 as al
import m3.module03 as m3
if __name__ == '__main__':
    module01.m1_fn1()
    m1_fn2()

    m2.m2_fn1()

    m3.m3_fn1()

