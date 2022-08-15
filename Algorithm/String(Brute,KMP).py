'''
String 
Brute force 탐색 알고리즘을 이해를 통해 직접 구현해보자
'''

# target = 'isTh a isisisitargetis'   # 패턴 찾을 타겟 string
# pattern = 'is'                      # 패턴 string


# def Brute(target, pattern):         # 함수 선언
#     N = len(target)                 # N = 타겟 string의 길이
#     M = len(pattern)                # M = 패턴 string의 길이
#     i = 0                           # 타겟의 인덱스
#     j = 0                           # 패턴의 인덱스
#     count = 0                       # 타겟 내의 패턴의 수
#     while i < N and j < M:          # 타겟 길이 만큼 순회, 패턴 길이만큼 순회
#         if target[i] != pattern[j]: # 맞지 않다면
#             i = i - j               # 타겟에서는 j만큼 온 것만큼 돌아간 후 +1 해준 인덱스로 가야한다( -j + 1) 밑에서 +1 해주기 째문에 i - j
#             j = -1                  # j는 0으로 돌아가 자시 탐색 시작해야한다 밑에서 +1해주기 때문에 j = -1
#         i = i + 1                   # 틀린 경우 -j만큼한다음 +1핸다 맞은경우 다음 요소 탐색을 위해 +1
#         j = j + 1                   # 틀린경우 0으로 돌아가기위해 위에서 -1해준데에 +1 맞은경우 다음 요소 탐색 위해 +1
        
#         if j == M:                  # j가 M이라면 j의 길이만큼 일치했다는 의미
#             count += 1              # count +1
#             j = 0                   # 계속 탐색을 위해 j = 0
#         if i == N and count == 0:   # 타겟안에 패턴이 없다면
#             count = -1              # -1 출력
#     return count

    

# print(Brute(target, pattern))
            

'''
kmp알고리즘을 구현해보자
'''

# lps 구현
# lps: kmp 알고리즘을 위해 패턴 내의 반복을 찾아내 리스트화 한 후 타겟 탐색 시 돌아갈 인덱스를 미리 지정해 주는 것
# T : target / P : pattern

# def pre_process(P):
#     lps = [0] * len(P)

#     # lps를 만들기 위한 prefix에 대한 idx,
#     j = 0
    
#     """
#     i : pattern에서 지나가고 있는 id
#     j : 지나가고 있는 idx와 pattern의 앞부분과 같은 부분에 대한 idx
#     """

#     # 처음부터 끝까지 순회를 돌면서
#     for i in range(1, len(P)):
#         # i 와 j가 같으면 lps의 i 자리에 j+1을 넣어줍니다. (prefix idx 위치에 있는 char와 같으면 lps에 숫자 추가)
#         if P[i] == P[j]:
#             lps[i] = j + 1
#             j += 1
#         # 다르다면, j를 초기화 해주어 pattern의 가장 처음부터 인식하도록 합니다.
#         # 그 자리에서 기존의 j자리(비교를 하고 있던 자리)가 아닌 pattern 처음으로 돌아가 비교를 해줍니다.
#         else:
#             j = 0
#             if P[i] == P[j]:
#                 lps[i] = j + 1
#                 j += 1

#     return lps
# P = 'ABABABBA'
# lps = pre_process(P)
# print(lps)
# T = 'abcdabeeababcdabcef'








# def pre_process(P):
    
#     lps = [0] * len(P)
#     j = 0
    
#     for i in range(1, len(P)):
#         if P[i] == P[j]:
#             lps[i] = j + 1
#             j = j + 1
            
#         elif P[i] != P[j]:
#             j = 0
#             if P[i] == P[j]:
#                 lps[i] = j + 1
#                 j = j + 1
           
#     return lps



# def KMP(T, P):
#     lps = pre_process(P)
#     N = len(T)
#     M = len(P)
#     i = 0
#     j = 0
#     count = 0
    
#     while i < N and j < M:
#         if T[i] == P[j]:
#             i = i + 1
#             j = j + 1
        
#         else:
#             if j != 0:
#                 j = lps[j-1]
#             else:
#                 i += 1
  
#         if j == M:
#             count += 1
#     return count





def pre_process(P):
    lps = [0] * len(P)
    j = 0
    
    for i in range(len(P)):
        if P[i] == P[j]:
            lps[i] = j+1
            j = j + 1
            
        else:
            j = 0
            if P[i] == P[j]:
                lps[i] = j + 1
                j = j + 1
    return lps

def KMP(T, P):

    lps = pre_process(P)

    # i : text를 순회하는 index
    i = 0
    # j : pattern을 순회하는 index
    j = 0

    position = -1
    while i < len(T):
        # 같으면 이동
        if P[j] == T[i]:
            i += 1
            j += 1
        else:
            # 다른데 j가 0이 아니라면, i의 자리는 유지한 채 j만 이동하여 비교 시작
            if j != 0:
                j = lps[j - 1]
            # 다른데 j가 0이라면, i를 한칸만 이동하여 처음부터 진행하듯이 진행
            else:
                i += 1
        # j가 pattern을 다 순회하면 성공
        if j == len(P):
            position = i - j
            break

    return position


T = 'abcdabeeababcdabcef'
P = 'eaba'


position = KMP(T, P)
print(position)

