#!/bin/sh

# O shell irá encerrar a execução do script quando um comando falhar
set -e

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  echo "🟡 Waiting for Postgres Database Startup ($POSTGRES_HOST $POSTGRES_PORT) ..."
  sleep 2
done

echo "✅ Postgres Database Started Successfully ($POSTGRES_HOST:$POSTGRES_PORT)"


python manage.py collectstatic --noinput
echo 'Executando makemigrations.sh'
python manage.py makemigrations --noinput
echo 'Executando migrate.sh'
python manage.py migrate --noinput
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('david', 'allysson.david.rose@gmail.com', 'Budeli@#2021')" || true
python manage.py runserver 0.0.0.0:8000