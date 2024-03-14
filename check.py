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
                    del required_variables[key]

    if required_variables:
        for key, value in required_variables.items():
            missing_variables.append(f"{key} не введена. {value}")

    return missing_variables

def main():
    missing = check_env_file()
    if missing:
        for item in missing:
            print("Один или несколько данных не введены:")
            print(item)
    else:
        print("Все необходимые данные введены. Запуск файла 'start'...")
        os.system("bash starts")

if __name__ == "__main__":
    main()
