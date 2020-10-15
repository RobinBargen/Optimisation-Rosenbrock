#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 17:28:06 2020

@author: Robin von Bargen
"""
import random
import pyomo.environ

class Rosenbrock:
    def __init__(self, number_of_dimensions, initial_variable_values = None):
        # Create model
        self.__model = pyomo.environ.ConcreteModel()
        
        # Specify variable ranges
        self.__model.iterator_i = range(number_of_dimensions - 1)
        
        # Add variables to model
        self.__model.variable_x = pyomo.environ.Var(self.__model.iterator_i)
        
        # Initialise variables
        self.__init_variables(self.__model.variable_x, number_of_dimensions, initial_variable_values)
        
        # Define objective function
        self.__objective_function_expression = self.__objective_function(self.__model.variable_x, number_of_dimensions)
        self.__model.objective_function = pyomo.environ.Objective(
                expr = self.__objective_function_expression,
                sense = pyomo.environ.minimize
        )
        
        self.__result = None
    
    def get_result(self):
        return self.__result
    
    def __init_variables(self, model_variable, number_of_dimensions, initial_variable_values = None):
        if(initial_variable_values is not None):
            for d in range(number_of_dimensions - 1):
                model_variable[d] = initial_variable_values[d]
        else:
            random.seed()
            for d in range(number_of_dimensions - 1):
                lower_initial = 1
                upper_initial = 15
                model_variable[d] = random.randrange(lower_initial, upper_initial)
        
    
    def __objective_function(self, x, number_of_dimensions):
        d = number_of_dimensions - 1
        return sum(100 * (x[i + 1] - x[i]**(2))**(2)  + (x[i] - 1)**(2) for i in range(d - 1))
    
    def print_model(self):
        self.__model.pprint()
        self.__model.objective_function.pprint()
        
    def solve_model(self):
        optimiser = pyomo.opt.SolverFactory('ipopt')
        optimiser.solve(self.__model)
        result = []
        for i in self.__model.variable_x:
            result.append(self.__model.variable_x[i].value)
        self.__result = result
            
        
    