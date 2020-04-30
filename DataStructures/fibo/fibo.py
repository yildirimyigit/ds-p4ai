"""
  @author: yigit.yildirim@boun.edu.tr
"""

import matplotlib.pyplot as plt

# def recursive_fibo(n):
#     # fibo = recursive_fibo(n-1) + recursive_fibo(n-2)
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return recursive_fibo(n-1) + recursive_fibo(n-2)
#
#
# for i in range(20):
#     print(recursive_fibo(i))


def fibo(n):  # n >= 2 varsayımında
    fn_2, fn_1 = 0, 1
    print(fn_2)
    print(fn_1)
    golden_ratio = []
    for i in range(2, n):
        f = fn_2 + fn_1
        fn_2 = fn_1
        fn_1 = f
        golden_ratio.append(fn_1/fn_2)
        print(f'{f}: {fn_1/fn_2}')

    return golden_ratio


num = 50
gr = fibo(num)
plt.plot(list(range(len(gr))), gr)
plt.show()





