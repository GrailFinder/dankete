#!/bin/bash

set -e

echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'hard2crack')" | python manage.py shell