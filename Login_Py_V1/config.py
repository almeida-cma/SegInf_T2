import os

SECRET_KEY = os.getenv("SECRET_KEY", "chave_secreta_super_segura")

EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587))
EMAIL_USER = os.getenv("EMAIL_USER", "mail@gmail.com")
EMAIL_PASS = os.getenv("EMAIL_PASS", "senha app")

DATABASE = "database.db"  # Agora definida corretamente
