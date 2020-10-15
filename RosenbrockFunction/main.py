#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 22:11:28 2020

@author: Robin von Bargen
"""
import Rosenbrock

def main():
    number_of_dimensions = 3
    
    rosenbrock = Rosenbrock.Rosenbrock(number_of_dimensions)
    rosenbrock.print_model()
    rosenbrock.solve_model()
    
    result = rosenbrock.get_result()
    print("\nResult: " + str(result))

if __name__ == "__main__":
    main()