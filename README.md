# Лабораторна робота №7 — база даних спортивних результатів

Варіант 9 продовжує пакет `sports_streaming` із попередніх робіт: CSV-валідація та потокова обробка збережені, а persistence layer записує результати у SQLite. Він побудований на SQLAlchemy ORM і Repository Pattern; окремий DB-API запит показує параметризований пошук за видом спорту.

## Встановлення та запуск (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[test]"
python -m alembic upgrade head
python -m sports_streaming.main --persist-db
```

Без прапорця `--persist-db` попередній режим CSV → JSON продовжує працювати. Типовий файл бази `sports_results.db` створюється в корені проєкту. Можна передати інший шлях:

```powershell
python -m sports_streaming.main --persist-db --database-url "sqlite:///my_results.db"
```

## Тести

```powershell
python -m pytest -v
```

Тести запускаються на окремій SQLite in-memory базі; вони не торкаються production БД. Є перевірки CRUD для всіх трьох сутностей, зв'язків, обмежень, DB-API-фільтра, AVG/MAX-рейтингів, commit/rollback та Alembic migrations.

## Структура

```text
src/sports_streaming/  # ЛР5/ЛР6-пакет і persistence layer
migrations/             # початкова схема та migration з датою змагання
tests/integration/      # інтеграційні перевірки на тестовій SQLite
report/                 # звіт та докази запуску
```
