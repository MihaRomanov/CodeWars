leaderboard = ['John', 'Brian', 'Jim', 'Dave', 'Fred']
changes = ['Dave +1', 'Fred +4', 'Brian -1']

# list_of_changes = []
list_of_changes = [i for i in range(len(changes)) append(changes[i].split())]
# for i in range(len(changes)):
#     list_of_changes.append(changes[i].split())
print(list_of_changes)
for y in range(len(list_of_changes)):
    for x in range(len(leaderboard)):
        if y == len(list_of_changes)-1:
            if leaderboard[x] == list_of_changes[y][0]:
                leaderboard.insert(int(leaderboard.index(leaderboard[x])) - int(list_of_changes[y][1]), str(leaderboard.pop(x)))
                print(leaderboard)
                break
        else:
            if leaderboard[x] == list_of_changes[y][0]:
                leaderboard.insert(int(leaderboard.index(leaderboard[x])) - int(list_of_changes[y][1]), str(leaderboard.pop(x)))



