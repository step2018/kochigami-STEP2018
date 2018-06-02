#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
reference: https://github.com/xharaken/step2015/blob/master/matrix.py
'''

import numpy, sys, time
import matplotlib.pyplot as plt

if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print "usage: python %s N" % sys.argv[0]
        sys.exit()

    x = []
    y = []
    for n in xrange(1, int(sys.argv[1])+1):
        x.append(n)
        a = numpy.zeros((n, n)) # Matrix A
        b = numpy.zeros((n, n)) # Matrix B
        c = numpy.zeros((n, n)) # Matrix C

        # Initialize the matrices to some values.
        for i in xrange(n):
            for j in xrange(n):
                a[i, j] = i * n + j
                b[i, j] = j * n + i
                c[i, j] = 0

        begin = time.time()

        ######################################
        # Write code to calculate C = A * B. #
        ######################################
        for i in xrange(n):
            for k in xrange(n):
                for j in xrange(n):
                    c[i, k] += a[i, j] * b[j, k]

        end = time.time()
        y.append(end - begin)
        
    plt.plot(x, y)
    plt.title("test")
    plt.show()
