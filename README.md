## General info
This is the repository of `celery_example`. This project showcases basic usage of celery
(asynchronous task queue) + redis as a broker.

## Technologies
Project is created with:
* [django](https://www.djangoproject.com)
* [poetry](https://python-poetry.org)
* [celery](https://docs.celeryproject.org/en/stable/index.html)
* [redis](https://redis.io/)

## Launch
[poetry](https://python-poetry.org) is a package-manager tool of the project.


Create appropriate directory for the project and clone repository to your local machine

```bash
$ cd <project_directory>
$ git clone <repo_address>
```


Generate virtual environment and install all needed dependencies

```bash
$ poetry install
```


If you need help or more info about poetry, run:

```bash
$ poetry --help
```