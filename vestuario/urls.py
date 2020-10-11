from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.pocetna, name='pocetna'),
    path('contact/', views.contact, name='kontakt'),
    path('stil/', views.stil, name='stil'),
    path('proizvod/', views.proizvod, name='proizvodi'),
    path('register/', views.UserFormView.as_view(), name='register'),
    path('cart/', views.cart, name='korpa'),
    path('checkout/', views.checkout, name='isplata'),
    path('login/', auth_views.LoginView.as_view(template_name='vestuario/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='vestuario/logout.html'), name='logout'),
    path('profile/', views.profile, name='profil'),
    path('proizvod/update_item/', views.updateItem, name='update_item'),
    path('cart/update_item/', views.updateItem, name='update_item'),
    path('checkout/process_order/', views.processOrder, name='process_order')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)