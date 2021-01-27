# Test Education
Application to create courses and teachers

## Getting Started
To have a copy of the repository on your machine we must clone the repository
* Clone repository
```ssh
    git clone git@github.com:pollitosabroson/education.git
```
### Prerequisites
Make sure that you have met the following prerequisites before continuing with this tutorial.
* Logged in as a user with sudo privileges or Admin user for MAC.
* Have [Docker](https://docs.docker.com/install/) installed

### Installing
To install the project, we must access the docker folder, after the environment we are going to execute, in this case it is the one of dev and we execute the following commands.
* access folder
```ssh
  cd education/docker/dev
```
* Create dockers
```ssh
  docker-compose build --no-cache --force-rm
```
* Run dockers
```ssh
  docker-compose up -d
```
* Apply migrations
```ssh
  docker exec -it api_dev_api_1 python manage.py migrate
```
* Access

    * API: [localhost:8091](http://localhost:8091/)

### Endpoints
- profressor
    - Create Professor
        -  http://localhost:8091/api/v1/professors/
    - List Professors
        - http://localhost:8091/api/v1/professors/
    -  Profile Professorr
        -  http://localhost:8091/api/v1/professors/{professor_id}
- Courses
    - Create Course
        http://localhost:8091/api/v1/courses/
    - List Courses
        http://localhost:8091/api/v1/courses/
    - Single Course
        http://localhost:8091/api/v1/courses/{course_id}
- voting
    - Create vote
        http://localhost:8091/api/v1/voting/

## Running the tests
To run the tests just execute them via docker exec
* API
```ssh
  docker exec -it api_dev_api_1 pytest -v
```

## Project scaffolding
- api
    - Core
        - Application that manages functions that are used in multiple applications
    - Courses
        - Application to manage all courses
    - professors
        - Application to manage all professors
    - Voting
        - Application to manage all votes
- Docker
    - Dev
        - All configs for development

## Features

### Courses
* Create courses.
* List all courses
* Single Course

### professors

* Create professor
* List all professors
* Profile professor
