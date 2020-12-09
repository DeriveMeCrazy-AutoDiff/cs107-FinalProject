import pytest

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


#import auto_diff_pkg.AutoDiff as AutoDiff
from  auto_diff_pkg.AutoDiff import AutoDiff, sqrt, sin, cos, exp, log, tan

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

def test_sqrt_int():    
    curr_func = sqrt(5)
    assert curr_func == 2.23606797749979
       
def test_sqrt_AutoDiff():    
    x0 = AutoDiff(2)
    curr_func = sqrt(x0 + 6)
    assert curr_func.val == 2.8284271247461903 and curr_func.der == 0.17677669529663687
