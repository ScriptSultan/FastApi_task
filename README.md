# Сервис реализован:
### в файле models.py - модель Пользователи
### в файле private.py - есть 3 функции
- первая функция encode_jwt - я кодирую информацию по JWT токену, который выдаётся на время (600 секунд)
- decode_jwt - декодирую токен, в нём также прописаны ошибки, по истечению времени, и о том, что токен неверный.
- get_user_id_by_token - получение id пользователя по JWT токену
### в файле req_user.py 3 запроса
- регистрация, нужно ввести в POST запрос почту, пароль и данные.
- логин для него нужно ввести только пароль и почту, после чего создаётся JWT токен, который существует 600 секунд и храню в cookie также на 600 секунд
- просмотр профиля (в котором данные о должности, зарплаты и дате повышения), чтобы его посмотреть, нужно сделать запрос и сразу я беру информацию из Cookie, где хранится токен
### в файле users.py
- схемы
