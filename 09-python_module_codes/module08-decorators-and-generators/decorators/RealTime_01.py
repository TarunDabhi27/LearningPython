authorized_users = {"john":1234,
               "paul":4321
               }

def validate_credentials(user_name,password):
    if user_name in authorized_users.keys():
        if password == authorized_users[user_name]:
            return "Login Success"
    return "Login Failed"

@authorized_users
def send_otp(user_name, password):
    return "OTP Sent"


def authorized_users(any_function):
    def wrapper_function(user_name,password):
        if user_name in authorized_users.keys():
            if password == authorized_users[user_name]:
                any_function(user_name,password)
    return authorized_users;


if __name__ == '__main__':

print(send_otp("john"))