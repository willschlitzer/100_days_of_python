from functools import wraps


def make_html(element):
    def func_dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            text = "<" + element + ">"
            text += func()
            text += "</" + element + ">"
            return text
        return wrapper
    return func_dec

@make_html('p')
@make_html('strong')
def get_text(text='I code with PyBites'):
    return text


if __name__ == "__main__":
    print(get_text())