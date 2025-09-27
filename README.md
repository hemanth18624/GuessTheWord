# Guess the Word - A Django Web Application


A modern, full-featured "Guess the Word" web application built with Python and Django. This project is a Wordle-like game that includes secure user authentication, role-based access, and a comprehensive reporting dashboard for superusers.

---

## Features

This application is built from the ground up to be secure, robust, and user-friendly, incorporating a wide range of modern web development practices.

* **Secure User Authentication**:
    * Separate registration and login portals for users and admin.
    * Custom validation rules for usernames (minimum 5 characters, upper/lowercase) and passwords (minimum 5 characters, must include alpha, numeric, and special characters `[$%*@]`).

* **Role-Based Access**:
    * **User Mode**: Players can register, log in, and play the game.
    * **Admin Portal**: Admin have exclusive access to a reporting dashboard after logging in through a separate portal.

* **Core Wordle-like Gameplay**:
    * A 5-letter word is randomly selected from the database for each game.
    * Users get a maximum of 5 attempts to guess the word.
    * **Color-Coded Feedback**: Letters are highlighted in green (correct letter, correct position), orange (correct letter, wrong position), or grey (letter not in word) after each guess.
    * Clear win/loss messages are displayed at the end of each game.

* **Daily Play Limit**:
    * Users are restricted to playing a maximum of 3 games per day to encourage daily engagement.

* **Admin Reporting Dashboard**:
    * **Daily Summary Report**: Shows the number of unique users who played and the total number of correct guesses for the current day.
    * **User-Specific Report**: Allows the admin to select any player from a dropdown menu and view their entire game history, including dates, words, and results.

* **Enhanced Security & UX**:
    * **Cache Control**: Implemented server-side cache-control headers to prevent browsers from caching sensitive pages (like logged-in game pages or login forms), fixing back/forward button issues after logout.
    * **Professional UI/UX**: All pages, including forms and game boards, are styled with Tailwind CSS for a modern, responsive, and professional look and feel.

---

## Tech Stack

* **Backend**: Python, Django
* **Database**: SQLite3 (Built-in)
* **Frontend**: HTML, Tailwind CSS
* **Development Environment**: Python Virtual Environment

---

## Setup and Installation

Follow these steps to get the project up and running on your local machine.

#### 1. Prerequisites
* Python 3.x
* pip (Python package installer)

#### 2. Clone the Repository
```bash
git clone https://github.com/hemanth18624/GuessTheWord.git
cd GuessTheWord
```

#### 3. Database and Initial Data
* Run ```bash python manage.py makemigrations```
* Run ```bash python manage.py migrate ```
* Run ```bash python manage.py load_words``` to populate the database with the initial set of words.

#### 4. Create a Superuser (for Admin access)
* Run ```bash python manage.py createsuperuser``` and follow the prompts. This account will be used to access the reports dashboard.

#### 5. Run the Development Server
* Run ```bash python manage.py runserver```
* Open your web browser and go to ```bash http://127.0.0.1:8000/ ```.

