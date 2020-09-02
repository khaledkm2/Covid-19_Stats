# Covid-19 data display <br />
This application has been written in Python 3.7 and Flask framework. <br />
It is a fully working application but it has not been fully tested.<br />
The dependable packages are saved in requirments.txt. <br />
This is the command which can be used to run the application on the development server: <br />
<br/>
**python manage.py  runserver -h 127.0.0.1 -p 500** <br />
 <br/>
- The server will run on the local host using port 5000, the user can select different port.<br />
# Usage<br />
The user can select a US state from a pull-down menu at the main page then press "Submit" button.<br />
Then, a tabular view will pop up which contains data related to Covid-19 for the selected state.<br />
The table columns can be sorted and the user can select how many rows to display in each page.<br />
The data is fetched at run time from https://covidtracking.com/data/api.<br />
# Testing<br />
The application has a basic test unit (test_app) which is extendable.<br />
