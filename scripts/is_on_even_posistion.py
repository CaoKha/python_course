def is_on_even_posistion(table,value):
    answer = []
    for idx,item in enumerate(table):
        if (item == value):
            if (idx % 2 == 0): 
                return True
    return False
            

t = [9,8,7,6,6,5,4,3,2,1,0]
print(is_on_even_posistion(t,6))