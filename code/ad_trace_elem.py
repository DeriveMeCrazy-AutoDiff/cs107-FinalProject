class ad_trace_elem:

    def __init__(parent_ad_trace, operation, op_list):
        self.parent_ad_trace = parent_ad_trace
        self.derivs = [] #value of our current node partial derivatives that are calculated 
        self.operation = operation # operation to be used for updating the trace (as a string, e.g 'sin')
        #we can have one or two depending on the type
        self.operands = op_list 
        self.curr_operand = operand(1)
        self.curr_operand.set_value = "x" + self.parent_ad_trace.elements_dict.size()
        self.nodes = []
        nodes = []
        for op in op_list:
            if op.op_type == 1: 
                self.nodes.append(self.parent_ad_trace.elements_dict[op.get_op_string])
            else: 
                self.nodes.append(op.get_value)
        evaluate()
        
    def get_val_deriv():
        return (self.value, self.derivs)
    
    def __str__():
        #Go over element attributes and return a string of this table row 
        element_string = ""
        return element_string

    def evaluate():
        #uses previous node's values and the overloaded operation function 
        #To obtain and calculate the value of the current node 
        #We will have a sort of Switch statement here for operation selection 
        res = None
        if self.operation == None: #this is an input only node, single operand in op_list
            self.val_func = self.parent_ad_trace.input_vars[0]
            self.derivs.append(1)
        elif self.operation == 'add':
            res = nodes[0] + nodes[1]
        elif self.operation == 'mul':
            res = nodes[0] * nodes[1]
        elif self.operation == 'sub':
            res = nodes[0] - nodes[1]
        elif self.operation == 'div':
            res = nodes[0] / nodes[1]
        elif self.operation == 'pow':
            #res = nodes[0] ** nodes[1] 
            pass
        elif self.operation == 'exp':
            #res = exp(nodes[0])
            pass
        elif self.operation == 'sqrt':
            #res = sqrt(nodes[0])
            pass
        elif self.operation == 'sin':
            #res = sin(nodes[0])
            pass
        elif self.operation == 'sinh':
            #res = sinh(nodes[0])
            pass
        elif self.operation == 'cos':
            #res = cos(nodes[0])
            pass
        elif self.operation == 'cosh':
            #res = cosh(nodes[0])
            pass
        elif self.operation == 'tan':
            #res = tan(nodes[0])
            pass
        elif self.operation == 'tanh':
            #res = tanh(nodes[0])
            pass
        self.val_func = res.val
        self.derivs[0] = res.der
        self.parent_ad_trace.elements_dict[self.curr_operand.get_op_string] = self
    
    def __add__(self, other):
        res = None
        if type(other) == ad_trace_elem:
            res.val = other.val_func + self.val_func
            res.der = other.derives[0] + self.derives[0]
        else:
            res.val = (other*1.0) + self.val_func
            res.der = self.derives[0]
        return res
    
    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        res = None
        if type(other) == ad_trace_elem:
            res.val = self.val_func - other.val_func
            res.der = self.derives[0] - other.derives[0]
        else:
            res.val = self.val_func - (other*1.0)
            res.der = self.derives[0]
        return res
    
    def __rsub__(self, other):
        res = None
        if type(other) == ad_trace_elem:
            res.val = other.val_func - self.val_func
            res.der = other.derives[0] - self.derives[0]
        else:
            res.val = (other*1.0) - self.val_func
            res.der = (-1.0)*self.derives[0]
        return res
    
    def __mul__(self, other):
        res = None
        if type(other) == ad_trace_elem:
            res.val = self.val_func*(1.0) * other.val_func
            res.der = self.derives[0]*1.0*other + other.derives[0]*1.0*self
        else:
            res.val = self.val_func * (other*1.0)
            res.der = (other*1.0)
        return res
    
    def __rmul__(self, other):
        return self.__mul__(other)
        return res
    
    def __div__(self, other): #self/other
        res = None
        if type(other) == ad_trace_elem:
            res.val = (self.val_func*1.0) / other.val_func
            res.der = self.derives[0]*1.0*other + other.derives[0]*1.0*self
            res.der = res.der / (self*self)
        else:
            res.val = self.val_func / (other*1.0)
            res.der = self.derives[0]*1.0 / (other*1.0)
        return res
    
    def __rdiv__(self, other): #other/self
        res = None
        if type(other) == ad_trace_elem:
            res.val = (other.val_func*1.0) / self.val_func
            res.der = other.derives[0]*1.0*self + self.derives[0]*1.0*other
            res.der = res.der / (self*self)
        else:
            res.val = (other*1.0) / self.val_func
            res.der = (other*1.0) / (self*self)
        return res

    ## operator overloads for all elementary functions
