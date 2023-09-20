#!/bin/sh


echo "The postgres host  is: $POSTGRES_HOST $POSTGRES_DB_PORT"
# Wait for the DB to be ready
until nc -z -v -w30 $POSTGRES_HOST $(( $POSTGRES_DB_PORT ));
do
 echo 'Waiting for the DB to be ready...'
 sleep 2
done

python manage.py makemigrations
python manage.py migrate
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='user1').exists():
  User.objects.create_user('user1@example.com', 'user1', 'John', 'Doe', 'kadabra13')
if not User.objects.filter(username='user2').exists():
  User.objects.create_user('user2@example.com', 'user2', 'John', 'Doe', 'kadabra13')
if not User.objects.filter(username='user3').exists():
  User.objects.create_user('user3@example.com', 'user3', 'John', 'Doe', 'kadabra13')
EOF

gunicorn -c gunicorn.py core.wsgi:application
