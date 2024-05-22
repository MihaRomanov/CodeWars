leaderboard = ['John', 'Brian', 'Jim', 'Dave', 'Fred']
changes = ['Dave +1', 'Fred +4', 'Brian -1']

# def leaderboard_sort(leaderboard, changes):
list_of_changes = []
for i in range(len(changes)):
    list_of_changes.append(changes[i].split())
list_do = []
list_posle = []

# for x in range(len(leaderboard)):
#     for y in range(len(list_of_changes)):
#         if leaderboard[x] == list_of_changes[y][0]:
#             leaderboard.insert(leaderboard[x], leaderboard.pop(list_of_changes[y]))
print(leaderboard)
leaderboard.insert(leaderboard.index(leaderboard[2]), leaderboard.pop(3))
print(leaderboard)
# print(leaderboard.pop(3))

# print(list_of_changes)
# print(leaderboard)
# print(int(list_of_changes[2][1]))

# MyList.insert(index_to_insert, MyList.pop(index_to_remove))

# leaderboard_sort(leaderboard, changes)