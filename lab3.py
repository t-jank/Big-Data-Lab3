# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 18:50:44 2023

@author: t-jan
"""

def minHash(L, hash_functions):
    num_hashes = len(hash_functions)
    min_values = [float('inf')] * num_hashes

    for x in L:
        for i, hash_func in enumerate(hash_functions):
            hash_value = hash_func(x)
            min_values[i] = min(min_values[i], hash_value)

    return min_values

def hash_func1(x):
    return hash(x)  # Przykładowa funkcja haszująca

def hash_func2(x):
    return hash(x + "abc")  # Przykładowa funkcja haszująca

L = ["apple", "banana", "orange"]
hash_functions = [hash_func1, hash_func2]

result = minHash(L, hash_functions)
print(result)
