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
    return answer//len(jobs)


print(solution([[0, 3], [1, 9], [2, 6]]))