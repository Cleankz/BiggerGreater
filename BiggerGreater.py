import random
def factor(num):
    factorial = 1
    for i in range(2, num+1):
        factorial *= i
    return factorial



def BiggerGreater(inp):
    count =  factor(len(inp)) * len(inp)
    varity = []
    varity.append(inp)
    string = list(inp)
    flag = False
    for i in range(count):
        s1 = random.randint(0,(len(inp) - 1))
        s2 = random.randint(0,(len(inp) - 1))
        string[s1],string[s2] = string[s2],string[s1]
        if "".join(string) not in varity:
            varity.append("".join(string))
    varity.sort()
    for i in range(len(varity)):
        if varity[i] > inp:
            flag = True
            result = varity[i]
            break
    if flag:
        return result
    else:
        return ""