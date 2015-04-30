def go(x,y,z):
    """
    x           first digit
    y           last digit
    z           number of digits in phone number
                note that z digits => z-1 movements
    deltas      is a list of all the possible knight moves
    counter     tracks how many possible ways we can get to a position
    next_iter   tracks what numbers we've been at in the current iteration
    prev_iter   tracks what numbers we were at in the previous iteration
    """
    assert(z>=1)
    assert(x in range(10))
    assert(y in range(10))

    def tuple_add(a,b):
        return (a[0]+b[0], a[1]+b[1])

    pos_dict = {
        1:(1,1),
        2:(1,2),
        3:(1,3),
        4:(2,1),
        5:(2,2),
        6:(2,3),
        7:(3,1),
        8:(3,2),
        9:(3,3),
        0:(1,4),
        }

    positions = pos_dict.values()
    deltas = [(a,b) for a in [-1,1,-2,2] for b in [-1,1,-2,2] if abs(a) != abs(b)]
    prev_counter = {p : 0 for p in positions}


    if z == 1:
        return 1 if x==y else 0

    # apply first iteration
    x_pos = pos_dict[x]
    x_plus_deltas = [tuple_add(x_pos,d) for d in deltas if tuple_add(x_pos,d) in positions]
    for a in x_plus_deltas:
        prev_counter[a] += 1
    if z == 2:
        return prev_counter[pos_dict[y]]

    """
    - apply next z-2 iterations
        - (meaning a total of z-1 iterations. see above for why z-1 iters)
    - prev_counter is the counter for the previous iteration
        - key is a position
        - value is the number of ways we could have gotten to v
    - cur_counter is the counter for the current iteration
        - same format as prev_counter
    """

    cur_counter = {}
    for i in range(z-2):
        prev_counter = cur_counter.copy() if i != 0 else prev_counter
        cur_counter = {p : 0 for p in positions}

        for p in prev_counter:
            if prev_counter[p] == 0:
                continue
            p_plus_deltas = [tuple_add(p,d) for d in deltas if tuple_add(p,d) in positions]
            for pos in p_plus_deltas:
                cur_counter[pos] += prev_counter[p]

    return cur_counter[pos_dict[y]]

print (go(1,1,1))
