from flask_wtf import FlaskForm as Form
from flask_table import Table, Col, DateCol
from wtforms import StringField, IntegerField, FormField,SelectField, FieldList
import yaml
from flask import url_for
def get_states(return_dict=False):
    import os
    states_abr=r"states_abr.txt"
    dir_path = os.path.dirname(os.path.realpath(__file__))
    states_abr=os.path.join(dir_path, states_abr)
    with open(states_abr) as f:
        abrvs = yaml.load(f)
    if not return_dict:
       return [(v, k) for k,v in abrvs.items()]
    else:
       return abrvs

class StatesForm(Form):
      Local_Name = SelectField(
        "States",
        choices=get_states()
    )

# Declare table to display the data
class changeTable(Table):
    options={"table_id": "change_id"}
    classes = ["table", "table-bordered", "table-striped"]
    date = Col ('Date')
    positiveIncrease = Col("Daily number of confirmed cases")
    positive=Col("Total number of confirmed cases")
    death_increase=Col("Daily number of death")
    death = Col("Total number of deaths")


