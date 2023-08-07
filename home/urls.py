from django.conf import settings
from home import views
from django.conf.urls.static import static
from django.urls import path, include, reverse_lazy


urlpatterns = [
    path('', views.index, name='index'),
    path('amazon', views.amazon, name='amazon'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('flipkart', views.flipkart, name='flipkart'),
    path('pricetracker', views.pricetracker, name="pricetracker"),
    path('register', views.registers, name="register")

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
