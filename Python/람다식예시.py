movie_5 = sorted(list_movie, key = lambda d:(d['vote_average'], d['id']), reverse=True)

# movie_5에 list_movie 대상으로 key값 기준 정렬을 하는데,
# 여기에서 key값은 list_movie의 ['vote_average'] 기준이며,
# 만약 위의 값이 동일할 경우 두 번째 순위로 ['id'] 기준으로 정렬한다.
# 마지막으로 역순으로 정렬한다.