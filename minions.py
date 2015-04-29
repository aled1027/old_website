def go(x,y,z):
    """
    x           start
    y           end
    z           num iterations
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

    deltas = [(a,b) for a in [-1,1,-2,2] for b in [-1,1,-2,2] if abs(a) != abs(b)]
    counter = {p:0 for p in pos_dict.values()}

    # apply first iteration
    x_pos = pos_dict[x]
    prev_iter = [tuple_add(x_pos,d) for d in deltas if tuple_add(x_pos,d) in pos_dict.values()]
    for p in prev_iter:
        counter[p] += 1

    # do the rest of the iterations
    for i in range(z-1):
        prev_iter = next_iter if i!=0 else prev_iter
        next_iter = []
        for p in prev_iter:
            for d in deltas:
                cur_pos = tuple_add(p,d)
                if cur_pos in pos_dict.values():
                    next_iter.append(cur_pos)
                    counter[cur_pos] += 1

    return new[pos_dict[y]]

print (go(1,1,2))

