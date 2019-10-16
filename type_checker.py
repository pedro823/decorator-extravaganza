from functools import wraps

def type_checked(f):

    @wraps(f)
    def wrapped_f(*args, **kwargs):

        annotations_copy = dict(f.__annotations__)

        for arg, value in kwargs.items():
            expected_arg_type = annotations_copy[arg]

            if not isinstance(value, expected_arg_type):
                raise TypeError(f'Error in argument {arg}: expected type {expected_arg_type}, got {type(value)}')

            del annotations_copy[arg]

        for (argument_name, expected_type), argument in zip(annotations_copy.items(), args):
            if not isinstance(argument, expected_type):
                raise TypeError(f'Error in positional argument {argument_name}: expected {expected_type}, got {type(argument)}')

        return_value = f(*args, **kwargs)

        expected_return_type = annotations_copy.get('return', None)

        if not isinstance(return_value, expected_return_type):
            raise TypeError(f'Error in return type: expected {expected_return_type}, got {type(return_value)}')

        return return_value

    return wrapped_f