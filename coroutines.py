def subgen():
    message = yield 'It is message from subgen before accept income message'
    print(f'Subgen recived: {message}')


def coroutine(coroutine_function):
    def inner(*args, **kwargs):
        g = coroutine_function(*args, **kwargs)
        g.send(None)
        return g

    return inner


class CustomException(Exception):
    pass


@coroutine
def average():
    count = sum = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print('Average generator was stopped!')
            break
        except CustomException:
            print('It is CustomException!')
            break
        else:
            count += 1
            sum += x
            average = round(sum / count, 2)

    return average