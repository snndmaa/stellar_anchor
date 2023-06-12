import dotenv
import os

dotenv.load_dotenv()

SECRET_SALT = os.getenv('SECRET_SALT')
