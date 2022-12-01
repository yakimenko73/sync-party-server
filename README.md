# <p align="center">Sync-party server app</p>

[![Pray for Ukraine](https://img.shields.io/badge/made_in-ukraine-ffd700.svg?labelColor=0057b7)](https://stand-with-ukraine.pp.ua)
[![Licence](https://img.shields.io/github/license/yakimenko73/sync-party-server)](https://github.com/yakimenko73/sync-party-server/blob/master/LICENSE)
[![Deploy](https://github.com/yakimenko73/sync-party-server/actions/workflows/docker-image.yml/badge.svg)](https://github.com/yakimenko73/sync-party-server/actions/workflows/docker-image.yml)

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

`Docker compose` is used to make it easier to start and deploy the web server. See the
official [docker installation documentation](https://docs.docker.com/compose/install/).

### Installation

Clone the repo

   ```sh
   git clone https://github.com/yakimenko73/sync-party-server.git
   ```

Run server with `Docker`

1. Create `.env.dev` file and fill it according to the `env-file.template`
   ```sh
   cat env-file.template >> .env.dev
   ```
3. Build and run docker image
   ```sh
   docker build --tag web-app .
   docker run --env-file=.env.dev --net=host web-app
   ```

Run production server with `nginx` by `docker-compose`

1. Create `.env.prod` file and fill it according to the `env-file.template`
    ```sh
    cat env-file.template >> .env.prod
    ```
2. Run `docker-compose`
   ```sh
   docker-compose up --build
   ```

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any
contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also
simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/amazing-feature`)
3. Commit your Changes (`git commit -m 'Add some amazing-feature'`)
4. Push to the Branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Contact
* Email - r.yakimenko.73@gmail.com
