# Alice Li

from apiclient.errors import HttpError

import json, requests, os, io

DEVELOPER_KEY = "AIzaSyAa53IZ5AYwWiWNL2hpV8aTf-jd-AlxeZs"
BASE_URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
LOCATION = '30.400927,-97.693073'    # not real current location

def roadside_search(towNeeded):
    if(towNeeded):
        httpResp = httpResp = requests.get(BASE_URL,
                                params={'location': LOCATION,
                                        'type': 'car_repair',
                                        'keyword': 'tow',
                                        'rankby': 'distance',
                                        'openNow': True,
                                        'key': DEVELOPER_KEY})
    else:
        httpResp = requests.get(BASE_URL,
                            params={'location': LOCATION,
                                    'type': 'car_repair',
                                    'rankby': 'distance',
                                    'openNow': True,
                                    'key': DEVELOPER_KEY})

    if httpResp.status_code == 200:
        results = json.loads(httpResp.content)
        results = results['results']

        attributes = ['name', 'vicinity']

        repairShops = []
        for result in results:
            repairShop = {}
            for attr in attributes:
                repairShop[attr] = result[attr]

            repairShops.append(repairShop)

        resultFile = open('repairShops.json', 'w')
        json.dump(repairShops, resultFile)
        return httpResp.content

    else:
        print "Request not fulfilled"
        print httpResp.status_code, httpResp.reason, httpResp.text


if __name__ == "__main__":
  try:
    roadside_search(True)
  except HttpError, e:
    print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)
