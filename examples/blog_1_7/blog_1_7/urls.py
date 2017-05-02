from django.conf.urls import include, url

urlpatterns = [
    url(r'^mongonaut/', include('mongonaut.urls')),
    url(r'^', include('articles.urls')),
]
