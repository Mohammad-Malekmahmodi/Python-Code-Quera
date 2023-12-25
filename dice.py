def calculate_probabilities(a, b):
    possibilities = 0
    total_outcomes = (b - a + 1) ** 2

    for i in range(a, b + 1):
        for j in range(a, b + 1):
            possibilities += 1 if i + j > total_outcomes else 0

    return possibilities / total_outcomes


def find_winner(gunnar_dice, emma_dice):
    gunnar_prob = calculate_probabilities(gunnar_dice[0], gunnar_dice[1])
    emma_prob = calculate_probabilities(emma_dice[0], emma_dice[1])

    if gunnar_prob > emma_prob:
        return "Gunnar"
    elif gunnar_prob < emma_prob:
        return "Emma"
    else:
        return "Tie"


# Reading input
gunnar_dice = list(map(int, input().split()))
emma_dice = list(map(int, input().split()))

# Finding the winner
result = find_winner(gunnar_dice, emma_dice)

# Outputting the result
print(result)
