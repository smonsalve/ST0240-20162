import random

cant   = int(raw_input())
lim_sup = int(raw_input())

def var_col(lim_sup, col = 3):
    resp = ""
    for i in range(col):
        resp += str(random.randint(0, lim_sup)).rjust(len(str(lim_sup))) + " "
    resp += "\n"
    return resp

for i in range(cant):
    print var_col(lim_sup, 6)

