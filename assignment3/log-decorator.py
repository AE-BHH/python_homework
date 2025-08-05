import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))


def logger_dectorator(func):



    def wrapper(*args, **kwargs):
        positional = list(args) if args else 'none'
        keyword = dict(kwargs) if kwargs else 'none'
        
        result = func(*args, **kwargs)

        logger.log(
            logging.INFO,
            f"function: {func.__name__}\n"
            f"positional parameters: {positional}\n"
            f"keyward parameters: {keyword}\n"
            f"return: {result}\n"
            )
        print(result)
    return wrapper
        


@logger_dectorator
def say_Hello():
    print("Hello, World!")


@logger_dectorator
def add(*args):
    return True

@logger_dectorator
def contact(**kwargs):
    return logger_dectorator


say_Hello()
add(5, 10, True)
contact(name='Sam Smith', phone_number="1234567890", email="sam.smith123@gmail.com")
