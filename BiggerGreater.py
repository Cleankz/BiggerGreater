import random
def factor(num): # считает факториал числа
    factorial = 1
    for i in range(2, num+1):
        try:
            factorial *= i
        except OverflowError:
            print("OverFlowError!!!")
    return factorial



def BiggerGreater(inp): # функция ищет наибольшее значение
    count =  factor(len(inp)) * len(inp)
    varity = []
    varity.append(inp)
    string = list(inp)
    for i in range(count):
        s1 = random.randint(0,(len(inp) - 1))
        s2 = random.randint(0,(len(inp) - 1))
        string[s1],string[s2] = string[s2],string[s1]
        if "".join(string) not in varity:
            varity.append("".join(string))
    varity.sort()
    done = False # флажок обозначающий что значение найдено
    for i in range(len(varity)):
        if varity[i] > inp:
            done = True
            result = varity[i]
            break
    if done:
        return result
    else:
        return ""
