from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
   path('', views.home, name = 'start'),
   path('start', views.start, name ='start'),
   path('signup', views.signup, name ='signup'),
   path('reset', views.reset, name ='reset'),
   path('location', views.location, name ='location'),
   path('forgot', views.forgot, name ='forgot'),
   path('classify', views.classify, name ='classify'),
   path('feedback', views.feedback, name ='feedback'),
   path('feedbackLoc', views.feedbackLoc, name ='feedbackLoc'),
   path('logout_view',views.logout_view, name = 'logout_view'),
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)