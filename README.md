# Capstone1-Space-app

## Title of Project
NASA Visual Exploration - https://iozsa-space-app.herokuapp.com/
## Goal
This app is intended to pique one’s interest about astronomy and increase curiosity about what’s out there - outer Space.
The goal of this app is to offer the users a visual interaction, where simple searches can return amazing photos from NASA public APIs
## Demographics
The app is mainly an educational visual tool, easy to navigate, so that anybody that wants to find out more about Space will be a potential user.
## Features
The site has 4 main parts, accessible through the navbar and uses 3 different APIs:

- NASA Images - a service provided by NASA that allows searches on their image database.
This uses NASA Image Library API - [docs here](https://images.nasa.gov/docs/images.nasa.gov_api_docs.pdf). For the users who are unsure what to search for, the "I Feel Lucky" button will retrive a random picture from a list of about 50 celestial objects.
- APOD - Astronomy Picture of the DAY - This micro-API delivers an image/video file updated daily by NASA - [docs here](https://github.com/nasa/apod-api)
- Perseverance Rover - Displays images from Mars. Using this API,  the app randomly selects a sol (Mars day) out of the total number of days the rover has been active and retrieves pictures from 15 different cameras - [docs here](https://github.com/chrisccerami/mars-photo-api)
- Your Image Collection - When using the NASA Images search tool
user can add/delete their favorite pictures to/from the database, if they are logged in.
This link is not shown and the route is blocked to "Guest" users.
## Used flow
User is taken to the home page that has a welcoming message. A guide for the site navigation is linked to "About" in the Nav bar.
The 3 services are listed in the Nav bar, and no login is necessary for browsing the site. When user is querying the Nasa Image Library API,
they can select a specific picture which will be routed to a full screen image with title, description, authors, etc. This page has a "Add Image" button.
The database part of the site can only be used by logged in users.<br>
There are friendly messages displayed as action confirmations, also the app checks for response code status and gratiously catches any errors that 
might be coming from the API servers or from interractions with the database.<br>
The logged in username is diplayed in the navbar. "Guest" is displayed if user is not logged in.
All pages are responsive, the app will work fine on small screens, provided the connectivity speed is above 4G.
## Technology
The server side is built in Python3/Flask, frontend is server rendered using templating with Jinja2, HTML and JavaScript. Bootstrap and CSS is used for responsive styling, DB with PostgreSQL.
## Future addons
- Future pagination for the Nasa Image Library page. Currently the API retrieves 100 results per page,
and it defaults to "page=1" as one of the API parameters.<br>
###### Note - The pagination was intentionally not implemented on the Rover API because the raw data comes in bulk, without description. There is a lot of repetition in some responses. The image tiles are smaller to fit more on screen so the easiest way to deal with this is to use the page scroll instead of "Next Page" link. This approach might create a poor user experience for 3G/4G internet speeds, so likely pagination will be implemented here as well. ######
## Install
Go to your bash terminal.
- Create a virtual environment
> python3 -m venv venv
- Activate the venv
> source venv/bin/activate
- After cloning, install dependencies from requirements.txt
> pip install -r requirements.txt
###### The app was written in Python-3.8.10 - in case you need a specific Python version. ######
- ***While in (venv), set up 4 environmental variables from the terminal: API_KEY, FLASK_KEY, DB_USER, DB_PASSWORD. You can also save or export these values from secret.py file.***
> **Example:**
    FLASK_KEY = "_some_randomized_string_"
    API_KEY="DEMO_KEY"
    OR
    export FLASK_KEY="_some_randomized_string_"
    export API_KEY="DEMO_KEY"    
###### Note - If PostgreSQL is used, DB_USER and DB_PASSWORD are not needed. For MariaDB, a db user / password needs to be setup in MariaDB. My recommendation is to stick to PostgreSQL, as it has a simpler setup. For hosting reasons, I added MariaDB as a secondary option. iF no database is found, the app will default to hardcoded db selection. Uncomment the correct db use in the config part of app.py ######
You can quickly and easily get a new API key [here](https://api.nasa.gov) or you can use their DEMO_KEY.
>#### The rate limits for the DEMO_KEY are:
> - Hourly Limit: 30 requests per IP address per hour
> - Daily Limit: 50 requests per IP address per day

#### For Postgresql use:
- install PostgreSQL
> sudo apt-get install postgresql
- start PostgreSQL server
> sudo service postgresql start
- create DB
> createdb space
- create tables
> python seed.py

#### For Mariadb use:
- perform a secure installation of MariaDB. Multiple steps process.
- start Mariadb
> sudo service mysql start
- log in MariaDB with root account
> mariadb -u root -p
- create DB
> CREATE DATABASE space;
- verify db
> SHOW DATABASES;
> EXIT;
- create tables
> python seed.py

- start Flask server
> flask run
- go to http://127.0.0.1:5000/