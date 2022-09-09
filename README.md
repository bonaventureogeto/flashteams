# flashteams

# Introduction

The goal of this project is to create a simple to use team management system where one can create a team or organization,

invite memebers to join, and members can see their teammates.

<!-- ![Default Home View](__screenshots/home.png?raw=true "Title") -->

### Main features

- Create and delete a Team or Organization

- Send invites via email

- Dashboard containing a list of teams and teammates

- User registration and logging in

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/USERNAME/{{ project_name }}.git
    $ cd {{ project_name }}

Activate the virtualenv for your project.

Install project dependencies:

    $ pip install -r requirements.txt

Then simply apply the migrations:

    $ python manage.py migrate

You can now run the development server:

    $ python manage.py runserver
