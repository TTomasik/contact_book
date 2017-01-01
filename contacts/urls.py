"""contacts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from contact_book.views import NewContact, EditContact, DeleteContact, ShowContact, ShowContactList, FindContact


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^new$', NewContact.as_view()),
    url(r'^modify/(?P<contact_id>(\d)+)$', EditContact.as_view()),
    #url(r'^delete/(?P<contact_id>(\d)+)$', DeleteContact.as_view()),
    url(r'^show/(?P<contact_id>(\d)+)$', ShowContact.as_view()),
    url(r'^$', ShowContactList.as_view()),
    url(r'^delete$', DeleteContact.as_view()),
    url(r'^find$', FindContact.as_view()),
    url(r'^edit$', EditContact.as_view()),

    
               
]
