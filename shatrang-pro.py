input_data = input().split()
puyan_pieces = [int(x) for x in input_data]
standard_pieces = [1, 1, 2, 2, 2, 8]
difference = [s - p for p, s in zip(puyan_pieces, standard_pieces)]
print(' '.join(map(str, difference)))
