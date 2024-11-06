#!/bin/bash
set -e

host="$1"
port="$2"
timeout="${3:-30}"

echo "Esperando hasta que MYSQL -> $host:$port esté disponible..."
while ! nc -z "$host" "$port"; do
  timeout=$((timeout - 1))
  if [ $timeout -eq 0 ]; then
    >&2 echo "Esperando a $host:$port"
    exit 1
  fi
  sleep 1
done

echo "MYSQL -> $host:$port está disponible"

# COPY DEPENDENCIES
# COPY requirements.txt .
# CHANGE DIRECTORY
#WORKDIR /opt/app/$APP_DIRECTORY
# INSTALL DEPENDENCIES
echo "CREATE VIRTUAL ENVIRONMENT"
python3 -m venv /opt/app/$APP_DIRECTORY/env
echo "INSTALL DEPENDENCIES"
source /opt/app/$APP_DIRECTORY/env/bin/activate && python -m pip install -r /opt/app/$APP_DIRECTORY/requirements.txt
# CHANGE DIRECTORY
#WORKDIR /opt/app/$APP_DIRECTORY
echo "EXECUTE DJANGO APP"
source /opt/app/$APP_DIRECTORY/env/bin/activate && python /opt/app/$APP_DIRECTORY/manage.py runserver 0.0.0.0:8000
