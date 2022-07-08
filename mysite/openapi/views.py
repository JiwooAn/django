from urllib.parse import urlencode, quote_plus
from urllib.request import Request, urlopen
from django.http import HttpResponse


# Create your views here.
def index(request):
    url = "http://openapi.nsdi.go.kr/nsdi/BuildingAgeService/attr/getBuildingAge"
    query_params = '?' + urlencode({quote_plus('authkey'): '023b8185a334fe63350db8',
                                    quote_plus('pnu'): '1111012500100190000'
                                       , quote_plus('buldAge'): '6'
                                       , quote_plus('buldAgeSe'): '1'
                                       , quote_plus('format'): 'json'
                                       , quote_plus('numOfRows'): '10'
                                       , quote_plus('pageNo'): '1'
                                    })

    request = Request(url + query_params)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read()
    print(response_body)
    return HttpResponse("family & genus info upload")