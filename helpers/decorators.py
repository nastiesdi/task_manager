
def login_required(function):
    def check_login(self, input):
        if not self.current_dev:
            raise ValueError('Please login!!!!!!!!!')
        return function(self, input)
    return check_login
