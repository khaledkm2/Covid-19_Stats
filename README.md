# Covid-19 data display
\This application has been written in Python 3.7 and Flask framework. 
\It is a fully working application but it has not been fully tested.
\The dependable packages are saved in requirments.txt
This is the command which can be used to run the application on the development server at the: 
    python manage.py  runserver -h 127.0.0.1 -p 5000
The server will run on the local host using port 5000, the user can select different port.
#Usage
The user can select US state from a pull-dwon menu at the main page then press "Submit" button.
Then, a tabular view will pop up which contains data related to Covid-19 for the select state.
The table columns can be sorted and the user can select how many rows to display in each pages.
The data is fetched at run time from https://covidtracking.com/data/api.
#Testing
The application has a basic test unit (test_app) which is extendable.
