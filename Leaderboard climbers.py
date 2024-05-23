leaderboard = ['John', 'Brian', 'Jim', 'Dave', 'Fred']
changes = ['Dave +1', 'Fred +4', 'Brian -1']

list_of_changes = []
for i in range(len(changes)):
    list_of_changes.append(changes[i].split())

print(leaderboard)
print(list_of_changes[2][1])
for y in range(len(list_of_changes)):
    for x in range(len(leaderboard)):
        if leaderboard[x] == list_of_changes[y][0]:
            leaderboard.insert(int(leaderboard.index(leaderboard[x])) - int(list_of_changes[y][1]), leaderboard.pop(x))
            print(int(leaderboard.index(leaderboard[x])) - int(list_of_changes[y][1]))
            print(leaderboard)



