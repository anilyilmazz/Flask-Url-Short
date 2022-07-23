# Url Short App
Url shortener is a url shortening web service, which provides short aliases for redirection of long URLs.
## Tech
Url shortener uses a number of open source projects to work properly:
- [Python] - Programming language
- [Flask] - Web framework
- [Docker] - Virtualization and build solutions
- [PostgreSQL] - Open source object-relational database system
- [SQLAlchemy] - Python SQL toolkit

## Installation
Requires docker and docker enginer
Build project with docker compose and run
```sh
docker compose build
docker compose up
```

Migrate Database with Flask cli
```sh
flask db init
flask db migrate -m "Url shortener first migration."
flask db upgrade
```

Run Flask tests at project root
```sh
pytest
```

## API Swagger

Swagger url is "/doc" at project

![alt text](https://i.ibb.co/LgXQTms/Screenshot-18.png)



## Features

- Short url
- Count url view
- Url list at project with view count

## License

MIT


   [Python]: <https://www.python.org/r>
   [Flask]: <https://flask.palletsprojects.com/en/2.1.x/>
   [PostgreSQL]: <https://www.postgresql.org/>
   [Docker]: <https://www.docker.com/>
   [SQLAlchemy]: <https://www.sqlalchemy.org/>


