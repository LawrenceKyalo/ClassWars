#lawrencekyalo09@gmail.com
#get user input check forlength, @ and . return valid or invalid email

email = input("Enter your email:")
def is_valid_email(email):
    if len(email) < 5:
        return "Invalid email: too short"
    if '@' not in email or '.' not in email:
        return "Invalid email: missing '@' or '.'"
    if email.count('@') > 1:
        return "Invalid email: too many '@'"
    if email.count('.') > 1:
        return "Invalid email: too many '.'"
    return "Valid email"

