l = [{'user': 'user6', 'match_sum': 8},
     {'user': 'user7', 'match_sum': 4},
     {'user': 'user9', 'match_sum': 7},
     {'user': 'user8', 'match_sum': 2}]

d = next(item for item in l if item['user'] == 'user7')
d['match_sum'] += 3
print(l)