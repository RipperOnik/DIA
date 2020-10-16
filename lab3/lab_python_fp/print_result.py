def print_result(func):
    def decorator(*args, **kwargs):
        print("Имя функции = "+func.__name__)
        res = func(*args, **kwargs)
        if isinstance(res, list):
            for i in res:
                print(i)
        elif isinstance(res, dict):
            for key, value in res.items():
                print("{}={}".format(key, value))
        else:
            print(res)
        return res
    return decorator