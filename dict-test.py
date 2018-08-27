
class sum1:
    def __init__(self, dict1):
        self.sum = 0
        self.dict1 = dict1

    def cal_total(self):
        for k, v in self.dict1.items():
            self.sum = self.sum + v
        return self.sum

dict1 = {'a': 23, 'b': 32}
obj1 = sum1(dict1)
sum_dict1 = obj1.cal_total()
print(sum_dict1)

''' 
#without class        
def total(a):
    sum = 0
    for k,v in a.items():
        sum = sum + v
    return sum

dict1 = {'a': 8, 'b': 2, 'c': 23}

total1 = total(dict1)

print(total1)
'''