import numpy as np

class AutoDiff():

    def __init__(self, value, deriv=1.0):
        self.val = value
        self.der = deriv

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
            return AutoDiff(self.val*other.val, self.der*other.val + self.val*other.der)
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
            return AutoDiff(other-self.val, self.der)
    
    def __truediv__(self, other): 
        try:
            return AutoDiff(self.val/other.val, (self.der*other.val - self.val*other.der)/(other.val**2))
        except AttributeError:
            return AutoDiff(self.val/other, self.der/other)
    
    def __rtruediv__(self, other): 
        try:
            return AutoDiff(other.val/self.val, (self.val*other.der- self.der*other.val)/(self.val**2))
        except AttributeError:
            return AutoDiff(other/self.val, other/self.der)
        
    def __rdiv__(self, other): 
        try:
            return AutoDiff(other.val/self.val, self.val*other.der- self.der*other.val)/(self.val**2)
        except AttributeError:
            return AutoDiff(other/self.val, self.der/other)
    
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


def log(x):
    try:
        return AutoDiff(np.log(x.val), x.der*(1/x.val))
    except AttributeError:
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
        return AutoDiff(np.sqrt(x.val), x.der/(1/2*(np.sqrt(x.val))))
    except AttributeError:
        return np.sqrt(x)

