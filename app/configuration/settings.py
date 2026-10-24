from dotenv import load_dotenv
import os

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env


def database_settings():
    """
    função retorn url do sqlalchemy para POSTGRESQL
    """

    settings = {
        "host": os.getenv("DB_HOST"),
        "port": int(os.getenv("DB_PORT")),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "database": os.getenv("DB_NAME")
    }

    return f"postgresql://{settings['user']}:{settings['password']}@{settings['host']}:{settings['port']}/{settings['database']}"



if __name__ == "__main__":
    print(f"Database URL: {database_settings()}")


