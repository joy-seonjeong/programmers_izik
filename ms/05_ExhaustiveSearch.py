#!/usr/bin/env python
# coding: utf-8

# In[6]:


# code description ***
# Author : minsik.lee
# FileName : 05_ExhaustiveSearch.py
# Note 
	# @Summary : 코딩테스트 - 프로그래머스 Question (5) - 모의고사
	# @version 1.0 : (2021-01-22) draft


# 테스트 1 〉	통과 (0.02ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.3MB)
# 테스트 4 〉	통과 (0.01ms, 10.3MB)
# 테스트 5 〉	통과 (0.04ms, 10.3MB)
# 테스트 6 〉	통과 (0.04ms, 10.3MB)
# 테스트 7 〉	통과 (2.47ms, 10.3MB)
# 테스트 8 〉	통과 (0.66ms, 10.4MB)
# 테스트 9 〉	통과 (4.26ms, 10.3MB)
# 테스트 10 〉	통과 (2.06ms, 10.3MB)
# 테스트 11 〉	통과 (4.49ms, 10.3MB)
# 테스트 12 〉	통과 (4.08ms, 10.3MB)
# 테스트 13 〉	통과 (0.81ms, 10.2MB)
# 테스트 14 〉	통과 (4.73ms, 10.3MB)



def solution(answers):
    # Rule of man
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # How many answer correct
    count = {
        1 : 0,
        2 : 0,
        3 : 0
    }

    # 정답지 loop
    p1_len = 5
    p2_len = 8
    p3_len = 10

    for i in range(len(answers)): # for idx, answer in enumerate(answers):

        idx1 = i%p1_len
        idx2 = i%p2_len
        idx3 = i%p3_len

        answer_i = answers[i]

        # True : 1, False : 2
        count[1] += (answer_i == p1[idx1])
        count[2] += (answer_i == p2[idx2])
        count[3] += (answer_i == p3[idx3])

    answer = [k for k, v in count.items() if v == max(count.values())]
    
    return answer


# In[ ]:


# code description ***
# Author : minsik.lee
# FileName : 05_ExhaustiveSearch.py
# Note 
	# @Summary : 코딩테스트 - 프로그래머스 Question (5).2 - 소수 찾기 
	# @version 1.0 : (2021-01-24) draft


# 테스트 1 〉	통과 (0.24ms, 10.4MB)
# 테스트 2 〉	통과 (150.97ms, 10.4MB)
# 테스트 3 〉	통과 (0.04ms, 10.4MB)
# 테스트 4 〉	통과 (7.02ms, 10.4MB)
# 테스트 5 〉	통과 (4.93ms, 10.8MB)
# 테스트 6 〉	통과 (0.04ms, 10.4MB)
# 테스트 7 〉	통과 (0.16ms, 10.5MB)
# 테스트 8 〉	통과 (4.93ms, 10.9MB)
# 테스트 9 〉	통과 (0.05ms, 10.4MB)
# 테스트 10 〉	통과 (2113.60ms, 10.5MB)
# 테스트 11 〉	통과 (73.69ms, 10.4MB)
# 테스트 12 〉	통과 (1.10ms, 10.3MB)

import itertools

def is_prime(n):
    
    if n < 2: # 1은 소수가 아님 
        return False

    for x in range(2, n): 
        if n%x == 0: # 나머지가 9인 경우 소수가 아님
            return False
    return True

def return_permutation(number_list):
    
    result = []
    for _r in range(1, (len(number_list)+1)):
        nPr = itertools.permutations(number_list, r=_r)
        # element = list(set(nPr))
        element = nPr
        int_element = [int(''.join(sub_element)) for sub_element in element]
        result.extend(int_element)
    result = list(set(result)) # 중복 제거
    return result


def solution(numbers):
    numbers_permutation = return_permutation(numbers)
    answer = [x for x in numbers_permutation if is_prime(x)]
    return len(answer)


# In[ ]:


numbers = '17'
numbers_permutation = return_permutation(numbers)
answer = [x for x in numbers_permutation if is_prime(x)]
answer


# In[133]:


# code description ***
# Author : minsik.lee
# FileName : 05_ExhaustiveSearch.py
# Note 
	# @Summary : 코딩테스트 - 프로그래머스 Question (5).3 - 카펫
	# @version 1.0 : (2021-01-26) draft

# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (54.42ms, 10.3MB)
# 테스트 4 〉	통과 (0.14ms, 10.1MB)
# 테스트 5 〉	통과 (0.82ms, 10.2MB)
# 테스트 6 〉	통과 (18.86ms, 10.1MB)
# 테스트 7 〉	통과 (69.03ms, 10.2MB)
# 테스트 8 〉	통과 (54.71ms, 10.2MB)
# 테스트 9 〉	통과 (67.65ms, 10.2MB)
# 테스트 10 〉	통과 (79.67ms, 10.3MB)
# 테스트 11 〉	통과 (0.00ms, 10.2MB)
# 테스트 12 〉	통과 (0.00ms, 10.2MB)
# 테스트 13 〉	통과 (0.01ms, 10.1MB)

# 1) total_tile = brown + yellow
# 2) yellow를 y_w * y_h 로 표현하여 y_w, y_h 쌍을 다 찾는다. (y_w >= y_h)
# 3) (y_w)에서 하나씩 빼면서 total_tile
# 4) total_tile = (y_w + 2) * (y_h + 2) # yellow 에서 가로, 세로 하나씩 추가해서 계산한 값

def solution(brown, yellow):
    total_tile = brown + yellow # 1)total_tile = brown + yellow
    for y_w in range(yellow, 0, -1): # 3) (y_w)에서 하나씩 빼면서 total_tile
        if yellow%y_w == 0: # 2) yellow를 y_w * y_h 로 표현하여 y_w, y_h 쌍을 다 찾는다. 
            y_h = yellow//y_w # type  : int
            if (y_w+2) * (y_h+2) == total_tile: # 4) total_tile = (y_w + 2) * (y_h + 2)
                return [(y_w+2), (y_h+2)]

