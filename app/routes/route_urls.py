from . import routes
from flask import request, render_template
from  app.forms.forms_tabls import get_states, StatesForm, changeTable
from app.routes.routes_util import get_data

'''
Contains the application main routes
'''
@routes.route('/',methods=['POST', 'GET'])
def index():
    statesForm=StatesForm()
    if statesForm.validate_on_submit():
        data = request.form.to_dict()
        print (data)
        state=data.get("Local_Name")

        st, values=get_data(state)

        tabel_=changeTable(values)
        return render_template('changes.html', table=tabel_, state=st[0])
    return render_template("index.html", title="Covid update",states_form=statesForm)

