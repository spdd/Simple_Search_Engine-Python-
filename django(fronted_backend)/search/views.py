#coding: utf-8 

from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.cache import cache_page
from django.shortcuts import render_to_response
from django.http import Http404
from irkonline.search.models import Goods, Seller 
from django.template import RequestContext
from django.utils import simplejson
from irkonline.search.forms import SearchForm
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def image(request):
    return render_to_response('search_result.html')

def search(request):
    form = SearchForm()
    error = []
    if 'search' in request.GET:
        q = request.GET['search']
        if not q:
            error.append('Enter query')
        elif len(q) > 100:
            error.append('Enter query len < 100')
        else:
            goods = Goods.search.query(q).set_options(passages=True,
						      passages_opts={
						      'before_match':'<b>',
						      'after_match':'</b>',
						      'chunk_separator':'...',
						      'around':6,
						      'limit':256,})
            return render_to_response('search_results.html',
                                  {'goods':goods, 
                                   'query':q,
                                   'form':form}, context_instance=RequestContext(request))
    return render_to_response('search_form.html', {'error': error, 'form':form})

def pager(x): 
    try:
        if pages[x]:
            if len(pages) == 1 or (x != -1 and pages[x] == pages[-1]):
                return ''
            else:
                return pages[x]
    except IndexError:
        return ''
    
def autocompleteSearch(request):
    error = []
    if 'search' in request.GET:
        q = request.GET['search']
        if not q:
            error.append('Enter query')
        elif len(q) > 100:
            error.append('Enter query len < 100')
    	if len(q) > 2:
        	model_results = Goods.objects.filter(name__icontains=q)
        	results = [ x.name for x in model_results ]
		json = simplejson.dumps(results)
		return HttpResponse(json, mimetype='application/json')
