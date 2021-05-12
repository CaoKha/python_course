import math
def closest_to_zero(ints):
    if not ints:
        return 0
    else:
        neg = []
        pos = []
        for value in ints:
            if value < 0:
                neg.append(value)
            else:
                pos.append(value)
        if (neg != []):
            max_neg= max(neg)
        else:
            max_neg=-math.inf
        if (pos != []):
            min_pos= min(pos)
        else:
            min_pos= math.inf
        if (-max_neg < min_pos):
            return max_neg
        else:
            return min_pos    

ints = [-8,-8,-2,-8,-8]
result = closest_to_zero(ints)
print(result)    
# triple_quote_example = '''this is a sentence written in triple quotes'''
# print(triple_quote_example)
# for c in list(triple_quote_example):
#     print(c)
# for c in triple_quote_example:
#     print(c)
# with triple_quote_example as c:
#     print(c)