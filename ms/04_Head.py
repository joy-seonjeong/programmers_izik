import heapq
# https://seoyoung2.github.io/algorithm/2020/06/04/Programmers-diskcontroller.html

def solution(jobs):
    count, last, answer = 0, -1, 0
    heap = []
    jobs.sort()
    # 시작시간 초기화
    current_time = jobs[0][0]
    while count < len(jobs):
        for ticket_time, running_time in jobs:
            # ticket_time : 1개의 요청이 들어온 시간
            # running_time : 1개의 작업이 수행되는 시간
            if last < ticket_time <= current_time:
                # 작업 소요시간으로 min heap을 만들기 위해 (running_time, ticket_time) 푸시
                heapq.heappush(heap, (running_time, ticket_time))
        # 바로 수행할 수 있는 작업이 있는 경우
        if len(heap) > 0:
            count += 1
            last = current_time # 마지막으로 answer 입력된 task의 수행 시작 시점
            running_time_i, ticket_time_i = heapq.heappop(heap)
            current_time += running_time_i
            answer += (current_time - ticket_time_i)
        # 바로 수행할 수 있는 작업이 없는 경우
        else:
            current_time += 1
    return answer//len(jobs) # 소수점 버림


print(solution([[0, 3], [1, 9], [2, 6]]))



# code description ***
# Author : minsik.lee
# FileName : 04_HeapT.py
# Note 
	# @Summary : 코딩테스트 - 프로그래머스 Question (3)
	# @version 1.0 : (2021-01-05) https://seoyoung2.github.io/algorithm/2020/06/04/Programmers-diskcontroller.html
    # @version 2.0 : (2021-01-05) 내가 이해할 수 있는 주석으로 변경

    # 결국에 키는 ticket_time, running_time 을 변경해서 heap 에 넣고 min 으로 추출 

import heapq

def solution(jobs):
    count, last, answer = 0, -1, 0
    heap = []
    jobs.sort() # 짧은 시간 순서로
    # 시작시간 초기화
    current_time = jobs[0][0] # 0초, 10초, 40초
    while count < len(jobs):
        for ticket_time, running_time in jobs:
            # ticket_time : 1개의 요청이 들어온 시간
            # running_time : 1개의 작업이 수행되는 시간
            if last < ticket_time <= current_time:
                # 작업 소요시간으로 min heap을 만들기 위해 (running_time, ticket_time) 푸시
                heapq.heappush(heap, (running_time, ticket_time))
        # 바로 수행할 수 있는 작업이 있는 경우
        if len(heap) > 0:
            count += 1
            last = current_time # 마지막으로 answer 입력된 task의 수행 시작 시점
            running_time_i, ticket_time_i = heapq.heappop(heap)
            current_time += running_time_i
            answer += (current_time - ticket_time_i)
        # 바로 수행할 수 있는 작업이 없는 경우
        else:
            current_time += 1
    return answer//len(jobs)


print(solution([[0, 3], [1, 9], [2, 6]]))


# code description ***
# Author : minsik.lee
# FileName : 04_HeapT.py
# Note 
	# @Summary : 코딩테스트 - 프로그래머스 Question (3) Heap (3)
	# @version 1.0 : (2021-01-13)

    # I : insert _ number
    # D : delete {max(n > 0), min(n < 0)}

# coding sketch
# (1) 기본 I/D 부터 만들기
#       min heap 으로 정렬
#       max 구하는 방식 
# (2) return 
#       비어있는 경우 
#       최대,최소 반환 경우


# 채점을 시작합니다.
# 정확성  테스트
# 테스트 1 〉	통과 (0.04ms, 10.4MB)
# 테스트 2 〉	통과 (0.03ms, 10.3MB)
# 테스트 3 〉	통과 (0.04ms, 10.4MB)
# 테스트 4 〉	통과 (0.03ms, 10.3MB)
# 테스트 5 〉	통과 (0.03ms, 10.4MB)
# 테스트 6 〉	통과 (0.03ms, 10.4MB)
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

import heapq

def solution(operations):    
    heap = []

    for operation_i in operations:
        # operator 연산자
        # number action하는 숫자 
        operator, number = operation_i.split() 
        number = int(number)
        # D/I 연산 
        if operator == 'I':
            heapq.heappush(heap, number)
        elif len(heap) > 0 : # delete
            if number < 0:
                heapq.heappop(heap)
            else: # max heap
                maxN = heapq.nlargest(1, heap)[0] # 최대 값 반환
                heap.pop(heap.index(maxN)) # 최대 값의 index 삭제 (list)
        else: # delete - empty heap
            pass

    if len(heap) == 0:
        return [0, 0]
    else:
        minN = heap[0]
        maxN = maxN = heapq.nlargest(1, heap)[0] 
        return [maxN, minN]






# code description ***
# Author : minsik.lee
# FileName : 04_HeapT.py
# Note 
	# @Summary : 코딩테스트 - 프로그래머스 Question (3) Heap (3)
	# @version 1.0 : (2021-01-13)

    # I : insert _ number
    # D : delete {max(n > 0), min(n < 0)}

# coding sketch
# (1) 기본 I/D 부터 만들기
#       min heap 으로 정렬
#       max 구하는 방식 
# (2) return 
#       비어있는 경우 
#       최대,최소 반환 경우


# 채점을 시작합니다.
# 정확성  테스트
# 테스트 1 〉	통과 (0.04ms, 10.4MB)
# 테스트 2 〉	통과 (0.03ms, 10.3MB)
# 테스트 3 〉	통과 (0.04ms, 10.4MB)
# 테스트 4 〉	통과 (0.03ms, 10.3MB)
# 테스트 5 〉	통과 (0.03ms, 10.4MB)
# 테스트 6 〉	통과 (0.03ms, 10.4MB)
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

import heapq

def solution(operations):    
    heap = []

    for operation_i in operations:
        # operator 연산자
        # number action하는 숫자 
        operator, number = operation_i.split() 
        number = int(number)
        # D/I 연산 
        if operator == 'I':
            heapq.heappush(heap, number)
        elif len(heap) > 0 : # delete
            if number < 0:
                heapq.heappop(heap)
            else: # max heap
                maxN = heapq.nlargest(1, heap)[0] # 최대 값 반환
                heap.pop(heap.index(maxN)) # 최대 값의 index 삭제 (list)
        else: # delete - empty heap
            pass

    if len(heap) == 0:
        return [0, 0]
    else:
        minN = heap[0]
        maxN = maxN = heapq.nlargest(1, heap)[0] 
        return [maxN, minN]


operations = ["I 7","I 5","I -5","D -1"]
solution(operations)