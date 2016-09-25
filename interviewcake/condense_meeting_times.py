meeting_times =   [(1, 10), (2, 6), (3, 5), (7, 9), (11, 13)]


def condense_meeting_times(mt):
    mt_sorted = sorted(mt)
    result = []
    begin, end = mt_sorted[0]
    for curr_begin, curr_end in mt_sorted[1:]:
        if curr_begin > end:
            result.append((begin, end))
            begin, end = curr_begin, curr_end  # start a new condensed period
        else:
            end = max(end, curr_end)
    result.append((begin, end))
    return result


print(condense_meeting_times(meeting_times))