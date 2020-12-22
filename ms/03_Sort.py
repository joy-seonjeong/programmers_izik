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

# # 홀수 케이스

# [3, 0, 6, 1, 5] # n = 5
#      A = h, B < h
#     (A, B)
# 6 - (1, 4)
# 5 - (2, 3)
# 3 - (3, 2) V
# 1 - (4, 1)
# 0 - (5, 0)

# # 짝수 케이스
# [3, 0, 6, 1, 5, 4] # n = 6
#      A = h, B < h
#     (A, B)
# 6 - (1, 5)
# 5 - (2, 4)
# 4 - (3, 4)
# 3 - (4, 2) V
# 1 - (5, 1)
# 0 - (6, 0)

# # 차이가 큰 케이스
# [1000, 999, 888, 777, 666, 555, 3, 1] # n = 7
# 1000 - (1, 6)
# 999  - (2, 5)
# 888  - (3, 4)
# 777  - (4, 3) V
# 666  - (5, 2)
# 3    - (6, 1)
# 1    - (7, 1)

# ## 동일 숫자 .. 짝수
# [3, 0, 6, 6, 6, 5] # = 6

# 6 - (1, 3) ... (1, 5)
# 6 - (1, 3) ... (2, 4)
# 6 - (1, 3) ... (3, 3)
# 5 - (4, 2) V
# 3 - (3, 1)
# 0 - (6, 0)


def solution(citations):
    citations = sorted(citations, reverse=True)
    return citations[int(len(citations)/2)]
    # if len(citations) % 2 == 1: # odd
    #     return citations[int(len(citations)/2)]
    # else:
    #     return citations[int(len(citations)/2) + 1]


# In[42]:


citations = [1000, 999, 888, 777, 666, 555, 3, 1] 
print('result - ', solution(citations))
citations = sorted(citations, reverse=True)
print(citations)
print(len(citations) % 2, '    ', len(citations)/2)


# In[43]:


citations = [0, 0, 0, 0, 0, 1]
citations = sorted(citations, reverse=True)
citations

     A = h, B < h
    (A, B)
1 - (1, 5)


# In[30]:


int(len(citations)/2)


# In[ ]:


# 짝수 케이스
[3, 0, 6, 1, 5, 4] # n = 6
     A = h, B < h
    (A, B)
6 - (1, 5)
5 - (2, 4)
4 - (3, 3) V
3 - (4, 2) 
1 - (5, 1)
0 - (6, 0)

# 차이가 큰 케이스
[1000, 999, 888, 777, 666, 555, 3, 1] # n = 8
1000 - (1, 7)
999  - (2, 6)
888  - (3, 5)
777  - (4, 4) V
666  - (5, 2)
555  - (6, 2)
3    - (7, 1)
1    - (8, 0)

## 동일 숫자 .. 짝수
[3, 0, 6, 6, 6, 5] # = 6

6 - (1, 3) ... (1, 5)
6 - (1, 3) ... (2, 4)
6 - (1, 3) ... (3, 3)
5 - (4, 2) V
3 - (3, 1)
0 - (6, 0)


# In[3]:


citations = [3, 0, 6, 1, 5] 


# In[6]:


citations = sorted(citations, reverse=True)


# In[20]:


citations = sorted(citations, reverse=True)

if len(citations) % 2 == 1: # odd
    return citations[int(len(citations)/2)]
else:
    return citations[int(len(citations)/2) + 1]


# In[21]:


citations[int(len(citations)/2)]

