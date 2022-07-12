from urllib.parse import urlencode, quote_plus
from urllib.request import Request, urlopen
from django.http import HttpResponse
import xmltodict
import json

# Create your views here.
def index(request):
    url = "http://openapi.nsdi.go.kr/nsdi/BuildingAgeService/attr/getBuildingAge"
    query_params = '?' + urlencode({quote_plus('authkey'): '023b8185a334fe63350db8',
                                    quote_plus('pnu'): '1111012500100190000'
                                       , quote_plus('buldAge'): '6'
                                       , quote_plus('buldAgeSe'): '1'
                                       , quote_plus('numOfRows'): '10'
                                       , quote_plus('pageNo'): '1'
                                    })

    req = Request(url + query_params)
    req.get_method = lambda: 'GET'
    response_body = urlopen(req).read().decode('utf-8')
    json_response = json.dumps(xmltodict.parse(response_body), indent=4)
    return HttpResponse(json_response)