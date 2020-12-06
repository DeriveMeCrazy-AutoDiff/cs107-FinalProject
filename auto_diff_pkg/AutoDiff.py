import numpy as np
import time

class AutoDiff():

    def __init__(self, value, deriv=1.0, variables = 1, position = 0):
        if isinstance(value, (list, int, float)):
            self.val = np.array([value]).T
            self.der = np.ones((len(self.val),1))*deriv
        elif isinstance(value, (np.ndarray, np.generic)):
            self.val = value
            self.der = deriv
        self.children = []
        self.grad_value = None
        
        if variables >1:
            self.der = np.zeros((len(self.val),variables))
            self.der[ : , position] = deriv

    def __neg__(self):
        return AutoDiff(-self.val, -self.der)

    def __add__(self, other):
        try:
            return AutoDiff(self.val+other.val, self.der+other.der)
        except AttributeError:
            return AutoDiff(self.val+other, self.der)
        
    def __radd__(self, other): 
        return self.__add__(other)
          
    def __mul__(self, other):
        try:
            z = AutoDiff(self.val*other.val, self.der*other.val + self.val*other.der)
            self.children.append((other.val, z))
            other.children.append((self.val, z))
            return z
        except AttributeError:
            return AutoDiff(self.val*other, self.der*other)

    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __sub__(self, other):
        try:
            return AutoDiff(self.val-other.val, self.der-other.der)
        except AttributeError:
            return AutoDiff(self.val-other, self.der)
    
    def __rsub__(self, other): 
        try:
            return AutoDiff(other.val-self.val, other.der-self.der)
        except AttributeError:
            return AutoDiff(other-self.val, -self.der)
    
    def __truediv__(self, other): 
        try:
            return AutoDiff(self.val/other.val, (self.der*other.val - self.val*other.der)/(other.val**2))
        except AttributeError:
            return AutoDiff(self.val/other, self.der/other)
    
    def __rtruediv__(self, other): 
        try:
            return AutoDiff(other.val/self.val, (self.val*other.der- self.der*other.val)/(self.val**2))
        except AttributeError:
            return AutoDiff(other/self.val, -self.der*other/(self.val**2))
    
    def __pow__(self, other):
        try:
            return AutoDiff(self.val**other.val, other.val*(self.val**(other.val-1))*self.der+np.log(np.abs(self.val))*(self.val**other.val)*other.der)
        except AttributeError:
            return AutoDiff(self.val**other, other*(self.val**(other-1))*self.der)
        
    def __rpow__(self, other):
        try:
            return AutoDiff(other.val**self.val, self.val*(other.val**(self.val-1))*other.der+np.log(np.abs(other.val))*(other.val**self.val)*self.der)
        except AttributeError:
            return AutoDiff(other**self.val, np.log(np.abs(other))*(other**self.val)*self.der)
    
    def __str__(self):
        return 'value: {}, derivative: {}'.format(self.val,self.der)
    
    def reverse_mode(self):
        # recurse only if the value is not yet cached
        if self.grad_value is None:
            # calculate derivative using chain rule
            self.grad_value = sum(weight * var.reverse_mode()for weight, var in self.children)
        return self.grad_value

def log(x):
    try:
        if x.val < 0:
            raise ValueError('Log is not defined for negative values')
        else:
            return AutoDiff(np.log(x.val), x.der*(1/x.val))
    except AttributeError:
        if x < 0:
            raise ValueError('Log is not defined for negative values')
        else: 
            return np.log(x)

def exp(x):
    try:
        return AutoDiff(np.exp(x.val), x.der*np.exp(x.val))
    except AttributeError:
        return np.exp(x)

def sin(x):
    try:
        return AutoDiff(np.sin(x.val), x.der*np.cos(x.val))
    except AttributeError:
        return np.sin(x)

def cos(x):
    try:
        return AutoDiff(np.cos(x.val), x.der*(-np.sin(x.val)))
    except AttributeError:
        return np.cos(x)

def tan(x):
    try:
        return AutoDiff(np.tan(x.val), x.der*(1/np.cos(x.val)**2))
    except AttributeError:
        return np.tan(x)
    
def sqrt(x):
    try:
        if x.val < 0:
            raise ValueError('Sqrt is not defined for negative values')
        else:
            return AutoDiff(np.sqrt(x.val), (1/2)*x.der/(np.sqrt(x.val)))
    except AttributeError:
        if x < 0:
            raise ValueError('Sqrt is not defined for negative values')
        else: 
            return np.sqrt(x)
        
def jacobian (variables, functions):
    jacobian_array = np.empty((len(functions), len(variables)))  
                                 
    autodiff_list = []
    for idx_val, val in enumerate(variables):
        autodiff_list.append(AutoDiff(val,0))
    for idx_diff, val  in enumerate(variables):
        autodiff_list[idx_diff] = AutoDiff(val,1)
        for idx_f, function  in enumerate(functions):
            jacobian_array[idx_f,idx_diff] = function(*autodiff_list).der
        autodiff_list[idx_diff] = AutoDiff(val,0)
    return jacobian_array


values = [1,2,4] 
def f1(x0, x1, x2):
    return (x0 + x1 + x2)
def f2(x0, x1, x2):
    return (1*x0 + 2*x1 + 3*x2)
def f3(x0, x1, x2):
    return (1*x0*2*x1*3*x2)
def f4(x0, x1, x2):
    return (x0**2 + x1**3 + x2**4)
functions = [f1, f2, f3,f4]
print(jacobian(values, functions), "\n")

x0=AutoDiff(1,1,3,0)
x1=AutoDiff(2,1,3,1)
x2=AutoDiff(4,1,3,2)

f1 = x0 + x1 + x2
f2 = 1*x0 + 2*x1 + 3*x2
f3 = 1*x0*2*x1*3*x2
f4 = x0**2 + x1**3 + x2**4
print(f4.der, "\n")

F=[f1, f2, f3, f4]
print(F[0].der)
print(F[1].der)
print(F[2].der)
print(F[3].der)


tic = time.perf_counter()
x = AutoDiff(4)
y = AutoDiff(.5)

a = x * y
a.grad_value = 1
print(x.reverse_mode(), y.reverse_mode())
toc = time.perf_counter()
print(f"Reverse Mode {toc - tic} seconds")


tic = time.perf_counter()
x = AutoDiff(4,1,2,0)
y = AutoDiff(.5,1,2,1)

a = x * y

print(a.der)
toc = time.perf_counter()
print(f"Forward Mode {toc - tic} seconds")

a = [2,4,6]
b = [1,3,5]
c = [3,6,9]
x0=AutoDiff(a,1,3,0)
x1=AutoDiff(b,1,3,1)
x2=AutoDiff(c,1,3,2)

f1 = x0 + x1 + x2
f2 = 1*x0 + 2*x1 + 3*x2
f3 = 1*x0*2*x1*3*x2
f4 = x0**2 + x1**3 + x2**4
f5 = x0/x1**x2

F=[f1, f2, f3, f4, f5]
print(F[0].der)
print(F[1].der)
print(F[2].der)
print(F[3].der)
print(F[4].der)
