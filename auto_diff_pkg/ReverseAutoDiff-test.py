import numpy as np

class ReverseAutoDiff():

    def __init__(self, value, deriv=1, variables = 1, position = 0):
        self.val = value
        self.children = []
        self.grad_value = None
        self.op = ''
        self.der = deriv
        
        if variables >1:
            self.der = np.zeros(variables)
            self.der[position] = deriv

    def __neg__(self):
        node = ReverseAutoDiff(-self.val)
        node.children.append((-self.der, self))
        node.op = 'neg'
        return node

    def __add__(self, other):
        try:
            node = ReverseAutoDiff(self.val+other.val)
            node.children.append((other.der, other))
            node.children.append((self.der, self))
        except AttributeError:
            node = ReverseAutoDiff(self.val+other)
            other_node = ReverseAutoDiff(other)
            node.children.append((0.0*self.der, other_node))
            node.children.append((self.der, self))
        node.op = 'add'
        return node
            
        
    def __radd__(self, other): 
        return self.__add__(other)
          
    def __mul__(self, other):
        try:
            node = ReverseAutoDiff(self.val*other.val)
            node.children.append((other.val*self.der, self))
            node.children.append((self.val*other.der, other))
        except AttributeError:
            node = ReverseAutoDiff(self.val*other)
            other_node = ReverseAutoDiff(other)
            node.children.append((other_node.val*self.der, self))
            node.children.append((0.0*self.der, other_node))
        node.op = 'mul'
        return node

    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __sub__(self, other):
        try:
            node = ReverseAutoDiff(self.val-other.val)
            node.children.append((1.0, self))
            node.children.append((-1.0, other))
        except AttributeError:
            node = ReverseAutoDiff(self.val-other)
            other_node = ReverseAutoDiff(other)
            node.children.append((1.0, self))
            node.children.append((0, other_node))
        node.op = 'sub'
        return node
    
    def __rsub__(self, other): 
        node = ReverseAutoDiff(other - self.val)
        other_node = ReverseAutoDiff(other)
        node.children.append((-1.0, self))
        node.children.append((0, other_node))
        node.op = 'sub'
        return node
    
    def reverse_mode(self):
        # recurse only if the value is not yet cached
        if self.grad_value is None:
            self.grad_value = 0
            # calculate derivative using chain rule
            if len(self.children) == 0:
                return 1
            for der, node in self.children:
                self.grad_value += (der * node.reverse_mode())
        return self.grad_value
    
    def graph(self):
        if len(self.children) == 0:
            print("leaf node: ", self.val )
        else:
            print("Op node: ", self.op , " Value: ",  self.val)
            for der, node in self.children:
                node.graph()

x = ReverseAutoDiff(4)
y = ReverseAutoDiff(0.5)
z = ReverseAutoDiff(5)


a = 4 + y * x 
b = z - 2
print("reverse mode res is ", a.reverse_mode())
print("function value is ", a.val)
print("reverse mode res is ", b.reverse_mode())
print("function value is ", b.val)

a.graph()

x = ReverseAutoDiff(4,1,2,1)
y = ReverseAutoDiff(0.5,1,2,0)
z = ReverseAutoDiff(5)


a = 4 + y * x 
print("reverse mode res is ", a.reverse_mode())