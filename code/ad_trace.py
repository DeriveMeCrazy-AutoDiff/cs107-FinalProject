import operand
import ad_trace_elem


class ad_trace:

    def __init__(self, input_vals, function_string):
        #If I understand correctly we can get this number from the length of the list of variable_list
        self.input_vals = input_vals # determines how many derivatives are needed at each trace step
        self.status = "incomplete"
        self.function_string = function_string
        self.elements_dict = {} #initialize the dictionary holding all our operands and symbols 
        #self.function_parser = function_parser(function_string)

    def forward_mode(self):
        pass

    def display_graph(self):
        #print out the graph representation of our function
        if self.status == "incomplete":
            raise Exception("Cannot print partial graph, call forward_mode first to complete calculation")
        else:
            #Show graph 
            pass
    
    def print_table(self):
        #print the completed formatted table 
        if self.status == "incomplete":
            raise Exception("Cannot print partial table, call forward_mode first to complete calculation")
        else:
            for element in self.elements:
                print(element)