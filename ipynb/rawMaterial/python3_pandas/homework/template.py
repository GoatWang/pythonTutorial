from numpy import dot
from numpy.linalg import norm
import pandas as pd
from collections import Counter
import re
#Problem 1 ( Cosine Similarity )
def cosine_similarity(A,B):
    ### write your code here ###
    result_value = float()
    return result_value

#Problem 2 ( Grades )
def grades(file_path):
    dict_grades = dict()
    tuple_grades = []
        
    return dict_grades, tuple_grades

#Problem 3 ( The valid of password )
def valid_password(passwords):
    result_list = list()    
    return result_list

if __name__ == "__main__":
    pro_1_value = cosine_similarity([1,2,3],[4,5,6])
    pro_2_dict, pro_2_tuple = grades('./example.csv')
    pro_3_list = valid_password(['Ab12!','AA1234!?','AbCdEfGh','12345AaBa!', '12Zz!?98Aa#@'])
    print (pro_1_value)
    print (pro_2_dict)
    print (pro_2_tuple)
    print (pro_3_list)



