from django.shortcuts import render
from cmdb import models


def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # 添加到数据库
        models.UserInfo.objects.create(user=username, pwd=password)

    # 从数据库中读取数据
    user_list = models.UserInfo.objects.all()

    return render(request, 'index.html', {'data': user_list})
