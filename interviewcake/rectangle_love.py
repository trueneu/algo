rectangle1 = {
    'left_x': 1,
    'bottom_y': 5,
    'width': 10,
    'height': 4,
}

rectangle2 = {
    'left_x': 2,
    'bottom_y': 2,
    'width': 1,
    'height': 4,
}


rectangle1 = {
    'left_x': 1,
    'bottom_y': 5,
    'width': 10,
    'height': 4,
}

rectangle2 = {
    'left_x': 0,
    'bottom_y': 6,
    'width': 1,
    'height': 1,
}


def def_additional_pts(rec):
    rec['right_x'] = rec['left_x'] + rec['width']
    rec['top_y'] = rec['bottom_y'] + rec['height']

    rec['p0'] = (rec['left_x'], rec['bottom_y'])
    rec['p1'] = (rec['left_x'], rec['top_y'])
    rec['p2'] = (rec['right_x'], rec['top_y'])
    rec['p3'] = (rec['right_x'], rec['bottom_y'])


def intersection(rec1, rec2):
    def_additional_pts(rec1)
    def_additional_pts(rec2)

    if rec1['left_x'] > rec2['left_x']:  # sort by left
        rec1, rec2 = rec2, rec1

    if rec2['left_x'] > rec1['right_x']:
        return None

    if rec2['bottom_y'] > rec1['top_y']:
        return None

    if rec1['right_x'] <= rec2['left_x']:
        return None

    if rec1['bottom_y'] > rec2['bottom_y'] and rec1['bottom_y'] >= rec2['top_y']:
        return None

    if rec1['top_y'] <= rec2['bottom_y'] and rec1['top_y'] < rec2['top_y']:
        return None

    result = {}
    result['left_x'] = rec2['left_x']
    result['bottom_y'] = max([rec1['bottom_y'], rec2['bottom_y']])
    result['top_y'] = min([rec1['top_y'], rec2['top_y']])
    result['right_x'] = min([rec1['right_x'], rec2['right_x']])

    result['width'] = result['right_x'] - result['left_x']
    result['height'] = result['top_y'] - result['bottom_y']



    return result



print(intersection(rectangle1, rectangle2))
