import pytest
import ad_trace_elem.ad_trace_elem as ad_trace_elem
import ad_trace.ad_trace as ad_trace
import operand.operand as operand
#import ad_trace

#(parent_ad_trace, operation, op_list)
# (input_vals, function_string):

def test_input_node_result():
    x0 = operand(1)
    x0.set_value("x0")
    a = operand(2)
    a.set_value(5)
    x1 = operand(1)
    x1.set_value("x1")
    
    trace_table = ad_trace([1.5], "5*x0^2")
    elem_x0 = ad_trace_elem(trace_table, None, [x0])
    assert elem_x0.val_func == trace_table.input_vals[0]
    assert trace_table.elements_dict.has_key(x0.get_op_string())

def test_add_node_result():
    x0 = operand(1)
    x0.set_value("x0")
    a = operand(2)
    a.set_value(5)
    
    trace_table = ad_trace([1.5], "5+X0")
    ad_trace_elem(trace_table, None, [x0])
    ad_trace_elem(trace_table, "add", [x0,a])
    
    assert trace_table.elements_dict.has_key('x1')
    assert trace_table.elements_dict['x1'].val_func == 6.5
