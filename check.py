import os
import sys
import requests
from bs4 import BeautifulSoup
import time

ERROR = "error"

def check_env_file():
    required_variables = {
        "API_ID": "API_ID=\"1234567\"",
        "API_HASH": "API_HASH=\"abdgsmlpab13vsv\"",
        "number": "number=\"+71234567890\"",
        "user_id": "user_id=\"12345678\""
    }
    modified_variables = []

    try:
        with open('.env', 'r') as file:
            for line in file:
                if line.strip() and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    value = value.strip().strip('"')
                    if key in required_variables:
                        expected_value = required_variables[key].split('=')[1].split('#')[0].strip().strip('"')
                        if value.lower() == expected_value.lower():
                            modified_variables.append(f"[INFO] Значение переменной {key} соответствует ожидаемому. Замените на свои данные.")

        if modified_variables:
            for item in modified_variables:
                print(item)

    except FileNotFoundError:
        pass


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
