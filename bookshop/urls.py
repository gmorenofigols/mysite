from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home', views.home, name='home'),
    url(r'^search?', views.search, name='search'),
    url(r'^books/$', views.books, name='books'),
    url(r'^books/(?P<book_id>[0-9]+)/$', views.book_description, name='book_details'),
    url(r'^authors/$', views.authors, name='authors'),
    url(r'^authors/(?P<author_id>[0-9]+)/$', views.author_description, name='author_details'),
]
