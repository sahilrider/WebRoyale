from django.conf.urls import url

from . import views
app_name='card'
urlpatterns=[
	url(r'^$',views.index,name='index'),
	url(r'^arena/$',views.arena_index,name='arena_index'),
	url(r'^arena/(?P<arena_number>[0-9]+)/$', views.view_arena, name='view_arena'),
	url(r'^rarity/(?P<rarity_id>[0-9]+)/$', views.view_rarity, name='view_rarity'),
	url(r'^type/(?P<type_id>[0-9]+)/$', views.view_type, name='view_type'),
	url(r'^card/(?P<card_id>[0-9]+)/$', views.view_card, name='view_card'),
]

