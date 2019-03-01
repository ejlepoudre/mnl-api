<<<<<<< HEAD
# MNL Hockey League API

[![CircleCI](https://circleci.com/gh/monday-night-lights/mnl-api.svg?style=shield)](https://circleci.com/gh/monday-night-lights/mnl-api)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/6c339980c6f742c7a23de84e313e6af4)](https://www.codacy.com/app/monday-night-lights/mnl-api?utm_source=github.com&utm_medium=referral&utm_content=monday-night-lights/mnl-api&utm_campaign=badger)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A web API for managing Teams, Players, Games, and more for the Monday Night
Lights hockey league.

It is uses the [Django 2.0](https://docs.djangoproject.com/en/2.0/) web
framework, [Django Rest Framework 3.7](http://www.django-rest-framework.org/)
API library, and a [PostgreSQL 9.6](https://www.postgresql.org/docs/9.6/static/index.html)
database.

The Python code is written in accordance to the
[PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/#introduction).

## Development

To make set up as simple as possible across different operating systems, a
Vagrant file is set up to launch a Debian virtual machine using VirtualBox.
This VM can be treated like a production web server running locally on your
computer. [Docker Compose](https://docs.docker.com/compose/) is used to launch
the necessary services for running the application in a production-like manner.

In addition to the Django service, a separate [nginx](https://nginx.org/en/docs/)
service is used as a web proxy to connect the web application (running via
[Gunicorn](http://gunicorn.org/)) to web ports 80/443. It is also configured to
host static files separately from the web app.

### Environment Setup

Install these tools to set up the development environment:

- [Vagrant](https://www.vagrantup.com/downloads.html)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

Clone the repository and navigate to the project directory.

    $ git clone git@github.com:monday-night-lights/mnl-api.git
    $ cd mnl-api

#### Set Environment Variables

The `dev.env` environment variables file is already created. These variables
should be changed for other environments (int.env, prod.env, etc.) but are fine
as they are for development purposes.

##### Default Dev Variables

    SECRET_KEY=dev_secret_key
    ALLOWED_HOSTS=172.30.0.10
    HOST=django
    DEBUG=True

    POSTGRES_HOST=postgres
    POSTGRES_PORT=5432
    POSTGRES_DB=mnl_db
    POSTGRES_USER=mnl_db_user
    POSTGRES_PASSWORD=mnl_db_password

#### Run the Development Server

Use Vagrant to provision and run a Debian virtual development server

    $ vagrant plugin install vagrant-docker-compose vagrant-vbguest
    $ vagrant vbguest # see https://stackoverflow.com/a/37706087/1797103 for more info
    $ vagrant up

The application will be running at [https://172.30.0.10](https://172.30.0.10).

### Running Django Management Commands

In order to run [Django commands](https://docs.djangoproject.com/en/2.0/ref/django-admin/),
SSH into the Vagrant VM and use `docker-compose exec` to execute commands
inside the Django container:

    $ vagrant ssh
    vagrant@contrib-jessie:/src$ docker-compose exec django <sh command>

For example, to run the
[Django shell](https://docs.djangoproject.com/en/2.0/ref/django-admin/#shell):

    vagrant@contrib-jessie:/src$ docker-compose exec django /venv/bin/python manage.py shell

#### Testing

Unit tests can be run with the built-in
[Django test runner](https://docs.djangoproject.com/en/2.0/topics/testing/overview/):

    vagrant@contrib-jessie:/src$ docker-compose exec django /venv/bin/python manage.py test

### SSL in Development

In order to develop in an environment as production-like as possible, we are
using a self-signed SSL certificate. The dev certificate is already setup but
the steps taken to create it are documented below for reference. The
certificate is set to expire one year from its creation date so you may need to
generate a new one if you are working on this project on or after the
expiration date.

To create a self-signed key and certificate pair, ssh into the vagrant virtual
machine and navigate to the `nginx/certs` directory. Then use the OpenSSL
[`req` command](https://www.openssl.org/docs/manmaster/man1/req.html) to create
the `.key` and `.crt` files.

```
$ vagrant ssh
$ cd /src/nginx/certs
$ openssl req -x509 -nodes -days 365 -newkey rsa \
               -config dev.conf -keyout dev.key -out dev.crt
```
=======
# MNL

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

The [Monday Night Lights Hockey League](http://mnlhl.com/) API built
for managing Teams, Players, Seasons, Games, and more.

## Set up

This application can be run using Docker. If you cannot install Docker, a
Vagrantfile is provided for provisioning a Debian virtual machine.

To get started, clone the repository. Then make a copy of `template.env` and rename it `.env`.

    $ git clone git@github.com/mnlhl:mnl.git
    $ cd mnl
    $ cp template.env .env  # variables are preset for dev but should be changed in production

### Running with Docker

1. Install [Docker](https://docs.docker.com/install/)
   and [Docker Compose](https://docs.docker.com/compose/install/)
1. Build and run the application containers using docker-compose:

        $ docker-compose up --build -d

1. View the running application in a browser at https://localhost

When you need to run a command inside a container, use:

    docker-compose exec container_name <command>

Or you can run a shell to enter the container and run commands inside

    docker-compose exec container_name /bin/sh
    # <command>

### Running with Vagrant

1. Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads) and
   [Vagrant](https://www.vagrantup.com/downloads.html)
1. Add the [vagrant-docker-compose](https://github.com/leighmcculloch/vagrant-docker-compose)
   Vagrant plug-in and run the development VM:

        $ vagrant plugin install vagrant-docker-compose
        $ vagrant up

1. View the running application in a browser at https://172.16.0.2

### Running Tests

The unit tests can be run with:

    python manage.py test

### Admin users

An admin user can be added for development by running:

    python manage.py createsuperuser

### Python Requirements

We are using Pipenv to manage Python dependencies. This means there is a
`Pipfile` instead of the traditional `requirements.txt` file. To install
or update Python packages, run:

    pipenv install <package_name>
    pipenv update

    pipenv install --dev --system

This will update `Pipfile.lock` with the new version numbers, and then
install the packages globally within the `django` container.

### SSL in development

**Note:** Since we are using a self-signed certificate for SSL in development,
your browser will warn that the page connection is insecure. Bypass the warning
by clicking "Advanced" and adding an exception for this certificate.

![Firefox Insecure Connection Warning](https://prod-cdn.sumo.mozilla.net/uploads/gallery/images/2018-07-24-17-48-12-79a9e2.png)

### Helpful Links

#### Dev/Ops

- [Docker](https://docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Vagrant](https://www.vagrantup.com/)
- [debian/contrib-stretch64](https://app.vagrantup.com/debian/boxes/contrib-stretch64)
  virtual box (`contrib-*` boxes include the `vboxfs` kernel module for shared folders)
- [nginx](https://nginx.org/en/)

#### Database

- [PostgreSQL](https://www.postgresql.org/)

#### Python & Django

- [Python 3.7](https://www.python.org/)
- [PEP 8 Python Style Guide](https://www.python.org/dev/peps/pep-0008/#introduction)
- [Pipenv](https://pipenv.readthedocs.io/en/latest/)
- [Django](https://djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
>>>>>>> upstream/master
