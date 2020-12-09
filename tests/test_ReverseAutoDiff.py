import pytest
import numpy as np
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


#import auto_diff_pkg.ReverseADNode as AutoDiff
from  auto_diff_pkg.ReverseAutoDiff import ReverseADNode, sqrt, sin, cos, exp, log, tan, arcsin, arccos, arctan, sinh, cosh, tanh, jacobian

#final EPSILON = 10**(-12)
epsilon = 10**(-12)

def test_init_int_zero():    
    x0 = ReverseADNode(0)
    assert x0.value == 0 and x0.grad() == 0

def test_init_float():    
    x0 = ReverseADNode(0.0)
    assert x0.value == 0.0 and x0.grad() == 0.0
    
def test_init_None():
    with pytest.raises(TypeError):
       x0 = ReverseADNode(None)
       
def test_add_int():    
    x0 = ReverseADNode(0)
    curr_func = x0+5
    curr_func.grad_value = 1.0
    assert curr_func.value == 5 and x0.grad() == 1.0
    
def test_radd_int():    
    x0 = ReverseADNode(0)
    curr_func = 5 + x0
    curr_func.grad_value = 1.0
    assert curr_func.value == 5 and x0.grad() == 1

def test_add_float(): 
    x0 = ReverseADNode(0.0)
    curr_func = x0+5.0
    curr_func.grad_value = 1.0
    assert curr_func.value == 5.0 and x0.grad() == 1

def test_radd_float(): 
    x0 = ReverseADNode(0.0)
    curr_func = x0+5.0
    curr_func.grad_value = 1.0
    assert curr_func.value == 5.0 and x0.grad() == 1
  
def test_add_ReverseADNode():    
    x0 = ReverseADNode(5)
    curr_func = (x0+6.3)+x0
    curr_func.grad_value = 1.0
    assert curr_func.value == 16.3 and x0.grad() == 2

def test_sub():    
    x0 = ReverseADNode(0)
    curr_func = x0-5
    curr_func.grad_value = 1.0
    assert curr_func.value == -5.0 and x0.grad() == 1

def test_rsub():    
    x0 = ReverseADNode(0)
    curr_func = 5 - x0
    curr_func.grad_value = 1.0
    assert curr_func.value == 5.0 and x0.grad() == -1
   
def test_sub_ReverseADNode():    
    x0 = ReverseADNode(5)
    curr_func = (x0+6.3) - x0
    curr_func.grad_value = 1.0
    assert abs(curr_func.value - 6.3) < epsilon and x0.grad() == 0

def test_rsub_ReverseADNode():    
    x0 = ReverseADNode(5)
    curr_func = x0 - (x0+6.3)  
    curr_func.grad_value = 1.0
    assert abs(curr_func.value - -6.3) < epsilon and x0.grad() == 0

def test_mul_1():    
    x0 = ReverseADNode(1)
    curr_func = x0*5
    curr_func.grad_value = 1.0
    assert curr_func.value == 5.0 and x0.grad() == 5

def test_mul_0():    
    x0 = ReverseADNode(0)
    curr_func = x0 * 5
    curr_func.grad_value = 1.0
    assert curr_func.value == 0.0 and x0.grad() == 5

def test_rmul():    
    x0 = ReverseADNode(-3)
    curr_func = 5 * x0
    curr_func.grad_value = 1.0
    assert curr_func.value == -15.0 and x0.grad() == 5
   
def test_mul_ReverseADNode():    
    x0 = ReverseADNode(5)
    curr_func = (x0+6.3) * x0
    curr_func.grad_value = 1.0
    assert curr_func.value == 56.5 and x0.grad() == 16.3

def test_div_1():    
    x0 = ReverseADNode(1)
    curr_func = x0/5
    curr_func.grad_value = 1.0
    assert curr_func.value == 0.2 and x0.grad() == 0.2

def test_div_0():    
    x0 = ReverseADNode(0)
    curr_func = x0 / 5
    curr_func.grad_value = 1.0
    assert curr_func.value == 0.0 and x0.grad() == 0.2

def test_rdiv():    
    x0 = ReverseADNode(-2)
    curr_func = 6 / x0
    curr_func.grad_value = 1.0
    assert curr_func.value == -3.0 and x0.grad() == -6/4

def test_div_ReverseADNode():    
    x0 = ReverseADNode(5)
    curr_func = (x0+6.3) / x0
    curr_func.grad_value = 1.0
    assert abs(curr_func.value - 2.2600000000000002) < epsilon and x0.grad() == -0.252

def test_pow_0():    
    x0 = ReverseADNode(2)
    curr_func = x0**0
    curr_func.grad_value = 1.0
    assert curr_func.value == 1.0 and x0.grad() == 0.0

def test_pow_neg():    
    x0 = ReverseADNode(4)
    curr_func = x0**-1
    curr_func.grad_value = 1.0
    assert curr_func.value == 0.25 and x0.grad() == -1/16

def test_pow():    
    x0 = ReverseADNode(4)
    curr_func = x0 ** 2
    curr_func.grad_value = 1.0
    assert curr_func.value == 16.0 and x0.grad() == 8.0

def test_pow_frac():    
    x0 = ReverseADNode(4)
    curr_func = x0 ** 0.5
    curr_func.grad_value = 1.0
    assert curr_func.value == 2.0 and x0.grad() == 0.25
  
def test_rpow():    
    x0 = ReverseADNode(2)
    curr_func = 6 ** x0
    curr_func.grad_value = 1.0
    assert curr_func.value == 36 and x0.grad() == 64.50334089220998
  
def test_pow_ReverseADNode():    
    x0 = ReverseADNode(3)
    curr_func = (x0 ** 2) ** x0
    curr_func.grad_value = 1.0
    assert curr_func.value == 729 and x0.grad() == 3059.776716878104

def test_log():    
    curr_func = log(2)
    assert curr_func == 0.6931471805599453

def test_log_neg():    
    x0 = ReverseADNode(-4)
    with pytest.raises(ValueError):
        curr_func = log(x0)

def test_log_frac():    
    curr_func = log(0.5)
    assert curr_func == -0.6931471805599453

def test_log_ReverseADNode():    
    x0 = ReverseADNode(10)
    curr_func = log(x0 ** 2)
    real_log_value = 4.605170185988092
    curr_func.grad_value = 1.0
    assert curr_func.value == 4.605170185988092 and x0.grad() == 0.2

def test_exp_frac():    
    curr_func = exp(0.5)
    assert curr_func == 1.6487212707001282

def test_exp_int():    
    curr_func = exp(5)
    assert curr_func == 148.4131591025766

def test_exp_ReverseADNode():    
    x0 = ReverseADNode(2)
    curr_func = exp(x0 ** 2)
    curr_func.grad_value = 1.0
    assert curr_func.value == 54.598150033144236 and x0.grad() == 218.39260013257694

def test_sin_frac():    
    curr_func = sin(0.5)
    assert curr_func == 0.479425538604203

def test_sin_int():    
    curr_func = sin(5)
    assert curr_func == -0.9589242746631385

def test_sin_ReverseADNode():    
    x0 = ReverseADNode(2)
    curr_func = sin(x0 ** 2)
    curr_func.grad_value = 1.0
    assert curr_func.value == -0.7568024953079282 and x0.grad() == -2.6145744834544478

def test_cos_frac():    
    curr_func = cos(0.5)
    assert curr_func == 0.8775825618903728

def test_cos_int():    
    curr_func = cos(5)
    assert abs(curr_func - 0.2836621854632263) < epsilon

def test_cos_ReverseADNode():    
    x0 = ReverseADNode(2)
    curr_func = cos(x0 ** 2)
    curr_func.grad_value = 1.0
    assert curr_func.value == -0.6536436208636119 and x0.grad() == 3.027209981231713

def test_tan_frac():    
    curr_func = tan(0.5)
    assert abs(curr_func - 0.5463024898437905) < epsilon

def test_tan_int():    
    curr_func = tan(-5)
    assert abs(curr_func - 3.380515006246585) < epsilon

def test_tan_ReverseADNode():    
    x0 = ReverseADNode(2)
    curr_func = tan(x0 ** 2)
    curr_func.grad_value = 1.0
    assert curr_func.value == 1.1578212823495775 and x0.grad() == 9.36220048744648

def test_sqrt_frac():    
    curr_func = sqrt(0.5)
    assert curr_func == 0.7071067811865476

def test_sqrt_neg():
    with pytest.raises(ValueError):
        curr_func = sqrt(-5)

def test_sqrt_int():    
    curr_func = sqrt(5)
    assert curr_func == 2.23606797749979

def test_sqrt_ReverseADNode():    
    x0 = ReverseADNode(2)
    curr_func = sqrt(x0 + 6)
    curr_func.grad_value = 1.0
    assert curr_func.value == 2.8284271247461903 and x0.grad() == 0.17677669529663687

def test_arcsin_frac():
    curr_func = arcsin(0.5)
    assert abs(curr_func - 0.5235987755982988) < epsilon

def test_arcsin_int():
    curr_func = arcsin(1)
    assert abs(curr_func - 1.5707963267948966) < epsilon

def test_arcsin_outside_one():
    with pytest.raises(ValueError):
        curr_func = arcsin(2)

def test_arcsin_ReverseADNode():
    x0 = ReverseADNode(0.8)
    curr_func = arcsin(x0 ** 2)
    curr_func.grad_value = 1.0
    assert curr_func.value == 0.25268025514207865 and x0.grad() == 2.082316825181415

def test_arccos_frac():
    curr_func = arccos(0.5)
    assert abs(curr_func - 1.0471975511965976) < epsilon

def test_arccos_int():
    curr_func = arccos(-1)
    assert abs(curr_func - 3.141592653589793) < epsilon

def test_arccos_outside_one():
    with pytest.raises(ValueError):
        curr_func = arccos(2)

def test_arccos_ReverseADNode():
    x0 = ReverseADNode(0.8)
    curr_func = arccos(x0 ** 2)
    curr_func.grad_value = 1.0
    assert curr_func.value == 0.8762980611683405 and x0.grad() == -2.082316825181415

def test_arctan_frac():
    curr_func = arctan(0.5)
    assert abs(curr_func - 0.46364760900080615) < epsilon

def test_arctan_int():
    curr_func = arctan(1)
    assert abs(curr_func - 0.7853981633974483) < epsilon

def test_arctan_outside_half_pi():
    with pytest.raises(ValueError):
        curr_func = arctan(2)

def test_arctan_ReverseADNode():
    x0 = ReverseADNode(0.8)
    curr_func = arctan(x0 ** 2)
    curr_func.grad_value = 1.0
    assert curr_func.value == 0.5693131911006619 and x0.grad() == -1.1350737797956867

def test_sinh_frac():
    curr_func = sinh(0.5)
    assert abs(curr_func - 0.5210953054937474) < epsilon

def test_sinh_int():
    curr_func = sinh(5)
    assert abs(curr_func - 74.20321057778875) < epsilon

def test_sinh_ReverseADNode():
    x0 = ReverseADNode(0.8)
    curr_func = sinh(x0 ** 2)
    curr_func.grad_value = 1.0
    assert curr_func.value == 0.6845942276309516 and x0.grad() == 1.9390186426784002

def test_cosh_frac():
    curr_func = cosh(0.5)
    assert abs(curr_func - 1.1276259652063807) < epsilon

def test_cosh_int():
    curr_func = cosh(5)
    assert abs(curr_func - 74.20994852478785) < epsilon

def test_cosh_ReverseADNode():
    x0 = ReverseADNode(0.8)
    curr_func = cosh(x0 ** 2)
    curr_func.grad_value = 1.0
    assert curr_func.value == 1.2118866516740001 and x0.grad() == 1.0953507642095226

def test_tanh_frac():
    curr_func = tanh(0.5)
    assert abs(curr_func - 0.46211715726000974) < epsilon

def test_tanh_int():
    curr_func = tanh(5)
    assert abs(curr_func - 0.9999092042625951) < epsilon

def test_tanh_ReverseADNode():
    x0 = ReverseADNode(0.8)
    curr_func = tanh(x0 ** 2)
    curr_func.grad_value = 1.0
    assert curr_func.value == 0.5648995528462251 and x0.grad() == 1.089421592310616
 
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
    jacobian_res = jacobian(values, functions)

    diff_arr0 = np.subtract(jacobian_res[0],[1, 1, 1]) 
    diff_arr1 = np.subtract(jacobian_res[1],[1, 2, 3]) 
    diff_arr2 = np.subtract(jacobian_res[2],[0.48, 0.24, 0.12])
    diff_arr3 = np.subtract(jacobian_res[3],[0.2, 0.12, 0.256])
    diff_arr4 = np.subtract(jacobian_res[4],[0.9950041652780257, -0.19866933079506122, 1.178754105810975])
    assert (diff_arr0 < epsilon).all()
    assert (diff_arr1 < epsilon).all()
    assert (diff_arr2 < epsilon).all()
    assert (diff_arr3 < epsilon).all()
    assert (diff_arr4 < epsilon).all()

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
    jacobian_res = jacobian(values, functions)
    diff_arr0 = np.subtract(jacobian_res[0],[1, 1, 1]) 
    diff_arr1 = np.subtract(jacobian_res[1],[1, 2, 3]) 
    diff_arr2 = np.subtract(jacobian_res[2],[48, 24, 12])
    diff_arr3 = np.subtract(jacobian_res[3],[2, 12, 256])
    diff_arr4 = np.subtract(jacobian_res[4],[0.5403023058681398, -0.9092974268256817, 2.34055012186162])
    assert (diff_arr0 < epsilon).all()
    assert (diff_arr1 < epsilon).all()
    assert (diff_arr2 < epsilon).all()
    assert (diff_arr3 < epsilon).all()
    assert (diff_arr4 < epsilon).all()