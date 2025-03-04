import os
import sys
import googlesearch as gs
import subprocess
import webbrowser
import re
import csv
from datetime import date


try:
	from googlesearch import search
except ImportError: 
	print("No module named 'google' found")

# input and configuration
query = "stellenagebote programmierer \"python\""
keywords=["python","django"]
result= {}#{"fsfs":["dsjhdk","jhjdhad"],"fduah":["dsjdhdk","jhewrwejdhad"]}
linkPattern = r'https://[\w]*\.(.*)\..+'
sublinkPattern = r'href="\S+"'

#""" 
with open("_".join(["GglSearch","_".join(re.findall(r'[\w]+',query)[:2]),str(date.today()),".csv"]),"w+") as f:
    write= csv.writer(f)
    for g_result in search(query,tld='de', num=10, stop=10,pause=2):
        try:
                sourceName=re.search(linkPattern,g_result)#Name of the link
                #print(sourceName)
                for kw in keywords:
                    page=gs.get_page(g_result,gs.get_random_user_agent(),False)
                    if 	str(page).find(kw)>-1:
                        if sourceName[1] not in result.keys():
                            sublinks=re.findall(sublinkPattern,str(page))
                            #print(sublinks)
                            if sublinks :
                                for sublink in sublinks:
                                    if sublink.find(kw)>-1:
                                        if sourceName[1] in result.keys():
                                            result[sourceName[1]].append(sublink)
                                        else:
                                            result[sourceName[1]]= [sublink]
                        #print([sourceName[1]]+result[sourceName[1]])       
                            write.writerow([sourceName[1]]+result[sourceName[1]])
        except BaseException:
            continue
f.close()
print(result)

	