
def login_required(function):
    def check_login(manager, input):
        if not manager.current_dev:
            raise ValueError('Please login!!!!!!!!!')
        return function(manager, input)
    return check_login
