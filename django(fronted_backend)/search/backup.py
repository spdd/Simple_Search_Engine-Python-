from django.shortcuts import render_to_response
from django.http import Http404
from irkonline.search.models import Goods 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def image(request):
    return render_to_response('search_result.html')

def search(request, j='1'):
    try:
        j = int(j)
    except ValueError:
        raise Http404()
    error = []
    p = 2
    g = []
    if 'q' in request.GET:
        q = request.GET['q'].split('/')[0]
        if not q:
            error.append('Enter query')
        elif len(q) > 100:
            error.append('Enter len < 20')
        else:
            try:
                if request.GET['q'].split('/')[1]:
                    j = int(request.GET['q'].split('/')[1])
            except IndexError: pass
            goods = Goods.objects.filter(name__icontains=q)
            paginator = Paginator(goods, 2)
            page = request.GET.get('page')
            try:
                goods_list = paginator.page(page)
            except PageNotAnInteger:
                goods_list = paginator.page(1)
            except EmptyPage:
                goods_list = paginator.page(paginator.num_pages)
            global pages
            pages = []
            pg = len(goods)/p
            for i in range(pg):
                pages.append(i+1)
            return render_to_response('search_results.html',
                                  {'goods':goods[p*j-p:p*j], 
                                   'query':q, 
                                   'lengoods':goods, 
                                   'pg_1': pager(0),
                                   'pg_n1':pager(j),
                                   'pg_n2':pager(j+1),
                                   'pg_n3':pager(j+2),
                                   'pg_last':pager(-1),
                                   'goods_list':goods_list})
    return render_to_response('search_form.html', {'error': error})

def pager(x): 
    try:
        if pages[x]:
            if len(pages) == 1 or (x != -1 and pages[x] == pages[-1]):
                return ''
            else:
                return pages[x]
    except IndexError:
        return ''
    