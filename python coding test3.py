student_id = {"id1":{"name" : "alice", "score" : 70,},"id2":{ "name": "max", "score": 85,}}
print(student_id)

max = max(student_id)
min = min(student_id)
print('The most is ',max ,'and the least is',min)

lookup = input('Who do you want to search up id1 or id2').lower()
lookup2 = student_id.get(lookup)
print(lookup2)




