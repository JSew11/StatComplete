# StatComplete
Stat tracking and live score keeping web app for baseball games. Built using Django, PostgreSQL and Reactjs.

## Dev Environment Setup

### Installations
* Docker & Docker Compose [Docker Desktop](https://www.docker.com/products/docker-desktop/)
* [VSCode](https://code.visualstudio.com/download)
* [Git](https://git-scm.com/downloads)
* Database Management tool (I like [DBeaver](https://dbeaver.io/))

### Project Setup
1. Clone the repo (https://github.com/JSew11/StatComplete) using the command:  
    `git clone https://github.com/JSew11/StatComplete`

### Running the App
1. Navigate to the project root
1. In your terminal, run the command `docker compose up -d` to start the app (to tear down, run `docker compose down`)  
1. If you have made local changes (outside of the Docker container) and wish to restart the app with them applied, run the command `docker compose restart`
