from werkzeug.security import generate_password_hash, check_password_hash

def set_password(password):
    return generate_password_hash(password)

def verify_password(stored, provided):
    return check_password_hash(stored, provided)

