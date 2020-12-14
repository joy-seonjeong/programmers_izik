#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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


# In[ ]:


def main():
    array = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

    print(solution(array, commands))     # return [5, 6, 3]


# In[ ]:


if __name__ == "__main__":
    main()

