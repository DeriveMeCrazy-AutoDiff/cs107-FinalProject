import pytest

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


#import auto_diff_pkg.AutoDiff as AutoDiff
from auto_diff_pkg.AutoDiff import AutoDiff, sqrt, sin, cos, exp, log, tan, arcsin, arccos, arctan, sinh, cosh, tanh, logistic, jacobian

epsilon = 10**(-12)

def test_init_int_zero():    
    x0 = AutoDiff(0)
    assert x0.val == 0 and x0.der == 1

def test_init_float():    
    x0 = AutoDiff(0.0)
    assert x0.val == 0.0 and x0.der == 1
    
def test_init_None():
    x0 = AutoDiff(None)
    with pytest.raises(TypeError):
        x0 + 5

def test_add_int():    
    x0 = AutoDiff(0)
    curr_func = x0+5
    assert curr_func.val == 5 and curr_func.der == 1

def test_radd_int():    
    x0 = AutoDiff(0)
    curr_func = 5 + x0
    assert curr_func.val == 5 and curr_func.der == 1

def test_add_float(): 
    x0 = AutoDiff(0.0)
    curr_func = x0+5.0
    assert curr_func.val == 5.0 and curr_func.der == 1

def test_radd_float(): 
    x0 = AutoDiff(0.0)
    curr_func = x0+5.0
    assert curr_func.val == 5.0 and curr_func.der == 1
    
def test_add_AutoDiff():    
    x0 = AutoDiff(5)
    curr_func = (x0+6.3)+x0
    assert curr_func.val == 16.3 and curr_func.der == 2

def test_sub():    
    x0 = AutoDiff(0)
    curr_func = x0-5
    assert curr_func.val == -5.0 and curr_func.der == 1

def test_rsub():    
    x0 = AutoDiff(0)
    curr_func = 5 - x0
    assert curr_func.val == 5.0 and curr_func.der == -1
    
def test_sub_AutoDiff():    
    x0 = AutoDiff(5)
    curr_func = (x0+6.3) - x0
    assert abs(curr_func.val - 6.3) < epsilon and curr_func.der == 0

def test_rsub_AutoDiff():    
    x0 = AutoDiff(5)
    curr_func = x0 - (x0+6.3)  
    assert abs(curr_func.val - -6.3) < epsilon and curr_func.der == 0

def test_mul_1():    
    x0 = AutoDiff(1)
    curr_func = x0*5
    assert curr_func.val == 5.0 and curr_func.der == 5

def test_mul_0():    
    x0 = AutoDiff(0)
    curr_func = x0 * 5
    assert curr_func.val == 0.0 and curr_func.der == 5
   
def test_rmul():    
    x0 = AutoDiff(-3)
    curr_func = 5 * x0
    assert curr_func.val == -15.0 and curr_func.der == 5
    
def test_mul_AutoDiff():    
    x0 = AutoDiff(5)
    curr_func = (x0+6.3) * x0
    assert curr_func.val == 56.5 and curr_func.der == 16.3

def test_div_1():    
    x0 = AutoDiff(1)
    curr_func = x0/5
    assert curr_func.val == 0.2 and curr_func.der == 0.2

def test_div_0():    
    x0 = AutoDiff(0)
    curr_func = x0 / 5
    assert curr_func.val == 0.0 and curr_func.der == 0.2
   
def test_rdiv():    
    x0 = AutoDiff(-2)
    curr_func = 6 / x0
    
    assert curr_func.val == -3.0 and curr_func.der == -6/4
    
def test_div_AutoDiff():    
    x0 = AutoDiff(5)
    curr_func = (x0+6.3) / x0
    assert abs(curr_func.val - 2.2600000000000002) < epsilon and curr_func.der == -0.252

def test_pow_0():    
    x0 = AutoDiff(2)
    curr_func = x0**0
    assert curr_func.val == 1.0 and curr_func.der == 0.0

def test_pow_neg():    
    x0 = AutoDiff(4)
    curr_func = x0**-1
    assert curr_func.val == 0.25 and curr_func.der == -1/16

def test_pow():    
    x0 = AutoDiff(4)
    curr_func = x0 ** 2
    assert curr_func.val == 16.0 and curr_func.der == 8.0

def test_pow_frac():    
    x0 = AutoDiff(4)
    curr_func = x0 ** 0.5
    assert curr_func.val == 2.0 and curr_func.der == 0.25
   
def test_rpow():    
    x0 = AutoDiff(2)
    curr_func = 6 ** x0
    assert curr_func.val == 36 and curr_func.der == 64.50334089220998
    
def test_pow_AutoDiff():    
    x0 = AutoDiff(3)
    curr_func = (x0 ** 2) ** x0
    assert curr_func.val == 729 and curr_func.der == 3059.776716878104

def test_log():    
    curr_func = log(2)
    assert curr_func == 0.6931471805599453

# def test_log_neg():
#     x0 = AutoDiff(-4)
#     with pytest.raises(ValueError):
#         curr_func = log(x0)

def test_log_frac():    
    curr_func = log(0.5)
    assert curr_func == -0.6931471805599453
       
def test_log_AutoDiff():    
    x0 = AutoDiff(10)
    curr_func = log(x0 ** 2)
    assert curr_func.val == 4.605170185988092 and curr_func.der == 0.2

def test_exp_frac():    
    curr_func = exp(0.5)
    assert curr_func == 1.6487212707001282

def test_exp_int():    
    curr_func = exp(5)
    assert curr_func == 148.4131591025766
       
def test_exp_AutoDiff():    
    x0 = AutoDiff(2)
    curr_func = exp(x0 ** 2)
    assert curr_func.val == 54.598150033144236 and curr_func.der == 218.39260013257694

def test_sin_frac():    
    curr_func = sin(0.5)
    assert curr_func == 0.479425538604203

def test_sin_int():    
    curr_func = sin(5)
    assert curr_func == -0.9589242746631385

def test_sin_AutoDiff():    
    x0 = AutoDiff(2)
    curr_func = sin(x0 ** 2)
    assert curr_func.val == -0.7568024953079282 and curr_func.der == -2.6145744834544478

def test_cos_frac():    
    curr_func = cos(0.5)
    assert curr_func == 0.8775825618903728

def test_cos_int():    
    curr_func = cos(5)
    assert abs(curr_func - 0.2836621854632263) < epsilon
       
def test_cos_AutoDiff():    
    x0 = AutoDiff(2)
    curr_func = cos(x0 ** 2)
    assert curr_func.val == -0.6536436208636119 and curr_func.der == 3.027209981231713

def test_tan_frac():    
    curr_func = tan(0.5)
    assert abs(curr_func - 0.5463024898437905) < epsilon

def test_tan_int():    
    curr_func = tan(-5)
    assert abs(curr_func - 3.380515006246585) < epsilon
       
def test_tan_AutoDiff():    
    x0 = AutoDiff(2)
    curr_func = tan(x0 ** 2)
    assert curr_func.val == 1.1578212823495775 and curr_func.der == 9.36220048744648

def test_sqrt_frac():    
    curr_func = sqrt(0.5)
    assert curr_func == 0.7071067811865476

# def test_sqrt_neg():
#     with pytest.raises(ValueError):
#         curr_func = sqrt(-5)

def test_sqrt_int():    
    curr_func = sqrt(5)
    assert curr_func == 2.23606797749979
       
def test_sqrt_AutoDiff():    
    x0 = AutoDiff(2)
    curr_func = sqrt(x0 + 6)
    assert curr_func.val == 2.8284271247461903 and curr_func.der == 0.17677669529663687

# ---- updated: arcsin, arccos, arctan, sinh, cosh, tanh, logistic, jacobian

def test_arcsin_frac():
    curr_func = arcsin(0.5)
    assert abs(curr_func - 0.5235987755982988) < epsilon

def test_arcsin_int():
    curr_func = arcsin(1)
    assert abs(curr_func - 1.5707963267948966) < epsilon

# def test_arcsin_outside_one():
#     with pytest.raises(ValueError):
#         curr_func = arcsin(2)

def test_arcsin_AutoDiff():
    x0 = AutoDiff(0.8)
    curr_func = arcsin(x0 ** 2)
    assert curr_func.val == 0.6944982656265561 and curr_func.der == 2.082316825181415

def test_arccos_frac():
    curr_func = arccos(0.5)
    assert abs(curr_func - 1.0471975511965976) < epsilon

def test_arccos_int():
    curr_func = arccos(-1)
    assert abs(curr_func - 3.141592653589793) < epsilon

# def test_arccos_outside_one():
#     with pytest.raises(ValueError):
#         curr_func = arccos(2)

def test_arccos_AutoDiff():
    x0 = AutoDiff(0.8)
    curr_func = arccos(x0 ** 2)
    assert curr_func.val == 0.8762980611683404 and curr_func.der == -2.082316825181415

def test_arctan_frac():
    curr_func = arctan(0.5)
    assert abs(curr_func - 0.46364760900080615) < epsilon

def test_arctan_int():
    curr_func = arctan(1)
    assert abs(curr_func - 0.7853981633974483) < epsilon

# def test_arctan_outside_half_pi():
#     with pytest.raises(ValueError):
#         curr_func = arctan(2)

def test_arctan_AutoDiff():
    x0 = AutoDiff(0.8)
    curr_func = arctan(x0 ** 2)
    assert curr_func.val == 0.5693131911006619 and curr_func.der == 1.1350737797956867

def test_sinh_frac():
    curr_func = sinh(0.5)
    assert abs(curr_func - 0.5210953054937474) < epsilon

def test_sinh_int():
    curr_func = sinh(5)
    assert abs(curr_func - 74.20321057778875) < epsilon

def test_sinh_AutoDiff():
    x0 = AutoDiff(0.8)
    curr_func = sinh(x0 ** 2)
    assert curr_func.val == 0.6845942276309516 and curr_func.der == 1.9390186426784002

def test_cosh_frac():
    curr_func = cosh(0.5)
    assert abs(curr_func - 1.1276259652063807) < epsilon

def test_cosh_int():
    curr_func = cosh(5)
    assert abs(curr_func - 74.20994852478785) < epsilon

def test_cosh_AutoDiff():
    x0 = AutoDiff(0.8)
    curr_func = cosh(x0 ** 2)
    assert curr_func.val == 1.2118866516740001 and curr_func.der == 1.0953507642095226

def test_tanh_frac():
    curr_func = tanh(0.5)
    assert abs(curr_func - 0.46211715726000974) < epsilon

def test_tanh_int():
    curr_func = tanh(5)
    assert abs(curr_func - 0.9999092042625951) < epsilon

def test_tanh_AutoDiff():
    x0 = AutoDiff(0.8)
    curr_func = tanh(x0 ** 2)
    assert curr_func.val == 0.5648995528462251 and curr_func.der == 1.089421592310616

def test_logistic_frac():
    curr_func = logistic(0.5)
    assert abs(curr_func - 0.6224593312018546) < epsilon

def test_logistic_int():
    curr_func = logistic(5)
    assert abs(curr_func - 0.9933071490757153) < epsilon

def test_logistic_AutoDiff():
    x0 = AutoDiff(0.8)
    curr_func = logistic(x0 ** 2)
    assert curr_func.val == 0.6547534606063192 and curr_func.der == 0.36168218628858945

def test_jacobian_frac():
    values = [0.1, 0.2, 0.4]
    def f1(x0, x1, x2):
        return (x0 + x1 + x2)
    def f2(x0, x1, x2):
        return (1 * x0 + 2 * x1 + 3 * x2)
    def f3(x0, x1, x2):
        return (1 * x0 * 2 * x1 * 3 * x2)
    def f4(x0, x1, x2):
        return (x0 ** 2 + x1 ** 3 + x2 ** 4)
    def f5(x0, x1, x2):
        return (sin(x0) + cos(x1) + tan(x2))
    functions = [f1, f2, f3, f4, f5]
    assert list(jacobian(values, functions)[0]) == [1, 1, 1]
    assert list(jacobian(values, functions)[1]) == [1, 2, 3]
    assert abs(jacobian(values, functions)[2][0] - 0.48)<epsilon and abs(jacobian(values, functions)[2][1] - 0.24)<epsilon and abs(jacobian(values, functions)[2][2] - 0.12)<epsilon
    assert abs(jacobian(values, functions)[3][0] - 0.2) < epsilon and abs(jacobian(values, functions)[3][1] - 0.12) < epsilon and abs(jacobian(values, functions)[3][2] - 0.256) < epsilon
    #assert list(jacobian(values, functions)[3]) == [0.2, 0.12, 0.256]
    assert abs(jacobian(values, functions)[4][0] - 0.9950041652780257) < epsilon and abs(jacobian(values, functions)[4][1] - -0.19866933079506122) < epsilon and abs(jacobian(values, functions)[4][2] - 1.178754105810975) < epsilon
    #assert list(jacobian(values, functions)[4]) == [0.9950041652780257, -0.19866933079506122, 1.178754105810975]

def test_jacobian_int():
    values = [1, 2, 4]
    def f1(x0, x1, x2):
        return (x0 + x1 + x2)
    def f2(x0, x1, x2):
        return (1 * x0 + 2 * x1 + 3 * x2)
    def f3(x0, x1, x2):
        return (1 * x0 * 2 * x1 * 3 * x2)
    def f4(x0, x1, x2):
        return (x0 ** 2 + x1 ** 3 + x2 ** 4)
    def f5(x0, x1, x2):
        return (sin(x0) + cos(x1) + tan(x2))
    functions = [f1, f2, f3, f4, f5]
    assert list(jacobian(values, functions)[0]) == [1, 1, 1]
    assert list(jacobian(values, functions)[1]) == [1, 2, 3]
    assert list(jacobian(values, functions)[2]) == [48, 24, 12]
    assert list(jacobian(values, functions)[3]) == [2, 12, 256]
    assert list(jacobian(values, functions)[4]) == [0.5403023058681398, -0.9092974268256817, 2.34055012186162]

# --- updated: vectors

def test_add_vector():
    a = [1, 2, 3]
    b = [0.5, 0.2, 0.1]
    c = [2, 4, 6]
    d = [0.3, 0.6, 0.9]

    x0 = AutoDiff(a, 1, 4, 0)
    x1 = AutoDiff(b, 1, 4, 1)
    x2 = AutoDiff(c, 1, 4, 2)
    x3 = AutoDiff(d, 1, 4, 3)

    f0 = x0 + 1  # testing add int
    f1 = 0.5 + x0  # testing radd frac
    f2 = x0 + x1  # testing AutoDiff
    f3 = x0 + x1 + x2 + x3  # testing 4 var
    F = [f0, f1, f2, f3]

    assert F[0].val[0][0] == 2 and F[0].val[1][0] == 3 and F[0].val[2][0] == 4
    assert F[1].val[0][0] == 1.5 and F[1].val[1][0] == 2.5 and F[1].val[2][0] == 3.5
    assert F[2].val[0][0] == 1.5 and F[2].val[1][0] == 2.2 and F[2].val[2][0] == 3.1
    assert F[3].val[0][0] == 3.8 and F[3].val[1][0] == 6.8 and F[3].val[2][0] == 10

    # der: len_val x num_var
    assert F[0].der[0][0] == 1 and F[0].der[0][1] == 0 and F[0].der[0][2] == 0 and F[0].der[0][3] == 0
    assert F[0].der[1][0] == 1 and F[0].der[1][1] == 0 and F[0].der[1][2] == 0 and F[0].der[1][3] == 0
    assert F[0].der[2][0] == 1 and F[0].der[2][1] == 0 and F[0].der[2][2] == 0 and F[0].der[2][3] == 0

    assert F[1].der[0][0] == 1 and F[1].der[0][1] == 0 and F[1].der[0][2] == 0 and F[1].der[0][3] == 0
    assert F[1].der[1][0] == 1 and F[1].der[1][1] == 0 and F[1].der[1][2] == 0 and F[1].der[1][3] == 0
    assert F[1].der[2][0] == 1 and F[1].der[2][1] == 0 and F[1].der[2][2] == 0 and F[1].der[2][3] == 0

    assert F[2].der[0][0] == 1 and F[2].der[0][1] == 1 and F[2].der[0][2] == 0 and F[2].der[0][3] == 0
    assert F[2].der[1][0] == 1 and F[2].der[1][1] == 1 and F[2].der[1][2] == 0 and F[2].der[1][3] == 0
    assert F[2].der[2][0] == 1 and F[2].der[2][1] == 1 and F[2].der[2][2] == 0 and F[2].der[2][3] == 0

    assert F[3].der[0][0] == 1 and F[3].der[0][1] == 1 and F[3].der[0][2] == 1 and F[3].der[0][3] == 1
    assert F[3].der[1][0] == 1 and F[3].der[1][1] == 1 and F[3].der[1][2] == 1 and F[3].der[1][3] == 1
    assert F[3].der[2][0] == 1 and F[3].der[2][1] == 1 and F[3].der[2][2] == 1 and F[3].der[2][3] == 1

def test_sub_vector():
    a = [1, 2, 3]
    b = [0.5, 0.2, 0.1]
    c = [2, 4, 6]
    d = [0.3, 0.6, 0.9]

    x0 = AutoDiff(a, 1, 4, 0)
    x1 = AutoDiff(b, 1, 4, 1)
    x2 = AutoDiff(c, 1, 4, 2)
    x3 = AutoDiff(d, 1, 4, 3)

    f0 = x0 - 1  # testing sub int
    f1 = 0.5 - x0  # testing rsub frac
    f2 = x0 - x1  # testing AutoDiff
    f3 = x0 - x1 - x2 - x3  # testing 4 var
    F = [f0, f1, f2, f3]

    assert F[0].val[0][0] == 0 and F[0].val[1][0] == 1 and F[0].val[2][0] == 2
    assert F[1].val[0][0] == -0.5 and F[1].val[1][0] == -1.5 and F[1].val[2][0] == -2.5
    assert F[2].val[0][0] == 0.5 and F[2].val[1][0] == 1.8 and F[2].val[2][0] == 2.9
    assert F[3].val[0][0] == -1.8 and abs(F[3].val[1][0] - (-2.8)) < epsilon and F[3].val[2][0] == -4

    # der: len_val x num_var
    assert F[0].der[0][0] == 1 and F[0].der[0][1] == 0 and F[0].der[0][2] == 0 and F[0].der[0][3] == 0
    assert F[0].der[1][0] == 1 and F[0].der[1][1] == 0 and F[0].der[1][2] == 0 and F[0].der[1][3] == 0
    assert F[0].der[2][0] == 1 and F[0].der[2][1] == 0 and F[0].der[2][2] == 0 and F[0].der[2][3] == 0

    assert F[1].der[0][0] == -1 and F[1].der[0][1] == 0 and F[1].der[0][2] == 0 and F[1].der[0][3] == 0
    assert F[1].der[1][0] == -1 and F[1].der[1][1] == 0 and F[1].der[1][2] == 0 and F[1].der[1][3] == 0
    assert F[1].der[2][0] == -1 and F[1].der[2][1] == 0 and F[1].der[2][2] == 0 and F[1].der[2][3] == 0

    assert F[2].der[0][0] == 1 and F[2].der[0][1] == -1 and F[2].der[0][2] == 0 and F[2].der[0][3] == 0
    assert F[2].der[1][0] == 1 and F[2].der[1][1] == -1 and F[2].der[1][2] == 0 and F[2].der[1][3] == 0
    assert F[2].der[2][0] == 1 and F[2].der[2][1] == -1 and F[2].der[2][2] == 0 and F[2].der[2][3] == 0

    assert F[3].der[0][0] == 1 and F[3].der[0][1] == -1 and F[3].der[0][2] == -1 and F[3].der[0][3] == -1
    assert F[3].der[1][0] == 1 and F[3].der[1][1] == -1 and F[3].der[1][2] == -1 and F[3].der[1][3] == -1
    assert F[3].der[2][0] == 1 and F[3].der[2][1] == -1 and F[3].der[2][2] == -1 and F[3].der[2][3] == -1

def test_mul_vector():
    a = [1, 2, 3]
    b = [0.5, 0.2, 0.1]
    c = [2, 4, 6]
    d = [0.3, 0.6, 0.9]

    x0 = AutoDiff(a, 1, 4, 0)
    x1 = AutoDiff(b, 1, 4, 1)
    x2 = AutoDiff(c, 1, 4, 2)
    x3 = AutoDiff(d, 1, 4, 3)

    f0 = x0 * 3  # testing mul int
    f1 = 0.5 * x0  # testing rmul frac
    f2 = x0 * x1  # testing AutoDiff
    f3 = x0 * x1 * x2 * x3  # testing 4 var
    F = [f0, f1, f2, f3]

    assert F[0].val[0][0] == 3 and F[0].val[1][0] == 6 and F[0].val[2][0] == 9
    assert F[1].val[0][0] == 0.5 and F[1].val[1][0] == 1 and F[1].val[2][0] == 1.5
    assert F[2].val[0][0] == 0.5 and F[2].val[1][0] == 0.4 and abs(F[2].val[2][0] - 0.3) < epsilon
    assert F[3].val[0][0] == 0.3 and F[3].val[1][0] == 0.96 and abs(F[3].val[2][0] - 1.62) < epsilon

    # der: len_val x num_var
    assert F[0].der[0][0] == 3 and F[0].der[0][1] == 0 and F[0].der[0][2] == 0 and F[0].der[0][3] == 0
    assert F[0].der[1][0] == 3 and F[0].der[1][1] == 0 and F[0].der[1][2] == 0 and F[0].der[1][3] == 0
    assert F[0].der[2][0] == 3 and F[0].der[2][1] == 0 and F[0].der[2][2] == 0 and F[0].der[2][3] == 0

    assert F[1].der[0][0] == 0.5 and F[1].der[0][1] == 0 and F[1].der[0][2] == 0 and F[1].der[0][3] == 0
    assert F[1].der[1][0] == 0.5 and F[1].der[1][1] == 0 and F[1].der[1][2] == 0 and F[1].der[1][3] == 0
    assert F[1].der[2][0] == 0.5 and F[1].der[2][1] == 0 and F[1].der[2][2] == 0 and F[1].der[2][3] == 0

    assert F[2].der[0][0] == 0.5 and F[2].der[0][1] == 1 and F[2].der[0][2] == 0 and F[2].der[0][3] == 0
    assert F[2].der[1][0] == 0.2 and F[2].der[1][1] == 2 and F[2].der[1][2] == 0 and F[2].der[1][3] == 0
    assert F[2].der[2][0] == 0.1 and F[2].der[2][1] == 3 and F[2].der[2][2] == 0 and F[2].der[2][3] == 0

    assert F[3].der[0][0] == 0.3 and F[3].der[0][1] == 0.6 and F[3].der[0][2] == 0.15 and F[3].der[0][3] == 1
    assert F[3].der[1][0] == 0.48 and F[3].der[1][1] == 4.8 and F[3].der[1][2] == 0.24 and F[3].der[1][3] == 1.6
    assert abs(F[3].der[2][0] - 0.54)<epsilon and abs(F[3].der[2][1] - 16.2)<epsilon and abs(F[3].der[2][2] - 0.27)<epsilon and abs(F[3].der[2][3] - 1.8)<epsilon

def test_div_vector():
    a = [1, 2, 3]
    b = [0.5, 0.2, 0.1]
    c = [2, 4, 6]
    d = [0.3, 0.6, 0.9]

    x0 = AutoDiff(a, 1, 4, 0)
    x1 = AutoDiff(b, 1, 4, 1)
    x2 = AutoDiff(c, 1, 4, 2)
    x3 = AutoDiff(d, 1, 4, 3)

    f0 = x0 / 3  # testing div int
    f1 = 0.5 / x0  # testing rdiv frac
    f2 = x0 / x1  # testing AutoDiff
    f3 = x0 / x1 / x2 / x3  # testing 4 var
    F = [f0, f1, f2, f3]

    assert F[0].val[0][0] == 0.33333333333333333 and F[0].val[1][0] == 0.6666666666666666 and F[0].val[2][0] == 1
    assert F[1].val[0][0] == 0.5 and F[1].val[1][0] == 0.25 and F[1].val[2][0] == 0.16666666666666666
    assert F[2].val[0][0] == 2 and F[2].val[1][0] == 10 and F[2].val[2][0] == 30
    assert F[3].val[0][0] == 3.33333333333333333 and F[3].val[1][0] == 4.1666666666666666 and F[3].val[2][0] == 5.555555555555555

    # der: len_val x num_var
    assert F[0].der[0][0] == 0.33333333333333333 and F[0].der[0][1] == 0 and F[0].der[0][2] == 0 and F[0].der[0][3] == 0
    assert F[0].der[1][0] == 0.33333333333333333 and F[0].der[1][1] == 0 and F[0].der[1][2] == 0 and F[0].der[1][3] == 0
    assert F[0].der[2][0] == 0.33333333333333333 and F[0].der[2][1] == 0 and F[0].der[2][2] == 0 and F[0].der[2][3] == 0

    assert F[1].der[0][0] == -0.5 and F[1].der[0][1] == 0 and F[1].der[0][2] == 0 and F[1].der[0][3] == 0
    assert F[1].der[1][0] == -0.125 and F[1].der[1][1] == 0 and F[1].der[1][2] == 0 and F[1].der[1][3] == 0
    assert F[1].der[2][0] == -0.05555555555555555 and F[1].der[2][1] == 0 and F[1].der[2][2] == 0 and F[1].der[2][3] == 0

    assert F[2].der[0][0] == 2 and F[2].der[0][1] == -4 and F[2].der[0][2] == 0 and F[2].der[0][3] == 0
    assert abs(F[2].der[1][0] - 5)<epsilon and abs(F[2].der[1][1] - -50)<epsilon and F[2].der[1][2] == 0 and F[2].der[1][3] == 0
    assert abs(F[2].der[2][0] - 10)<epsilon and abs(F[2].der[2][1] - -300)<epsilon and F[2].der[2][2] == 0 and F[2].der[2][3] == 0

    assert abs(F[3].der[0][0] - 3.33333333333333333)<epsilon and abs(F[3].der[0][1] - -6.6666666666666666)<epsilon and abs(F[3].der[0][2] - -1.66666666666666666)<epsilon and abs(F[3].der[0][3] - -11.11111111111111)<epsilon
    assert abs(F[3].der[1][0] - 2.08333333333333333)<epsilon and abs(F[3].der[1][1] - -20.833333333333333)<epsilon and abs(F[3].der[1][2] - -1.04166666666666666)<epsilon and abs(F[3].der[1][3] - -6.9444444444444444)<epsilon
    assert abs(F[3].der[2][0] - 1.8518518518518519)<epsilon and abs(F[3].der[2][1] - -55.555555555555555)<epsilon and abs(F[3].der[2][2] - -0.925925925925926)<epsilon and abs(F[3].der[2][3] - -6.172839506172839)<epsilon

def test_pow_vector():
    a = [1, 2, 3]
    b = [0.5, 0.2, 0.1]
    c = [2, 4, 6]
    d = [0.3, 0.6, 0.9]

    x0 = AutoDiff(a, 1, 4, 0)
    x1 = AutoDiff(b, 1, 4, 1)
    x2 = AutoDiff(c, 1, 4, 2)
    x3 = AutoDiff(d, 1, 4, 3)

    f0 = x0 ** 2  # testing pow int
    f1 = 0.5 ** x0  # testing rpow frac
    f2 = x0 ** x1  # testing AutoDiff
    f3 = x0 ** x1 ** x2 ** x3  # testing 4 var
    F = [f0, f1, f2, f3]

    assert F[0].val[0][0] == 1 and F[0].val[1][0] == 4 and F[0].val[2][0] == 9
    assert F[1].val[0][0] == 0.5 and F[1].val[1][0] == 0.25 and F[1].val[2][0] == 0.125
    assert F[2].val[0][0] == 1 and F[2].val[1][0] == 1.148698354997035 and F[2].val[2][0] == 1.1161231740339044
    assert F[3].val[0][0] == 1 and F[3].val[1][0] == 1.0173280592778047 and F[3].val[2][0] == 1.0000105948287346

    # der: len_val x num_var
    assert F[0].der[0][0] == 2 and F[0].der[0][1] == 0 and F[0].der[0][2] == 0 and F[0].der[0][3] == 0
    assert F[0].der[1][0] == 4 and F[0].der[1][1] == 0 and F[0].der[1][2] == 0 and F[0].der[1][3] == 0
    assert F[0].der[2][0] == 6 and F[0].der[2][1] == 0 and F[0].der[2][2] == 0 and F[0].der[2][3] == 0

    assert F[1].der[0][0] == -0.34657359027997264 and F[1].der[0][1] == 0 and F[1].der[0][2] == 0 and F[1].der[0][3] == 0
    assert F[1].der[1][0] == -0.17328679513998632 and F[1].der[1][1] == 0 and F[1].der[1][2] == 0 and F[1].der[1][3] == 0
    assert F[1].der[2][0] == -0.08664339756999316 and F[1].der[2][1] == 0 and F[1].der[2][2] == 0 and F[1].der[2][3] == 0

    assert F[2].der[0][0] == 0.5 and F[2].der[0][1] == 0 and F[2].der[0][2] == 0 and F[2].der[0][3] == 0
    assert F[2].der[1][0] == 0.11486983549970349 and F[2].der[1][1] == 0.796217026080042 and F[2].der[1][2] == 0 and F[2].der[1][3] == 0
    assert F[2].der[2][0] == 0.03720410580113015 and F[2].der[2][1] == 1.2261866346609027 and F[2].der[2][2] == 0 and F[2].der[2][3] == 0

    assert F[3].der[0][0] == 0.4259794049913497 and F[3].der[0][1] == 0 and F[3].der[0][2] == 0 and F[3].der[0][3] == 0
    assert F[3].der[1][0] == 0.012607228929462063 and F[3].der[1][1] == 0.20076180650653108 and F[3].der[1][2] == -0.009693409882811104 and F[3].der[1][3] == -0.08958612973709902
    assert F[3].der[2][0] == 3.214626600233811e-06 and F[3].der[2][1] == 0.0005314132353175134 and abs(F[3].der[2][2] - (-1.8354362907927648e-05))<epsilon and F[3].der[2][3] == -0.00021924402361285026

def test_arcsin_vector():
    a = [1, 2, 3]
    b = [0.5, 0.2, 0.1]

    x0 = AutoDiff(a, 1, 2, 0)
    x1 = AutoDiff(b, 1, 2, 1)

    f0 = arcsin((x0 + x1)/4)
    f1 = arcsin(x0**2 * x1)
    F = [f0, f1]

    assert F[0].val[0][0] == 0.3843967744956391 and F[0].val[1][0] == 0.5823642378687435 and F[0].val[2][0] == 0.8867150949995675
    assert abs(F[1].val[0][0] - 0.5235987755982988)<epsilon and F[1].val[1][0] == 0.9272952180016123 and F[1].val[2][0] == 1.1197695149986342
    # der: len_val x num_var
    assert F[0].der[0][0] == 0.26967994498529685 and F[0].der[0][1] == 0.26967994498529685
    assert F[0].der[1][0] == 0.2993421700446248 and F[0].der[1][1] == 0.2993421700446248
    assert F[0].der[2][0] == 0.3955938860646178 and F[0].der[2][1] == 0.3955938860646178

    assert F[1].der[0][0] == 1.1547005383792517 and F[1].der[0][1] == 1.1547005383792517
    assert F[1].der[1][0] == 1.3333333333333337 and F[1].der[1][1] == 6.666666666666668
    assert abs(F[1].der[2][0] - 1.3764944032233708)<epsilon and F[1].der[2][1] == 20.647416048350564  # print((9)/(np.sqrt(1-(0.9)**2)))

def test_arccos_vector():
    a = [1, 2, 3]
    b = [0.5, 0.2, 0.1]

    x0 = AutoDiff(a, 1, 2, 0)
    x1 = AutoDiff(b, 1, 2, 1)

    f0 = arccos((x0 + x1)/4)
    f1 = arccos(x0**2 * x1)
    F = [f0, f1]

    assert abs(F[0].val[0][0] - 1.1863995522992574)<epsilon and F[0].val[1][0] == 0.9884320889261531 and F[0].val[2][0] == 0.6840812317953292
    assert abs(F[1].val[0][0] - 1.0471975511965976)<epsilon and F[1].val[1][0] == 0.6435011087932843 and F[1].val[2][0] == 0.45102681179626236
    # der: len_val x num_var
    assert F[0].der[0][0] == -0.26967994498529685 and F[0].der[0][1] == -0.26967994498529685
    assert F[0].der[1][0] == -0.2993421700446248 and F[0].der[1][1] == -0.2993421700446248
    assert F[0].der[2][0] == -0.3955938860646178 and F[0].der[2][1] == -0.3955938860646178

    assert F[1].der[0][0] == -1.1547005383792517 and F[1].der[0][1] == -1.1547005383792517
    assert F[1].der[1][0] == -1.3333333333333337 and F[1].der[1][1] == -6.666666666666668
    assert F[1].der[2][0] == -1.376494403223371 and F[1].der[2][1] == -20.647416048350564

def test_arctan_vector():
    a = [1, 2, 3]
    b = [0.5, 0.2, 0.1]

    x0 = AutoDiff(a, 1, 2, 0)
    x1 = AutoDiff(b, 1, 2, 1)

    f0 = arctan((x0 + x1)/4)
    f1 = arctan(x0**2 * x1)
    F = [f0, f1]

    assert F[0].val[0][0] == 0.35877067027057225 and F[0].val[1][0] == 0.5028432109278609 and F[0].val[2][0] == 0.6593100683328579
    assert abs(F[1].val[0][0] - 0.46364760900080615)<epsilon and F[1].val[1][0] == 0.6747409422235527 and abs(F[1].val[2][0] - 0.7328151017865067)<epsilon
    # der: len_val x num_var
    assert F[0].der[0][0] == 0.2191780821917808 and F[0].der[0][1] == 0.2191780821917808
    assert F[0].der[1][0] == 0.19193857965451055 and F[0].der[1][1] == 0.19193857965451055
    assert F[0].der[2][0] == 0.15618898867629832 and F[0].der[2][1] == 0.15618898867629832

    assert F[1].der[0][0] == 0.8 and F[1].der[0][1] == 0.8
    assert F[1].der[1][0] == 0.4878048780487805 and F[1].der[1][1] == 2.4390243902439024
    assert F[1].der[2][0] == 0.33149171270718236 and F[1].der[2][1] == 4.972375690607735

def test_logistic_vector():
    a = [1, 2, 3]
    b = [0.5, 0.2, 0.1]

    x0 = AutoDiff(a, 1, 2, 0)
    x1 = AutoDiff(b, 1, 2, 1)

    f0 = logistic((x0 + x1)/4)
    f1 = logistic(x0**2 * x1)
    F = [f0, f1]

    assert F[0].val[0][0] == 0.5926665999540697 and F[0].val[1][0] == 0.6341355910108007 and F[0].val[2][0] == 0.6846015003234307
    assert F[1].val[0][0] == 0.6224593312018546 and F[1].val[1][0] == 0.6899744811276125 and F[1].val[2][0] == 0.7109495026250039
    # der: len_val x num_var
    assert abs(F[0].der[0][0] - 0.060353225313238106)<epsilon and abs(F[0].der[0][1] - 0.060353225313238106)<epsilon
    assert abs(F[0].der[1][0] - 0.058001910806045796)<epsilon and abs(F[0].der[1][1] - 0.058001910806045796)<epsilon
    assert abs(F[0].der[2][0] - 0.0539805715195846)<epsilon and abs(F[0].der[2][1] - 0.0539805715195846)<epsilon

    assert abs(F[1].der[0][0] - 0.2350037122015945)<epsilon and abs(F[1].der[0][1] - 0.2350037122015945)<epsilon
    assert abs(F[1].der[1][0] - 0.17112775721623552)<epsilon and abs(F[1].der[1][1] - 0.8556387860811776)<epsilon
    assert abs(F[1].der[2][0] - 0.1233001844053581)<epsilon and abs(F[1].der[2][1] - 1.8495027660803713)<epsilon

def test_sin_vector():
    a = [1, 2, 3]
    b = [0.5, 0.2, 0.1]

    x0 = AutoDiff(a, 1, 2, 0)
    x1 = AutoDiff(b, 1, 2, 1)

    f0 = sin((x0 + x1)/4)
    f1 = sin(x0**2 * x1)
    F = [f0, f1]

    assert F[0].val[0][0] == 0.36627252908604757 and F[0].val[1][0] == 0.5226872289306592 and F[0].val[2][0] == 0.6997160753466035
    assert F[1].val[0][0] == 0.479425538604203 and F[1].val[1][0] == 0.7173560908995228 and abs(F[1].val[2][0] - 0.7833269096274833)<epsilon
    # der: len_val x num_var
    assert F[0].der[0][0] == 0.23262690547807857 and F[0].der[0][1] == 0.23262690547807857
    assert F[0].der[1][0] == 0.21313113051487642 and F[0].der[1][1] == 0.21313113051487642
    assert F[0].der[2][0] == 0.17860525851398285 and F[0].der[2][1] == 0.17860525851398285

    assert F[1].der[0][0] == 0.8775825618903728 and F[1].der[0][1] == 0.8775825618903728
    assert abs(F[1].der[1][0] - 0.5573653674777325)<epsilon and abs(F[1].der[1][1] - 2.786826837388662)<epsilon
    assert abs(F[1].der[2][0] - 0.37296598096239875)<epsilon and abs(F[1].der[2][1] - 5.594489714435981)<epsilon

def test_cos_vector():
    a = [1, 2, 3]
    b = [0.5, 0.2, 0.1]

    x0 = AutoDiff(a, 1, 2, 0)
    x1 = AutoDiff(b, 1, 2, 1)

    f0 = cos((x0 + x1)/4)
    f1 = cos(x0**2 * x1)
    F = [f0, f1]

    assert F[0].val[0][0] == 0.9305076219123143 and F[0].val[1][0] == 0.8525245220595057 and F[0].val[2][0] == 0.7144210340559314
    assert F[1].val[0][0] == 0.8775825618903728 and abs(F[1].val[1][0] - 0.6967067093471655)<epsilon and abs(F[1].val[2][0] - 0.6216099682706645)<epsilon
    # der: len_val x num_var
    assert F[0].der[0][0] == -0.09156813227151189 and F[0].der[0][1] == -0.09156813227151189
    assert F[0].der[1][0] == -0.1306718072326648 and F[0].der[1][1] == -0.1306718072326648
    assert F[0].der[2][0] == -0.17492901883665088 and F[0].der[2][1] == -0.17492901883665088

    assert F[1].der[0][0] == -0.479425538604203 and F[1].der[0][1] == -0.479425538604203
    assert F[1].der[1][0] == -0.5738848727196183 and F[1].der[1][1] == -2.869424363598091
    assert abs(F[1].der[2][0] - -0.46999614577649007)<epsilon and abs(F[1].der[2][1] - -7.04994218664735)<epsilon

def test_tan_vector():
    a = [1, 2, 3]
    b = [0.5, 0.2, 0.1]

    x0 = AutoDiff(a, 1, 2, 0)
    x1 = AutoDiff(b, 1, 2, 1)

    f0 = tan((x0 + x1)/4)
    f1 = tan(x0**2 * x1)
    F = [f0, f1]

    assert F[0].val[0][0] == 0.39362657592563277 and F[0].val[1][0] == 0.6131052132881357 and abs(F[0].val[2][0] - 0.9794169572166087)<epsilon
    assert F[1].val[0][0] == 0.5463024898437905 and abs(F[1].val[1][0] - 1.029638557050364)<epsilon and abs(F[1].val[2][0] - 1.260158217550339)<epsilon
    # der: len_val x num_var
    assert abs(F[0].der[0][0] - 0.2887354703187345)<epsilon and abs(F[0].der[0][1] - 0.2887354703187345)<epsilon
    assert abs(F[0].der[1][0] - 0.34397450064027263)<epsilon and abs(F[0].der[1][1] - 0.34397450064027263)<epsilon
    assert abs(F[0].der[2][0] - 0.48981439402086013)<epsilon and abs(F[0].der[2][1] - 0.48981439402086013)<epsilon

    assert abs(F[1].der[0][0] - 1.2984464104095248)<epsilon and abs(F[1].der[0][1] - 1.2984464104095248)<epsilon
    assert abs(F[1].der[1][0] - 1.6481244465318043)<epsilon and abs(F[1].der[1][1] - 8.240622232659021)<epsilon
    assert abs(F[1].der[2][0] - 1.5527992399557886)<epsilon and abs(F[1].der[2][1] - 23.291988599336825)<epsilon

def test_sinh_vector():
    a = [1, 2, 3]
    b = [0.5, 0.2, 0.1]

    x0 = AutoDiff(a, 1, 2, 0)
    x1 = AutoDiff(b, 1, 2, 1)

    f0 = sinh((x0 + x1)/4)
    f1 = sinh(x0**2 * x1)
    F = [f0, f1]

    assert F[0].val[0][0] == 0.38385106791361456 and F[0].val[1][0] == 0.5781516037434543 and F[0].val[2][0] == 0.8549441730922384
    assert F[1].val[0][0] == 0.5210953054937474 and F[1].val[1][0] == 0.888105982187623 and F[1].val[2][0] == 1.0265167257081753
    # der: len_val x num_var
    assert F[0].der[0][0] == 0.2677850866761467 and F[0].der[0][1] == 0.2677850866761467
    assert F[0].der[1][0] == 0.28877535353098527 and F[0].der[1][1] == 0.28877535353098527
    assert F[0].der[2][0] == 0.328911988522801 and F[0].der[2][1] == 0.328911988522801

    assert F[1].der[0][0] == 1.1276259652063807 and F[1].der[0][1] == 1.1276259652063807
    assert F[1].der[1][0] == 1.069947957043876 and F[1].der[1][1] == 5.349739785219379
    assert abs(F[1].der[2][0] - 0.8598518312692647)<epsilon and abs(F[1].der[2][1] - 12.897777469038969)<epsilon

def test_cosh_vector():
    a = [1, 2, 3]
    b = [0.5, 0.2, 0.1]

    x0 = AutoDiff(a, 1, 2, 0)
    x1 = AutoDiff(b, 1, 2, 1)

    f0 = cosh((x0 + x1)/4)
    f1 = cosh(x0**2 * x1)
    F = [f0, f1]

    assert F[0].val[0][0] == 1.0711403467045868 and F[0].val[1][0] == 1.155101414123941 and F[0].val[2][0] == 1.315647954091204
    assert F[1].val[0][0] == 1.1276259652063807 and F[1].val[1][0] == 1.3374349463048447 and abs(F[1].val[2][0] - 1.4330863854487743)<epsilon
    # der: len_val x num_var
    assert F[0].der[0][0] == 0.09596276697840364 and F[0].der[0][1] == 0.09596276697840364
    assert F[0].der[1][0] == 0.14453790093586358 and F[0].der[1][1] == 0.14453790093586358
    assert F[0].der[2][0] == 0.2137360432730596 and F[0].der[2][1] == 0.2137360432730596

    assert F[1].der[0][0] == 0.5210953054937474 and F[1].der[0][1] == 0.5210953054937474
    assert F[1].der[1][0] == 0.7104847857500984 and F[1].der[1][1] == 3.552423928750492
    assert F[1].der[2][0] == 0.6159100354249053 and F[1].der[2][1] == 9.238650531373578

def test_tanh_vector():
    a = [1, 2, 3]
    b = [0.5, 0.2, 0.1]

    x0 = AutoDiff(a, 1, 2, 0)
    x1 = AutoDiff(b, 1, 2, 1)

    f0 = tanh((x0 + x1)/4)
    f1 = tanh(x0**2 * x1)
    F = [f0, f1]

    assert F[0].val[0][0] == 0.35835739835078595 and F[0].val[1][0] == 0.5005202111902353 and F[0].val[2][0] == 0.6498274636719203
    assert F[1].val[0][0] == 0.46211715726000974 and abs(F[1].val[1][0] - 0.664036770267849)<epsilon and F[1].val[2][0] == 0.7162978701990245
    # der: len_val x num_var
    assert F[0].der[0][0] == 0.21789499376181404 and F[0].der[0][1] == 0.21789499376181404
    assert F[0].der[1][0] == 0.18736987954752057 and F[0].der[1][1] == 0.18736987954752057
    assert F[0].der[2][0] == 0.14443106686442975 and F[0].der[2][1] == 0.14443106686442975

    assert F[1].der[0][0] == 0.7864477329659274 and F[1].der[0][1] == 0.7864477329659274
    assert abs(F[1].der[1][0] - 0.4472441341857952)<epsilon and abs(F[1].der[1][1] - 2.236220670928976)<epsilon
    assert abs(F[1].der[2][0] - 0.29215041668900493)<epsilon and abs(F[1].der[2][1] - 4.3822562503350735)<epsilon

def test_sqrt_vector():
    a = [1, 2, 3]
    b = [0.5, 0.2, 0.1]

    x0 = AutoDiff(a, 1, 2, 0)
    x1 = AutoDiff(b, 1, 2, 1)

    f0 = sqrt((x0 + x1)/4)
    f1 = sqrt(x0**2 * x1)
    F = [f0, f1]

    assert F[0].val[0][0] == 0.6123724356957945 and F[0].val[1][0] == 0.7416198487095663 and F[0].val[2][0] == 0.8803408430829505
    assert F[1].val[0][0] == 0.7071067811865476 and F[1].val[1][0] == 0.8944271909999159 and F[1].val[2][0] == 0.9486832980505138
    # der: len_val x num_var
    assert F[0].der[0][0] == 0.20412414523193154 and F[0].der[0][1] == 0.20412414523193154
    assert F[0].der[1][0] == 0.1685499656158105 and F[0].der[1][1] == 0.1685499656158105
    assert F[0].der[2][0] == 0.1419904585617662 and F[0].der[2][1] == 0.1419904585617662

    assert F[1].der[0][0] == 0.7071067811865475 and F[1].der[0][1] == 0.7071067811865475
    assert F[1].der[1][0] == 0.447213595499958 and F[1].der[1][1] == 2.23606797749979
    assert F[1].der[2][0] == 0.316227766016838 and F[1].der[2][1] == 4.743416490252569

def test_log_vector():
    a = [1, 2, 3]
    b = [0.5, 0.2, 0.1]

    x0 = AutoDiff(a, 1, 2, 0)
    x1 = AutoDiff(b, 1, 2, 1)

    f0 = log((x0 + x1)/4)
    f1 = log(x0**2 * x1)
    F = [f0, f1]

    assert F[0].val[0][0] == -0.9808292530117262 and F[0].val[1][0] == -0.5978370007556204 and F[0].val[2][0] == -0.25489224962879004
    assert F[1].val[0][0] == -0.6931471805599453 and F[1].val[1][0] == -0.2231435513142097 and F[1].val[2][0] == -0.10536051565782628
    # der: len_val x num_var
    assert F[0].der[0][0] == 0.6666666666666666 and F[0].der[0][1] == 0.6666666666666666
    assert F[0].der[1][0] == 0.45454545454545453 and F[0].der[1][1] == 0.45454545454545453
    assert F[0].der[2][0] == 0.3225806451612903 and F[0].der[2][1] == 0.3225806451612903

    assert F[1].der[0][0] == 2.0 and F[1].der[0][1] == 2.0
    assert F[1].der[1][0] == 1.0 and F[1].der[1][1] == 5.0
    assert F[1].der[2][0] == 0.6666666666666667 and F[1].der[2][1] == 10.0

def test_exp_vector():
    a = [1, 2, 3]
    b = [0.5, 0.2, 0.1]

    x0 = AutoDiff(a, 1, 2, 0)
    x1 = AutoDiff(b, 1, 2, 1)

    f0 = exp((x0 + x1)/4)
    f1 = exp(x0**2 * x1)
    F = [f0, f1]

    assert F[0].val[0][0] == 1.4549914146182013 and F[0].val[1][0] == 1.7332530178673953 and F[0].val[2][0] == 2.1705921271834425
    assert F[1].val[0][0] == 1.6487212707001282 and F[1].val[1][0] == 2.225540928492468 and F[1].val[2][0] == 2.45960311115695
    # der: len_val x num_var
    assert F[0].der[0][0] == 0.3637478536545503 and F[0].der[0][1] == 0.3637478536545503
    assert F[0].der[1][0] == 0.4333132544668488 and F[0].der[1][1] == 0.4333132544668488
    assert F[0].der[2][0] == 0.5426480317958606 and F[0].der[2][1] == 0.5426480317958606

    assert F[1].der[0][0] == 1.6487212707001282 and F[1].der[0][1] == 1.6487212707001282
    assert F[1].der[1][0] == 1.7804327427939743 and F[1].der[1][1] == 8.902163713969871
    assert F[1].der[2][0] == 1.47576186669417 and F[1].der[2][1] == 22.13642800041255
