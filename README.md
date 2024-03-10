<h1>О Hatiko-Userbot</h1>

<p>Hatiko-Userbot это Telegram userbot с открытым исходным кодом (если вы не знали, selfbot/userbot используются для автоматизации аккаунтов пользователей).

Как же он работает? Работает он очень просто: используя библиотеку telethon, скрипт на питоне подключается к вашему аккаунту (создавая новую сессию) и перехватывает ваши команды.



Использование selfbot/userbot противоречит Условиям предоставления услуг Telegram, и вы можете быть забанены за его использование, если не будете осторожны.



Разработчики не несут ответственности за любые последствия, с которыми вы можете столкнуться при использовании Hatiko-Userbot. 

Мы также не несём ответственности за любой ущерб, нанесенный чатам при использовании Hatiko-Userbot.</p>



<h1>Установка</h1>

<h2>Termux (используйте только <a href='https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://github.com/termux/termux-app/releases/download/v0.118.0/termux-app_v0.118.0%2Bgithub-debug_arm64-v8a.apk&ved=2ahUKEwjYuqHK1OiEAxUVAhAIHTsOASEQFnoECA8QAQ&usg=AOvVaw32pfVX2vAJMkK9hWOXzM2E'>эту</a> версию)</h2>


<p>1. Даём разрешение к файлом смартфона:</p>
<pre><code>termux-setup-storage</code></pre>
<h4><p>2. Устанавливаем всё необходимое:</p> Обратите внимание:</h4>

<p>При установке в termux будет спрашивать: </br>1. motd (Y/I/N/O/D/Z) [default=N] ?(Пишите: Y (Обязательно большой буквой если написано большой))</br>2. Do you want to continue? [Y/n] (Пишите: Y (Обязательно большой буквой))</p>
<pre><code>apt-get upgrade -y && apt-get update && apt install python && apt install git && apt install openssl-tool && apt upgrade openssl-tool && pkg install openssl && git clone https://github.com/jamalskiy/HatikoUBot.git && cd HatikoUBot/ && pip install -r requirements.txt
</code></pre>

<h1>Обязательно</h1>

<p>Перед запуском скрипта создайте файл .env и заполните все данные</p>

<pre><code>nano .env
</code></pre>

<p>Вставьте этот код и заполните данные:</p>

```
API_ID="1234567" # Замените на свои данные
API_HASH="abdgsmlpab13vsv" # Замените на свои данные
number="+71234567890" # Замените на номер аккаунта 
```
<p>Где взять эти данные? <a href='https://tlgrm.ru/docs/api/obtaining_api_id'>*ТЫК*</a></p>

<p>Как поменяли данные нажмите: (Везде англ. буквы)</p>
<p>1. CTRL + O + Enter</p>
<p>2. CTRL + X</p>

<h3>Обратите внимание:</h3>

<p>Если это первый запуск подождите немного, у вас запросит код. Так же если у вас установлен Облачный пароль, запросит его тоже. Когда будете вводить облачный пароль вы не будете этого видеть.</p>

<p>Вот и всё, отсалось запустить</p>
<p>Если вы всё сделали правильно то всё запустится</p>
<pre><code>bash start
</code></pre>
<p>Чтобы узнать доступные команды, напишите в любой чат эту команду</p>
<pre><code>.команды
</code></pre>

<h2>Следите за обновлениями:</h2>
<p>Наш канал: <a href='https://t.me/HatikoUserBot'>HatikoUBot</a></p>

<h4>Написано на <a href='https://github.com/LonamiWebs/Telethon'>Telethon❤️</a> и <a href='https://github.com/python'>Python❤️</a></h4>

