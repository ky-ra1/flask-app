import bcrypt

print('Something')

# Sign up
passwords = 'passw0rd1!'
hashed_password = bcrypt.hashpw(passwords.encode(), bcrypt.gensalt()).decode()
# Put this in database

# Never print passwords or hashed password in production
print(hashed_password)


# Log in
provided_password = "passw0rd1!"
password_correct = bcrypt.checkpw(provided_password.encode(), hashed_password.encode())

print(password_correct)