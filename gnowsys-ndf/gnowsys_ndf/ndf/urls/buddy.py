from django.conf.urls import patterns, url

urlpatterns = patterns('gnowsys_ndf.ndf.views.buddy',
			url(r'^[/]$', 'list_buddy', name='list_buddy'),
			url(r'^search_buddy_list/', 'search_buddy_list', name='search_buddy_list'),
			url(r'^/update_buddies/$', 'update_buddies', name='update_buddies'),
		)
