# B"H
import json

def calculate_esg(response):
    sum_weighted_esg = 0
    sum_weight = 0
    esg_json = json.loads(response)
    
    for tr in esg_json["esgScore"]:
        sum_weighted_esg += esg_json["esgScore"][tr]['score']*esg_json["esgScore"][tr]['weight']
        sum_weight += esg_json["esgScore"][tr]['weight']

    if sum_weight == 0:
        return 0
    else:
        return (sum_weighted_esg/sum_weight)
