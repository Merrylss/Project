from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
# 装饰器函数，要求登录访问
from django.contrib.auth.decorators import login_required
# 固定请求方式
from django.views.decorators.http import require_GET, require_POST
# 事务管理
from django.db import transaction


from . import models


@login_required
@transaction.atomic
def store_add(request):
    """
    开店视图函数
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'stores/store_add.html', {})
    elif request.method == 'POST':
        name = request.POST['name']
        intro = request.POST['intro']
        user = request.user

        # 设置原点
        s_id = transaction.savepoint()
        try:
            try:
                cover = request.FILES['cover']
                store = models.Store(name=name, intro=intro, user=user, cover=cover)
            except:
                store = models.Store(name=name, intro=intro, user=user)
            store.save()
            transaction.savepoint_commit(s_id)
            return render(request, 'stores/store_add.html', {'error_code': 0, 'error_msg': '开店成功！'})
        except:
            transaction.savepoint_rollback(s_id)
            return render(request, 'stores/store_add.html', {'error_code': -1, 'error_msg': '开店失败！'})


@require_GET
@login_required
def store_info(request, s_id):
    """
    店铺信息视图函数
    :param request:
    :return:
    """
    store = models.Store.objects.get(id=s_id)
    print(store)
    return render(request, 'stores/store_info.html', {'store': store})
    # return redirect(request, 'stores/store_info.html', {'store': store})


@require_GET
@login_required
def store_list(request):
    """
    店铺列表视图函数
    :param request:
    :return:
    """
    store_list = models.Store.objects.filter(user=request.user, status__in=[0, 1])
    return render(request, 'stores/store_list.html', {'store_list': store_list})


@login_required
def store_update(request, store_id):
    """
    店铺更新视图函数
    :param request:
    :return:
    """
    store = models.Store.objects.get(id=store_id)
    if request.method == 'GET':
        return render(request, 'stores/store_update.html', {'store': store})
    elif request.method == 'POST':
        name = request.POST['name']
        status = request.POST['status']
        try:
            cover = request.FILES['cover']
            store.cover = cover
        except:
            pass
        store.name = name
        store.status = status
        store.save()
        return redirect(reverse('stores:store_info', kwargs={'s_id': store_id}))


@require_GET
@login_required
def store_close(request, store_id):
    """
    关闭店铺
    :param request:
    :return:
    """
    store = models.Store.objects.get(id=store_id)
    store.status = 0
    store.save()
    return redirect(reverse('stores:store_info', kwargs={'s_id': store_id}))


@require_GET
@login_required
def store_del(request, store_id):
    """
    删除店铺
    :param request:
    :return:
    """
    store = models.Store.objects.get(id=store_id)
    store.status = 2
    store.save()
    return render(request, 'stores/store_list.html')