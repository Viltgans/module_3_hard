data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((),
     [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(params):
    global summa
    if isinstance(params, list) or isinstance(params, tuple) or isinstance(params, set):
        for items in params:
            calculate_structure_sum(items)
    elif isinstance(params, dict):
        for value in params.values():
            calculate_structure_sum(value)
        for key in params.keys():
            calculate_structure_sum(key)
    elif isinstance(params, int) or isinstance(params, str):
        if isinstance(params, int):
            summa += params
        elif isinstance(params, str):
            summa += len(params)
    return summa


summa = 0
result = calculate_structure_sum(data_structure)
print(result)
