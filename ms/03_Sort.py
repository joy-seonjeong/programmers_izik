#!/usr/bin/env python
# coding: utf-8

# In[40]:


# code description
# Author : minsik.lee
# FileName : 03_Sort.py
# Note 
	# @Summary : Sort 01. K 번쨰 수
	# @version 1.0 : (2020-12-14) 
# 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.

def solution(array, commands): 
    # command_i[0] - 1 : first element
    # command_i[1] : last element
    # command_i[2] : sort & n'th element 
    result = list(map(lambda command_i:sorted(array[(command_i[0]-1): command_i[1]])[(command_i[2]-1)], commands))
    return result


# In[43]:


def main_1():
    array = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

    print(solution(array, commands))     # return [5, 6, 3]


# In[44]:


if __name__ == "__main__":
    main_1()


# In[70]:


# code description
# Author : minsik.lee
# FileName : 03_Sort.py
# Note 
	# @Summary : Sort 02. 가장 큰 수
	# @version 1.0 : (2020-12-17) 
    # @version 2.0 : (2020-12-18) case 0, 0, 0, 0

def solution(numbers):
    answer = sorted(list(map(str, numbers)), key=lambda number_i:number_i*3, reverse=True)
    # # [(str(number_i) * 3) for number_i in numbers] # ['333', '303030', '343434', '555', '999']

    # answer = ''.join(answer)
    answer = str(int(''.join(answer)))
    return answer


# In[67]:


def main_2():
    numbers = [3, 30, 34, 5, 9]
    # numbers = [0, 0, 0, 0]


    print(solution(numbers))     # return [5, 6, 3]


# In[68]:


if __name__ == "__main__":
    main_2()


# In[39]:


# code description
# Author : minsik.lee
# FileName : 03_Sort.py
# Note 
	# @Summary : Sort 03. H-Index
	# @version 1.0 : (2020-12-18) 