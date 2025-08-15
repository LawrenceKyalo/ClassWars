#lawrencekyalo09@gmail.com
#get user input check forlength, @ and . return valid or invalid email

email = input("Enter your email:")
def is_valid_email(email):
    if len(email) < 5:
        return "Invalid email: too short"
    if '@' not in email or '.' not in email:
        return "Invalid email: missing '@' or '.'"
    if email.startswith('@') or email.startswith('.'):
        return "Invalid email: cannot start with '@' or '.'"
    if email.endswith('@') or email.endswith('.'):
        return "Invalid email: cannot end with '@' or '.'"  
    if email.count('@') > 1:
        return "Invalid email: too many '@'"
    if email.count('.') > 1:
        return "Invalid email: too many '.'"
    return "Valid email"

result = is_valid_email(email)
print(result)

