#!/bin/bash
# wait-for-postgres.sh

set -e

host="$1"
shift
user="$1"
shift
port="$1"
shift
cmd="$@"

echo "waiting for mysql"
while ! mysql -h"$host" -u"$user" --port="$port" -e status > /dev/null 2>&1; do
  >&2 echo "MySQL is unavailable - sleeping"
  sleep 1
done

>&2 echo "Mysql is up - executing command"
exec $cmd