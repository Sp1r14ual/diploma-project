# Двусторонняя интеграция базы данных ГГС и CRM Битрикс24

## Настройка проекта:

0. Проверяем, что развернута БД ggs_stud в SQL Server

1. Разворачиваем виртуальное окружение

```shell
python -m venv .venv
```

```shell
.venv/Scripts/activate
```

2. Устанавливаем зависимости

```shell
pip install -r requirements.txt
```

3. Переименовываем [.env.example](app/.env.example) в .env и прописываем переменные окружения

4. Поднимаем сервер

```shell
fastapi dev app/app.py
```

5. Если нужны автотесты, отключаем JWT-защиту (в модуле [settings.py](app/settings.py) на 48 строке переключаем флаг)

```python
ENABLE_SECURITY: bool = False
```

6. Часть автотестов отключены с целью минимизации расходов лимитированных запросов к коммерческим API DaData и GetGeo.<br>Если необходим их запуск, переключаем флаги в
   <br>a. [3_house_test.py](tests/3_house_test.py) на 9 строке
   <br>b. [11_validate_person_tests.py](tests/11_validate_person_tests.py) на 31 строке
   <br>с. [12_validate_organization_tests.py](tests/12_validate_organization_tests.py) на 36 строке

```python
IS_ACTIVE = True
```
