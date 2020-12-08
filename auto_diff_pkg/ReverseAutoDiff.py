import numpy as np

class ReverseAutoDiff():
    def __init__(self, variables, functions, input_values):
        self.graph = []
        self.variables = variables
        self.functions = functions
    

class ReverseADNode:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.grad_value = None
        self.op = ''

    def grad(self):
        if self.grad_value is None:
            self.grad_value = sum(weight * var.grad() for weight, var in self.children)
        return self.grad_value
    
    def __add__(self, other):
        node = ReverseADNode(self.value + other.value)
        self.children.append((1.0, node))
        other.children.append((1.0, node))
        node.op = 'ADD'
        return node
    
    def __sub__(self, other):
        if not isinstance(other, ReverseADNode):
            other = ReverseADNode(other)
        node = ReverseADNode(self.value - other.value)
        self.children.append((1.0, node))
        other.children.append((-1.0, node))
        node.op = 'SUB'
        return node
    
    def __rsub__(self, other):
        other = ReverseADNode(other)
        node = ReverseADNode(other.value - self.value)
        self.children.append((-1.0, node))
        other.children.append((1.0, node))
        node.op = 'SUB'
        return node
    
    def __inv__(self):
        node = ReverseADNode(1 / self.value)
        self.children.append(-self.value ** -2, node)
        node.op = 'INV'
        return node
                     
    def __truediv__(self, other):
        if not isinstance(other, ReverseADNode):
            other = ReverseADNode(other)
        return self.__mul__(other.__inv())
    
    def __rtruediv__(self, other):
        other = ReverseADNode(other)
        return other.__mul__(self.__inv())
    
    def __mul__(self, other):
        node = ReverseADNode(self.value * other.value)
        self.children.append((other.value, node))
        other.children.append((self.value, node))
        node.op = 'MUL/DIV'
        return node
    
    def __pow__(self, other):
        if not isinstance(other, ReverseADNode):
            other = ReverseADNode(other)
        node = ReverseADNode(self.value ** other.value)
        self.children.append((other.value*self.value**(other.value-1), node))
        other.children.append(((self.value**other.value)*np.log(np.abs(self.value)), node))
        node.op = 'POW'
        return node
        
    def __rpow__(self, other):
        other = ReverseADNode(other)
        return other.__pow__(self)
    
    def graph(self):
        if len(self.children) == 0:
                print("leaf node of type: ", self.op, " and value: ", self.value)
        else:
            print("Op node: ", self.op , " Value: ",  self.value)
            for der, node in self.children:
                node.graph()
    
def sin(x):
    try:
        node = ReverseADNode(np.sin(x.value))
        x.children.append((np.cos(x.value), node))
        node.op = 'SIN'
        return node
    except AttributeError:
        return np.sin(x)

def cos(x):
    try:
        node = ReverseADNode(np.cos(x.value))
        x.children.append((-1*np.sin(x.value), node))
        node.op = 'COS'
        return node
    except AttributeError:
        return np.cos(x)

def tan(x):
    try:
        node = ReverseADNode(np.tan(x.value))
        x.children.append(((np.tan(x.value)**2)+1, node))
        node.op = 'TAN'
        return node
    except AttributeError:
        return np.tan(x)
    
def arcsin(x):
    try:
        node = ReverseADNode(np.arcsin(x.value))
        x.children.append((1/np.sqrt(1-x.value**2), node))
        node.op = 'ARCSIN'
        return node
    except AttributeError:
        return np.arcsin(x)

def arccos(x):
    try:
        node = ReverseADNode(np.arccos(x.value))
        x.children.append((-1/np.sqrt(1-x.value**2), node))
        node.op = 'ARCCOS'
        return node
    except AttributeError:
        return np.arccos(x)
    
def arctan(x):
    try:
        node = ReverseADNode(np.arctan(x.value))
        x.children.append((1/(1+x.value**2), node))
        node.op = 'ARCTAN'
        return node
    except AttributeError:
        return np.arctan(x)

def exp(x):
    try:
        node = ReverseADNode(np.exp(x.value))
        x.children.append((np.exp(x.value), node))
        node.op = 'EXP'
        return node
    except AttributeError:
        return np.exp(x)

def sinh(x):
    try:
        node = ReverseADNode(np.sinh(x.value))
        x.children.append((np.cosh(x.value), node))
        node.op = 'SINH'
        return node
    except AttributeError:
        return np.sinh(x)

def cosh(x):
    try:
        node = ReverseADNode(np.cosh(x.value))
        x.children.append((np.sinh(x.value), node))
        node.op = 'COSH'
        return node
    except AttributeError:
        return np.cosh(x)

def tanh(x):
    try:
        node = ReverseADNode(np.tanh(x.value))
        x.children.append((1/(np.cosh(x.value)**2), node))
        node.op = 'TANH'
        return node
    except AttributeError:
        return np.tanh(x)
    
def log(x,base = np.exp):
    try:
        if x.value < 0:
            raise ValueError('Log is not defined for negative values')
        else:
            node = ReverseADNode(np.log(x.value)/np.log(base))
            x.children.append((1/(x.value*np.log(base)), node))
            node.op = 'LOG'
            return node
    except AttributeError:
        if x < 0:
            raise ValueError('Log is not defined for negative values')
        else: 
            return np.log(x)/np.log(base)
    
def sqrt(x):
    try:
        if x.value < 0:
            raise ValueError('Sqrt is not defined for negative values')
        else:
            node = ReverseADNode(np.sqrt(x.value))
            x.children.append((1/(2*np.sqrt(x.value)), node))
            node.op = 'SQRT'
            return node
    except AttributeError:
        if x < 0:
            raise ValueError('Sqrt is not defined for negative values')
        else: 
            return np.sqrt(x)