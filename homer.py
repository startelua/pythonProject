#https://github.com/sipcapture/homer-api/blob/master/apidoc/doc.php
import json

import requests
import datetime;




def homer_api(s,token,t_start,t_end,n_from,n_to):

 #Login and get Token
 url = 'http://172.18.18.116:9080/api/v3/search/message'


 json_data='{"timestamp":{"from":1433529542283,"to":1682074937000},"param":{"search":{"from_user":"79588753252"},"location":{"node":"single"}}}'
 x = s.post(url, json = json_data,headers={'Authorization': 'Bearer ' + token})
 print(x.status_code)
 print(x.content)



 print("call data\n")
 json_str='{"config":{"protocol_id":{"name":"SIP","value":1},"protocol_profile":{"name":"call","value":"call"}},"param":{"transaction":{},"limit":200,"orlogic":false,"search":{"1_call":[{"name":"data_header.from_user","value":"%(nomer)s","func":null,"type":"string","hepid":1}]}},"timestamp":{"from":1682024400000,"to":%(ts)s000}}' % {"ts":t_end,"nomer":n_from}

 json_data=json.loads(json_str)

 url='http://172.18.18.116:9080/api/v3/search/call/data'
 x = s.post(url, json = json_data,headers={'Authorization': 'Bearer ' + token})
 print(x.status_code)
 print(x.content)

 callid=""

 for x in x.json()["data"]:
   print("\n\rx ",x)
   if x['method']=='BYE' :
      print("\n\rfrom",x['aliasSrc'],"to ",x['aliasDst'] )
      print("\n\rcseq ",x['cseq'])
      callid=x['callid']

 print("callid",callid)


 print("call translation\n")
 j_string='{"param":{"transaction":{"call":true,"registration":false,"rest":false},"limit":200,"orlogic":false,"search":{"1_call":{"id":393731018,"callid":["%(id)s"]}},"location":{"node":["localnode"]},"timezone":{"value":-180,"name":"Local"}},"timestamp":{"from":1682074317012,"to":%(ts)s000}}'% {"ts":t_end,"id":callid}
 json_data=json.loads(j_string)
 url='http://172.18.18.116:9080/api/v3/call/transaction'
 x = s.post(url, json = json_data,headers={'Authorization': 'Bearer ' + token})
 print(x.status_code)
 print(x.content)
 #"method":"BYE"
 for x in x.json()["data"]["messages"]:
 #  print("\n\rx ",x)
   if x["method"] == "BYE":
      print("raw",x["raw"])


if __name__ == '__main__':
    s = requests.Session()
    # Login and get Token
    url = 'http://172.18.18.116:9080/api/v3/auth'
    json_data = {"username": "admin", "password": "sipcapture"}
    x = s.post(url, json=json_data)
    print(x.content)
    token = x.json()['token']
    print("Token is: " + str(token))
    ct = datetime.datetime.now()

    t_start=0
    t_end = int(ct.timestamp())
    print("timestamp:-", int(t_end))
    #n_from = 79588753252
    n_from=79378042112
    n_to=0
    ret_homer=homer_api(s,token,t_start,t_end,n_from,n_to)

