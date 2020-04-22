
def analyzing_result(result):
    global analized_res, total
    analized_res = {}
    total = 0
    for _ in result:
        for i, k in enumerate(zip(result.replace('X', 'X-')[0::2], result.replace('X', 'X-')[1::2]), start=1):
            analized_res[i] = k
    for k, v in analized_res.items():
        # print(v)
        if 'X' in v:
            total += 20
        elif '/' in v:
            total += 15
        elif '-' in v:
            total += 0
        elif '-' in v:
            total += 0
        else:
            total += int(v[0]) + int(v[1])
    print(total)


result = {}

analyzing_result(result=result)
