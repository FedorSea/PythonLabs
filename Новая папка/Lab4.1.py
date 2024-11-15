# TODO решите задачу
def task() -> float:
    summ = 0
    import json
    with open('input.json') as f:
        sload = json.load(f)
        for i in range (len(sload)):
            summ = summ + sload[i]['score']*sload[i]['weight']
    return round(summ, 3)

print(task())
