from django.conf.urls import patterns, url

urlpatterns = patterns('gnowsys_ndf.ndf.views.e-book',
                       	url(r'^[/]$', 'ebook_listing', name='e-book'),
						url(r'^/page-no=(?P<page_no>\d+)/$', 'ebook_listing', name='e-book_paged'),
                       )
