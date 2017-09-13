import urllib.request
import json

link = "http://cricapi.com/api/cricketScore?apikey=kcfYi6vUJvhsUoai1WKygReg9Et1"
unique_id = "1117822"

teamLink = "http://cricapi.com/api/fantasySquad?apikey=kcfYi6vUJvhsUoai1WKygReg9Et1"
teamUniqueID = unique_id

req = urllib.request.urlopen(link+"&unique_id="+unique_id)


with urllib.request.urlopen(link+"&unique_id="+unique_id) as response:
    resp = response.getcode()
    if resp == 200:
        ref = json.load(response)
        print(ref["team-1"]+" v/s "+ref["team-2"])

        with urllib.request.urlopen(teamLink+"&unique_id="+teamUniqueID) as teamResp:
            team = json.load(teamResp)
            print("Today's "+team["squad"][0]["name"]+" Squad:\n")
            for num in team["squad"][0]["players"]:
                print(num["name"])

            print("\n\n")
            print("Today's "+team["squad"][1]["name"]+" Squad:\n")
            for num in team["squad"][1]["players"]:
                print(num["name"])

            print(ref['stat'])
            print(ref["score"]+"\n")
        #for keys in ref.keys():
        #    print(ref[keys])
        #print(ref)
        #raw_json = json.loads(response)
        #print(raw_json)
#        print(response)
