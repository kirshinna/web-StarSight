# StarSight

StarSight — это онлайн-сервис для любителей астрономии, который помогает планировать наблюдения за звёздным небом. Пользователи могут проверять качество ночного неба для выбранного города и даты, а также вести личный дневник наблюдений с фотографиями и заметками.

**Ссылка на рабочий проект:** [https://nastasiak.pythonanywhere.com](https://nastasiak.pythonanywhere.com)

## Технологии
* **Python 3.10**
* **Django 4.2**
* **Pandas** — для обработки данных о погоде
* **Matplotlib / Seaborn** — для построения тепловых карт
* **Bootstrap 5** — для адаптивного интерфейса
* **HTML/CSS** — фронтенд сайта

## Интерфейс
<img width="3084" height="1917" alt="image" src="https://github.com/user-attachments/assets/e7b31bda-ccc2-4efb-98c5-f7e02b9d85c1" />

*Главная страница с навигацией и приветствием пользователей*

<img width="3112" height="1889" alt="image" src="https://github.com/user-attachments/assets/a44c65be-eec0-4c1c-adf9-d9c7a72de420" />

<img width="3113" height="1915" alt="image" src="https://github.com/user-attachments/assets/addbe24b-b064-4be2-b1d5-62fac2ac943e" />

*Страница с тепловой картой ночного неба и подробными данными по дням*

<img width="3102" height="1917" alt="image" src="https://github.com/user-attachments/assets/8ecbc4db-529f-4a7c-b771-fa883f5adbc1" />

*Личный дневник наблюдений с фотографиями, оборудованием и описанием событий*

<img width="3120" height="1829" alt="image" src="https://github.com/user-attachments/assets/c65a17a5-4008-4c4e-950b-c200be7ee51d" />

*Форма добавления новой записи в дневник*

# Запуск проекта локально

## 1. Клонирование репозитория
```bash
git clone https://github.com/kirshinna/web-StarSight.git
cd StarSight
```

## 2. Создание виртуального окружения

**Для Linux/Mac:**
```bash
python -m venv venv
source venv/bin/activate
```

**Для Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

## 3. Установка зависимостей
```bash
pip install -r requirements.txt
```

## 4. Настройка базы данных
```bash
python manage.py migrate
```

## 5. Создание суперпользователя (опционально)
```bash
python manage.py createsuperuser
```
Следуйте инструкциям в терминале для создания учетной записи администратора.

## 6. Запуск сервера разработки
```bash
python manage.py runserver
```
