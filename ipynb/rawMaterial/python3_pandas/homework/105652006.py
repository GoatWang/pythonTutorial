from numpy import dot
from numpy.linalg import norm
import pandas as pd
from collections import Counter
import re
#Problem 1 ( Cosine Similarity )
def cosine_similarity(A,B):
    ### write your code here ###
    result_value = float(dot(A, B) / (norm(A) * norm(B)))

    return result_value

#Problem 2 ( Grades )
def grades(file_path):
    dict_grades = dict()
    tuple_grades = []
        
    persondist = pd.read_csv("example.csv").T.to_dict()

    grades = []
    for num, person in persondist.items():
        # your csv file column headers contain space
        newdict = {}
        for key in person.keys():
            newdict[key.replace(" ", "")] = person[key]

        interval = newdict['Score'] // 10 * 10
        intervalStr = str(interval) + "~" + str(interval+9)
        grades.append(intervalStr)
    
        tuple_grades.append((newdict['Name'], newdict['Age'], newdict['Score']))

    dict_grades = dict(Counter(grades))

    tuple_grades = sorted(tuple_grades, key=lambda x:(x[0],x[1],x[2]))

    with open('output.csv','w') as f:
        for item in tuple_grades:
            f.write(item[0] + ", " + str(item[1]) + ", " + str(item[2]) + "\n")

    return dict_grades, tuple_grades

#Problem 3 ( The valid of password )
def valid_password(passwords):
    result_list = list()    
    for pwd in passwords:
        upperCase = re.findall(r'[A-Z]',pwd)
        lowerCasae =  re.findall(r'[a-z]',pwd)
        numbers = len(re.findall(r'\d',pwd)) >= 2
        specialChar = re.findall(r'[%!\?#@$\*]', pwd)
        pwdLength = len(pwd) >= 5 and len(pwd) <=10
        print(pwd)
        print(upperCase)
        print(lowerCasae)
        print(numbers)
        print(specialChar)
        print(pwdLength)
        if upperCase and lowerCasae and numbers and specialChar and pwdLength:
            result_list.append(pwd)
    return result_list

if __name__ == "__main__":
    pro_1_value = cosine_similarity([1,2,3],[4,5,6])
    pro_2_dict, pro_2_tuple = grades('./example.csv')
    pro_3_list = valid_password(['Ab12!','AA1234!?','AbCdEfGh','12345AaBa!', '12Zz!?98Aa#@'])
    print (pro_1_value)
    print (pro_2_dict)
    print (pro_2_tuple)
    print (pro_3_list)



