def add_num(number):

 num:int =  0
for i in  number: 
    num += i
 return num

def num():
    numbers :list[int] = [1,2,3,4,5,6,7,8,9]
    sum = add_num(numbers)

print(sum)

if __name__ == "__main__":
    num()