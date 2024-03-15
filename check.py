import os
import requests
from bs4 import BeautifulSoup

def check_env_file():
    required_variables = {
        "API_ID": "API_ID=\"1234567\" # Замените на свои данные",
        "API_HASH": "API_HASH=\"abdgsmlpab13vsv\" # Замените на свои данные",
        "number": "number=\"+71234567890\" # Замените на номер аккаунта",
        "user_id": "user_id=\"12345678\" # Можно узнать у @useridinfobot"
    }
    missing_variables = []

    with open('.env', 'r') as file:
        for line in file:
            if line.strip() and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                if key in required_variables:
                    if value.strip() == required_variables[key].split('=')[1].strip('"'):
                        del required_variables[key]

    if required_variables:
        for key, value in required_variables.items():
            missing_variables.append(f"[ERROR]Замените {key} на свой. Используйте nano .env")

    return missing_variables

def check_version():
    with open('HatikoUBot.py', 'r') as file:
        contents = file.read()
        version_line = [line for line in contents.split('\n') if line.strip().startswith('__version__')][0]
        local_version = version_line.split('=')[1].strip().strip('"')

    url = "https://github.com/jamalskiy/HatikoUBot/releases"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        latest_version_tag = soup.find("a", {"class": "Link--primary"})
        latest_version = latest_version_tag.text.strip()

        if local_version != latest_version:
            print("[INFO VERSION] У вас неактуальная версия, обновитесь с помощью команды git pull")
            return

def main():
    check_version()
    missing = check_env_file()
    if missing:
        print("[INFO] Замените следующие данные:")
        for item in missing:
            print(item)
            print("[INFO FOR EDIT] Используйте nano .env")

    else:
        print("Все необходимые данные введены. Запуск файла 'start'...")
        os.system("bash starts")

main()
