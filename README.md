![image](https://img.freepik.com/premium-photo/anime-girl-boy-romance-relationship-valentine-s-day-concept-generative-ai_717906-2726.jpg)

# 🚀 О версии 0.0.2

<p>🔹 Заменили префикс с "." на "!"</br></p>
<p>🔹 Теперь команды можно писать как на русском, так и английском. Пример: - !moon - !луна</br></p>
<p>🔹 Теперь мини-мультик можно активировать одной из 4 фраз: еж/ёж/ежик/ёжик </p>
<p>🔹 При каждом запуске проверяется актуальность версии, и если необходимо, то она автоматически обновляется</p>

# 🤖 О Hatiko-Userbot

Hatiko-Userbot это Telegram userbot с открытым исходным кодом, который предназначен для автоматизации аккаунтов пользователей. Однако, помните, использование selfbot/userbot противоречит Условиям предоставления услуг Telegram, и вы можете быть забанены за его использование, если не будете осторожны.

## 📌 Если уже устанавливали:
<pre><code>cd HatikoUBot && bash start</code></pre>

## 🛠️ Установка

### Termux (используйте только [эту версию](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://github.com/termux/termux-app/releases/download/v0.118.0/termux-app_v0.118.0%2Bgithub-debug_arm64-v8a.apk&ved=2ahUKEwjYuqHK1OiEAxUVAhAIHTsOASEQFnoECA8QAQ&usg=AOvVaw32pfVX2vAJMkK9hWOXzM2E))

<p>1. Даём разрешение к файлом смартфона:</p>
<pre><code>termux-setup-storage</code></pre>
<h4><p>2. Устанавливаем всё необходимое:</p>💡 Обратите внимание:</h4>

<p>При установке в termux будет спрашивать: </br>1. motd (Y/I/N/O/D/Z) [default=N] ?(Пишите: Y (Обязательно большой буквой если написано большой))</br>2. Do you want to continue? [Y/n] (Пишите: Y (Обязательно большой буквой))</p>
<pre><code>apt-get upgrade -y && apt-get update && apt install python && apt install git && apt install openssl-tool && apt upgrade openssl-tool && pkg install openssl && git clone https://github.com/jamalskiy/HatikoUBot.git && cd HatikoUBot/ && pip install -r requirements.txt
</code></pre>


<p>3. создайте файл .env и заполните все данные</p>

<pre><code>nano .env
</code></pre>

<p>4. Вставьте этот код и заполните данные:</p>

```
API_ID="1234567" # Замените на свои данные
API_HASH="abdgsmlpab13vsv" # Замените на свои данные
number="+71234567890" # Замените на номер аккаунта
user_id="12345678" # Можно узнать у @useridinfobot
```
<p>Где взять эти данные? <a href='https://tlgrm.ru/docs/api/obtaining_api_id'>*ТЫК*</a></p>

<p>Как поменяли данные нажмите: (Везде англ. буквы)</p>
<p>1. CTRL + O + Enter</p>
<p>2. CTRL + X</p>

<h3>💡 Обратите внимание:</h3>

<p>Если это первый запуск подождите немного, у вас запросит код. Так же если у вас установлен Облачный пароль, запросит его тоже. Когда будете вводить облачный пароль вы не будете этого видеть.</p>

<p>Вот и всё, отсалось запустить</p>
<p>Если вы всё сделали правильно то всё запустится</p>
<pre><code>bash start
</code></pre>
<p>Чтобы узнать доступные команды, напишите в любой чат эту команду</p>
<pre><code>!команды
</code></pre>

# 🚫 Отказ от ответственности
```
Внимание: использование данного кода и любых связанных файлов происходит на ваш собственный риск. Автор не несет ответственности за любые убытки, повреждения или другие проблемы, возникшие в результате использования этого программного обеспечения.

Этот репозиторий предоставляется "как есть", без каких-либо гарантий. Автор не предоставляет никаких явных или подразумеваемых гарантий в отношении работы, безопасности или пригодности для конкретного использования.

Пожалуйста, будьте внимательны при использовании этого кода и проверьте его на соответствие вашим требованиям. Если аккаунт будет заблокирован из-за злоупотребления этим скриптом, ответственность полностью лежит на вас.

Если у вас есть какие-либо вопросы или замечания, не стесняйтесь создавать Issue или делать Pull Request.

Спасибо за понимание!
```

<h2>🔄 Следите за обновлениями:</h2>
<p>Наш канал: <a href='https://t.me/HatikoUserBot'>HatikoUBot</a></p>

<h4>Написано на <a href='https://github.com/LonamiWebs/Telethon'>Telethon❤️</a> и <a href='https://github.com/python'>Python❤️</a></h4>

## Разработчики и те кто внёс вклад в проект

<a href="https://github.com/jamalskiy"><img src="https://avatars.githubusercontent.com/u/155892199?v=4" alt="Jamalskiy" width="40" height="40"></a>
<a href="https://github.com/PashaSalt"><img src="https://avatars.githubusercontent.com/u/162937401?v=4" alt="PashaSalt" width="40" height="40"></a>
<a href="https://github.com/Sentmen767"><img src="https://avatars.githubusercontent.com/u/162962885?v=4" alt="Sentmen767" width="40" height="40"></a>

