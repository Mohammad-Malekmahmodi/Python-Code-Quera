n = int(input())
states = [int(input()) for _ in range(n)]

changes = 0
current_state = states[0]

for i in range(1, n):
    if states[i] != current_state:
        changes += 1
        current_state = states[i]

print(changes)
