import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

email = os.getenv('EMAIL')
app_password = os.getenv('APP_PASSWORD')

link = 'https://dvmn.org/profession-ref-program/'
friend_name = 'Бэла'
my_name = 'Тома'

letter = """
From: lajpanovatoma@mail.ru
To: stgau.matem@mail.ru
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";

Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% - это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""".replace("%website%", 
	'{link}').replace("%friend_name%", '{friend_name}').replace("%my_name%", '{my_name}').format(link = link, friend_name = friend_name, my_name = my_name)

letter = letter.encode("UTF-8")
server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
server.login(email, app_password)
server.sendmail(email, 'stgau.matem@mail.ru', letter)
server.quit()