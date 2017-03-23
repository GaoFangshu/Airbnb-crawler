# -*- coding: utf-8 -*-

def meancut(a, N_part):
    L=len(a)
    L_part = L/N_part
    b = []
    for i in range(0,len(a),L_part):
        b.append(a[i:i+L_part])
    c = [b[x] for x in range(N_part)]
    return c
