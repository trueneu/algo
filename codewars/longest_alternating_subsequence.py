numbers = [1, 3, 2, 5, 6, 7, 3, 4, 2, 0, 10]


def longest_alternating_subsequence(numbers):
    max_seq_start = 0
    max_seq_end = 0

    seq_start = 0
    seq_end = 0
    prev_op = '='
    for index, number in enumerate(numbers):
        if index == 0:
            continue
        if number > numbers[index - 1]:
            if prev_op == '<' or prev_op == '=':
                seq_end = index
                prev_op = '>'
            else:
                if max_seq_end - max_seq_start < seq_end - seq_start:
                    max_seq_end = seq_end
                    max_seq_start = seq_start

                seq_start = seq_end = index
                prev_op = '='

        elif number < numbers[index - 1]:
            if prev_op == '>' or prev_op == '=':
                prev_op = '<'
                seq_end = index
            else:
                if max_seq_end - max_seq_start < seq_end - seq_start:
                    max_seq_end = seq_end
                    max_seq_start = seq_start

                seq_start = seq_end = index
                prev_op = '='
    print(numbers[max_seq_start:max_seq_end+1])

longest_alternating_subsequence(numbers)