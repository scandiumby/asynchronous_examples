def coroutine(coroutine_function):
    def inner(*args, **kwargs):
        g = coroutine_function(*args, **kwargs)
        g.send(None)
        return g

    return inner


class CustomException(Exception):
    pass


@coroutine
def subgen():
    while True:
        try:
            message = yield
        except CustomException:
            print('It is custom exception from subgen()!')
        else:
            print(f'Income message to subgen(): {message}')


@coroutine
def delegating_generator(gen):
    while True:
        try:
            income_data = yield
            gen.send(income_data)
        except CustomException as e:
            gen.throw(e)


def subgen_yield_from():
    while True:
        try:
            message = yield
        except CustomException:
            print('It is custom exception from subgen_yield_from()!')
        except StopIteration:
            break
        else:
            print(f'Income message to subgen_yield_from: {message}')
    return 'subgen_yield_from() was stopped by StopIteration!'


@coroutine
def delegating_generator_yield_from(gen):
    result = yield from gen
    print(result)


def simple_yield_example():
    for char in 'world':
        yield char

def simple_yield_from_example():
    yield from 'world'