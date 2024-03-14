import os

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

def main():
    missing = check_env_file()
    if missing:
        print("[INFO] Замените следующие данные:")
        for item in missing:
            print(item)

    else:
        print("Все необходимые данные введены. Запуск файла 'start'...")
        os.system("bash starts")

main()
