import os
from kaggle_secrets import UserSecretsClient

def load_environment_variables():
    user_secrets = UserSecretsClient()
    os.environ["GROQ_API_KEY"] = user_secrets.get_secret("GROQ_API_KEY")