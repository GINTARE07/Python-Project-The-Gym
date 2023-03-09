
GYM MAMAGEMENT APP 

Build a software to help gym management to manage members details, memberships, members registration to Sessions etc.

MVP

The app allows the gym to register(add) new Members and edit existing members

The app allows the gym management to create and edit existing Sessions

The app allows the gym management to assign members attendance to specific sessions they attended. This helps to monitor the popularity of the sessions and which part of the day which sessions are more popular.

The app shows a list of all available Sessions.

Extensions

The app should allow the gym to restrict members for booking new Sessions for a week who missed 3 or more Sessions they booked in

The app should have a maximum capacity for Sessions, and only allow Members to book in if capacity allows.

The app should allow Sessions to be filtered by part of day the happening (morning sessions, afternoon sessions, evening sessions) 


The project was built using the following technologies:

Python
Flask
Jinja
HTML5
CSS3
PostgreSQL


Run Locally

To run the project locally, you'll need Python3, PostgresSQL and Flask installed.

Run the following commands to create the database, seed with sample data and start the app:

createdb gym_manager
psql -d gym_manager -f db/gym_manager.sql
python3 console.py
flask run
You can then visit http://127.0.0.1:4999/ to view and try it out!

