from collections import Counter


def has_movies_with_needed_length(movie_lengths, flight_length):
    movie_lengths_counter = Counter(movie_lengths)
    for x in movie_lengths_counter:
        movie_lengths_counter[x] -= 1
        if movie_lengths_counter[flight_length - x] > 0:
            return True
    return False

l = [1, 2, 3, 4, 4]
f_l = 8
print(has_movies_with_needed_length(l, f_l))