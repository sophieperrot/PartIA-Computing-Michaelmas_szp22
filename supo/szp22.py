#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def fibonacci(n):
    terms = [1, 1]
    try:
        for _ in range(n-2):
            terms.append(terms[-2] + terms[-1])
    except:
        pass
    return np.array(terms[:n])

def terms_ratio(sequence):
    return sequence[1:] / sequence[:-1] 

def plot_difference(sequence, value):
    x = np.array([i for i in range(len(sequence))])
    y = np.abs(sequence - value)
    plt.plot(x, y)
    plt.xlabel("Term-pair index")
    plt.ylabel("Difference")
    plt.yscale("log")
    plt.show()

def main():
    fib_40 = fibonacci(40)
    ratio_40 = terms_ratio(fib_40)
    golden_ratio = (1 + np.sqrt(5)) / 2
    plot_difference(ratio_40, golden_ratio)

if __name__ == "__main__":
    main()