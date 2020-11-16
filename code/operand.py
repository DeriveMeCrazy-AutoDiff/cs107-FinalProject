from enum import Enum

#basic component enum
class op_type(Enum):
    Symbol = 1
    Value = 2

class operand():
    
    def __init__(self, op_type):
        self.op_type = op_type
    
    def set_value(self, op_val):
        self.op_val = op_val
    
    def get_value(self):
        return self.op_val
    
    def get_op_string(self):
        return "" + self.op_val
