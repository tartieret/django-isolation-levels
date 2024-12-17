# Isolation levels with Django - Demo application

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

License: MIT

## Overview

This repository provides a demo application to test different isolation levels with Django and PostgreSQL. It is based on the [django-cookiecutter template available here](https://github.com/cookiecutter/cookiecutter-django).

## Setup

Build the docker images using:

```bash
docker compose -f docker-compose.local.yml build
```

Then run the following management commands to initialize the database and create a superuser account:

```bash
docker compose -f docker-compose.local.yml run --rm django python manage.py migrate
docker compose -f docker-compose.local.yml run --rm django python manage.py createsuperuser
```

## Run the application

Start the stack using:

```bash
docker compose -f docker-compose.local.yml up
```

You can then browse the application at <http://localhost:8000>
