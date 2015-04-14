#coding: utf-8 

from django.db import models
from djangosphinx import SphinxSearch
from tagging_autocomplete.models import TagAutocompleteField

class Seller(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=70)
    phone = models.CharField(max_length=70)
    image1 = models.URLField()
    image2 = models.URLField()
    descr = models.CharField(max_length=1000)
    website = models.URLField()
    map_url = models.CharField(max_length=1000)
    work_days = models.CharField(max_length=500)
    work_time = models.CharField(max_length=100)
    hit_counts = models.IntegerField()
    views = models.IntegerField()
    http_click = models.IntegerField()
    sef_name = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class Goods(models.Model):
    name = models.CharField(max_length=300)
    author = models.CharField(max_length=50)
    subsection_id = models.IntegerField()
    brand_id = models.IntegerField()
    img_url = models.URLField()
    img_url2 = models.URLField()
    sef_name = models.CharField(max_length=300)
    date = models.DateField()
    editor = models.CharField(max_length=50)
    reason = models.CharField(max_length=50)
    views = models.IntegerField()
    forum_id = models.IntegerField()
    prod_url = models.URLField()
    descr = models.CharField(max_length=1000)
    descr2 = models.CharField(max_length=2000)
    price = models.IntegerField()
    v_id = models.IntegerField()
    kupon = models.CharField(max_length=1000)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ['-views']
        
    search = SphinxSearch(
            index='search',
            weights={
            'name':100,
            'descr':90,
            'descr2':80},
            mode='SPH_MATCH_PHRASE',
#            rankmode='SPH_RANK_NONE',
            )	
    name = TagAutocompleteField()
