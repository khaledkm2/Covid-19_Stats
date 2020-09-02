from app import covid_app
from datetime import datetime
import requests
import json
from  app.forms.forms_tabls import get_states

#https://api.covidtracking.com/v1/states/ca/daily.json



def get_val(item, val):
    if not item.get(val):
        val = 0
    else:
        val = item.get(val)

    return val

def get_data(state):
    covidtrackingUrl=covid_app.config.get('COVID_TRACK_URL')
    file_name = covid_app.config.get('JSON_FILE_NAME')
    api_url="%s/%s/%s"%(covidtrackingUrl,state,file_name)
    resp = requests.get(url=api_url,)
    data = json.loads(resp.text)
    if  isinstance(data, dict):
        if data.get("error")==True:
            return [], []

    returned_values=[]
    format_str = '%y/%m/%d'
    daily_death=0
    for i in range(0, len(data)):
        item=data[i]
        if not item.get("date"):
            continue
        date = datetime.strptime(str(item.get("date")), '%Y%m%d').date().strftime(format_str)
        death=get_val(item, "death")
        deathIncrease=get_val(item, "deathIncrease")
        death_increase=daily_death+deathIncrease


        returned_values.append({"date": date,"positiveIncrease" :get_val(item,"positiveIncrease"), "positive":get_val(item,"positive"), "death": death,"death_increase":death_increase })
    states = get_states(return_dict=True)
    st = [ky for ky, val in states.items() if val == state]
    return st,returned_values

