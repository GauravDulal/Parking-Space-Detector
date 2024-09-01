from werkzeug.security import generate_password_hash

password = '3240'
hashed_password = generate_password_hash(password)
print("Hashed password:", hashed_password)
