def pipeline(*funcs):
    def helper(arg):
        for element in funcs:
            arg = element(arg)
        return arg
    return helper


fun = pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2)
print(fun(3))