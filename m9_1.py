def apply_all_func(int_list, *functions):
    results={}
    for f in functions:
        rez=f(int_list)
        results[f.__name__]=rez

    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))