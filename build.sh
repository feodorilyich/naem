#!/usr/bin/env bash
# build.sh

set -o errexit

# Установка зависимостей
pip install -r requirements.txt

# Сбор статических файлов
python manage.py collectstatic --noinput

python manage.py migrate

python manage.py loaddata fixtures/category.json || true
python manage.py loaddata fixtures/product.json || true
python manage.py createsuperuser --no-input || true



