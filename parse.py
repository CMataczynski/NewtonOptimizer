import parser
from math import *
import re
import numpy as np

class FunctionParse:
    def __init__(self, input_string):
        self.variable_dict = {}
        self.number_of_variables = 0
        for i in range(1, 6):
            expression = 'x' + str(i)
            if re.search(expression, input_string) is not None:
                self.variable_dict[expression] = True
                self.number_of_variables = self.number_of_variables + 1
            else:
                self.variable_dict[expression] = False
        input_string = input_string.replace("^","**")
        self.code = parser.expr(input_string).compile()

    def get_value_matrix(self,variables, dx):
        value_matrix = np.zeros((self.number_of_variables, 3))
        iterator = 0
        for key in variables:
            variables_left = dict()
            variables_left.update(variables)
            variables_left.update({key:(variables[key] - dx)})
            variables_right = dict()
            variables_right.update(variables)
            variables_right.update({key:(variables[key] + dx)})
            value_matrix[iterator,0] = self.evaluate_expression(variables_left)
            value_matrix[iterator,1] = self.evaluate_expression(variables)
            value_matrix[iterator,2] = self.evaluate_expression(variables_right)
            iterator = iterator + 1
        return  value_matrix

    def evaluate_expression(self, variables):
        for key in self.variable_dict:
            if self.variable_dict[key] is True:
                exec(str(str(key) + ' = ' + str(variables[key])))
        return eval(self.code)

    def evaluate_list(self,list):
        for i, item in enumerate(list):
            exec("x"+str(i+1)+ ' ' + str(item))
        return eval(self.code)

    def evaluate_gradient(self,variables, dx = 1e-6):
        value_matrix = self.get_value_matrix(variables,dx)
        gradient_matrix = np.array(np.gradient(value_matrix,dx))
        return gradient_matrix[1,:,1]

    def evaluate_hessian(self,variables, dx = 1e-6):
        hes_mtx = []
        for key in variables:
            point_gradient = self.evaluate_gradient(variables,dx)
            left_variables = dict()
            left_variables.update(variables)
            left_variables.update({key:(variables[key]-dx)})
            left_gradient = self.evaluate_gradient(left_variables,dx)
            right_variables = dict()
            right_variables.update(variables)
            right_variables.update({key:(variables[key]+dx)})
            right_gradient = self.evaluate_gradient(right_variables,dx)
            val_mtx = np.array([left_gradient,point_gradient,right_gradient]).T
            hes_row = np.array(np.gradient(val_mtx,dx))
            hes_mtx.append(hes_row[1,:,1])
        hes_mtx = np.array(hes_mtx)
        return hes_mtx


