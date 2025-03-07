from django.http import JsonResponse

def api_home(request, *args,**kwargs):
    query_params= dict(request.GET)
    print(query_params)
    print(query_params.get('abc', [None])[0])
    print(request.headers)
    return JsonResponse({"message":"good"})