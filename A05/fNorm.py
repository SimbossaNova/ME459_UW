# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 15:22:12 2023

@author: jacob
"""


import numpy as np
import argparse

parser = argparse.ArgumentParser(description = 'Input a filename without the .csv at the end please. It wll not work otherwise ')
parser.add_argument('filename')
args = parser.parse_args()
input_file = args.filename
input_file = input_file + '.csv'
numpy_csv = np.loadtxt(input_file, delimiter=",", dtype=str)

frobenius = np.linalg.norm(numpy_csv)

print(frobenius)