""" Problem
 Given an Array A of N integers.You have to find number of subarrays having Primicity less than or equal to K.

 of sub-array is defined an number of primes in that subarray."""


def array_element(num_roses, args):
    lists = [[]]
    for i in range(len(args) + 1):
        for j in range(i):
            lists.append(args[j:i])
    return lists










print(array_element(5,[1,2,5,3,4]))