from django.conf.urls import url
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^countries/$',countries,name='countries'),
    url(r'^categories/$',categories,name='categories'),
    url(r'^month/$',month,name='month'),
    url(r'^aboutus/$',aboutus,name='aboutus'),
    url(r'^contactus/$',contactus,name='contactus'),
    url(r'^india/$',india,name='india'),
    url(r'^city_name/(.*)/(.*)/$',city,name='city_name'),
    url(r'^japan/$',japan,name='japan'),
    url(r'^argentina/$',argentina,name='argentina'),
    url(r'^brazil/$',brazil,name='brazil'),
    url(r'^canada/$',canada,name='canada'),
    url(r'^china/$',china,name='china'),
    url(r'^madagascar/$',madagascar,name='madagascar'),
    url(r'^uae/$',uae,name='uae'),
    url(r'^usa/$',usa,name='usa'),
    url(r'^france/$',france,name='france'),
    url(r'^greece/$',greece,name='greece'),
    url(r'^egypt/$',egypt,name='egypt'),
    url(r'^sweden/$',sweden,name='sweden'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
