# Двусторонняя интеграция базы данных ГГС и CRM Битрикс24

## Настройка проекта:

1. Разворачиваем виртуальное окружение

```shell
python -m venv .venv && .venv/Scripts/activate
```

2. Устанавливаем зависимости

```shell
pip install -r requirements.txt
```

3. Поднимаем сервер

```shell
fastapi dev app/app.py
```
