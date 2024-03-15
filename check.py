import os
import sys
import requests
from bs4 import BeautifulSoup
import time

ERROR = "error"

def check_env_file():
    required_variables = {
        "API_ID": "API_ID=\"1234567\" # Замените на свои данные",
        "API_HASH": "API_HASH=\"abdgsmlpab13vsv\" # Замените на свои данные",
        "number": "number=\"+71234567890\" # Замените на номер аккаунта",
        "user_id": "user_id=\"12345678\" # Можно узнать у @useridinfobot"
    }
    missing_variables = []

    try:
        with open('.env', 'r') as file:
            for line in file:
                if line.strip() and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    if key in required_variables:
                        if value.strip() == required_variables[key].split('=')[1].strip('"'):
                            del required_variables[key]

        if required_variables:
            for key, value in required_variables.items():
                missing_variables.append(f"[ERROR] Замените {key} на свой.")

    except FileNotFoundError:
        for key, value in required_variables.items():
            missing_variables.append(f"[ERROR] Файл .env отсутствует. Создайте файл.")

    return missing_variables


def check_version():
    with open('HatikoUserBot.py', 'r') as file:
        contents = file.read()
        version_line = [line for line in contents.split('\n') if line.strip().startswith('version')][0]
        local_version = version_line.split('=')[1].strip().strip('"')

    url = "https://github.com/jamalskiy/HatikoUBot/releases"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        latest_version_tag = soup.find("a", {"class": "Link--primary"})
        latest_version = latest_version_tag.text.strip()

        if local_version != latest_version:
            return ERROR

def main():
    print("[INFO VERSION] Проверка обновление...")
    check = check_version()
    if check == ERROR:
        print("[INFO VERSION] У вас неактуальная версия")
        print("[INFO VERSION] Запуск обновление")
        time.sleep(3)
        os.system("git pull")
        sys.exit(1)
    print("[INFO VERSION] Версия актуальная. Проверяем данные...")
    time.sleep(3)
    missing = check_env_file()
    if missing:
        print("[INFO] Замените следующие данные:")
        for item in missing:
            print(item)
        print("[INFO FOR EDIT] Используйте nano .env")

    else:
        print("[INFO FOR EDIT] Данные актуальные. Запуск скрипта...")
        time.sleep(3)
        os.system("bash starts")

main()
