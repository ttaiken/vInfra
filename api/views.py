from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
import json


from azure.models import resource,resourcegroup,Hero
from .serializers import resourceSerializer, resourcegroupSerializer
# Create your views here.

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse,self).__init__(content,**kwargs)
    
def index(request):
    all_resource = resource.objects.all()
    json_list = []
    for post in all_resource:
        json_dict = {}
        json_dict['id'] = post.id
        json_dict['resourcegroupName'] = post.ResourceGroupName
        json_dict['resourcetype'] = post.ResourceType
        json_dict['location'] = post.Location
        json_dict['name'] = post.Name
        json_list.append(json_dict)
    
    response_data = {}
    result = {}
    result['status'] = 'success'
    result['message'] = 'Test response'
    response_data['result'] = result
    response_data['datas'] = json_list
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def heros(request):
    all_hero = Hero.objects.all()
    all_resource = resource.objects.all()
    json_list = []
    for post in all_hero:
        json_dict = {}
        json_dict['id'] = post.id
        json_dict['name'] = post.name
        json_list.append(json_dict)
        response_data = {}
    result = {}
    result['status'] = 'success'
    result['message'] = 'Test response'
    response_data['result'] = result
    response_data['datas'] = json_list
    
    # url(r'^users/(?P<user_id>\d+)/$', 'viewname', name='urlname')
    return HttpResponse(json.dumps(response_data), content_type="application/json")

@api_view(['GET'])
def resources(request):
    # all_Articles = Articles.objects.all()
    # json_list = []
    # for post in all_Articles:
        # json_dict = {}
        # json_dict['title'] = post.title
        # json_dict['content'] = post.content
        # json_list.append(json_dict)
    # import json
    resources = resource.objects.all()
    serializer = resourceSerializer(resources, many=True)
    # url(r'^users/(?P<user_id>\d+)/$', 'viewname', name='urlname')
    return JSONResponse(serializer.data)


@api_view(['GET'])
def resourcegroups(request):
    resourcegroups = resourcegroup.objects.all()
    serializer = resourcegroupSerializer(resourcegroups, many=True)
    return JSONResponse(serializer.data) 
# -----------GET parameters-----------------
# /products?price_lte=5000
# url(r'^products/$', 'viewname', name='urlname')
# def viewname(request):
    # price_lte = request.GET['price_lte']
# Code to filter products whose price is less than price_lte i.e. 5000
#------------POST parameters-------------
# url(r'^register/$', 'register', name='urlname')

# def register(request):
    # form = RegisterForm()
    # if request.method == "POST":
        # form = RegisterForm(request.POST) #if no files
        # if form.is_valid():
        #    do something if form is valid
    # context = {
        # 'form': form
    # }
    #request.POST['num'] 
    # return render(request, "template.html", context)
# ----------------Post Json -----------------
# @ensure_csrf_cookie
# def index(request):

    # if request.method == 'GET':
        # return JsonResponse({})

    # datas = json.loads(request.body)

    #requestには、param1,param2の変数がpostされたものとする
    # ret = {"data": "param1:" + datas["param1"] + ", param2:" + datas["param2"]}

    #JSONに変換して戻す
    # return JsonResponse(ret)
# ----------------------------------------------------
