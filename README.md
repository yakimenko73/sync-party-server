# Sync-party server app
## What is it?
Django web server application for the open source project sync-party

### Built With

* [Django](https://www.djangoproject.com/)
* [Django-rest-framework](https://www.django-rest-framework.org/)
* [Django-sessions](https://docs.djangoproject.com/en/4.0/topics/http/sessions/)
* [Djongo](https://www.djongomapper.com/)
* [Mongodb](https://www.mongodb.com/)
* [Gunicorn](https://gunicorn.org/)
* [Nginx](https://nginx.org/en/)

## Getting Started

This tutorial will help you run server locally

### Prerequisites

`Docker compose` is used to make it easier to start and deploy the web server. See the official [docker installation documentation](https://docs.docker.com/compose/install/).

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/yakimenko73/sync-party-server.git
   ```
2. Create `.env.dev` file and fill it according to the `env-file.template`
   ```sh
   cat env-file.tempalate >> .env.dev
   ```
3. Collect static content for admin panel
   ```sh
   ./src/manage.py collectstatic
   ```
4. Build and run with `docker-compose`
   ```sh
   docker-compose up --build
   ```
   or run with `manage.py`
   ```sh
   docker-compose up mongodb
   ENV_FILE=./.env.dev ./src/manage.py runserver
   ```
5. Make entity migrations for admin panel
   ```sh
   ENV_FILE=./.env.dev ./src//manage.py makemigrations
   ENV_FILE=./.env.dev ./src/manage.py migrate
   ```
If the installation was successful, the server will be available on the http://0.0.0.0:1337

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/amazing-feature`)
3. Commit your Changes (`git commit -m 'Add some amazing-feature'`)
4. Push to the Branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Contact

* Twitter - [@masterslave_](https://twitter.com/masterslave_)
* Email - r.yakimenko.73@gmail.com
