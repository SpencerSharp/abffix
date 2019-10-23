import os
import filecmp
import json
import pandas as pd

old_export_filename = "oldexport.json"
new_export_filename = "newexport.json"

with open(old_export_filename,encoding='utf-8-sig') as oldexportfile:
    with open(new_export_filename,encoding='utf-8-sig') as newexportfile:
        old = pd.read_json('['+oldexportfile.read()+']',orient='records')
        new = pd.read_json('['+newexportfile.read()+']',orient='records')

        changed = new.copy()
        old_colors = old['teams'][0][0]['colors']
        changed['teams'][0][0]['colors'] = old_colors
        with open('fixedexport.json','w+',encoding='utf-8-sig') as fixedexport:
            temp = changed.to_json(orient='records')
            temp = temp[1:-1]
            fixedexport.write(temp)
        
