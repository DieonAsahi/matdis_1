import re

# Definisi pola regular expression untuk memvalidasi format email
email_pattern = re.compile(
    r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
)

# Fungsi untuk memvalidasi format email
def validate_email(email):
    if email_pattern.match(email):
        return True
    else:
        return False

# Contoh daftar email untuk diuji
emails = [
    "example@example.com",
    "user.name@domain.co",
    "user_name@domain.co.in",
    "username@.com",
    "@domain.com",
    "username@domain"
]

# Memvalidasi setiap email dalam daftar
for email in emails:
    if validate_email(email):
        print(f"'{email}' adalah email yang valid.")
    else:
        print(f"'{email}' adalah email yang tidak valid.")
