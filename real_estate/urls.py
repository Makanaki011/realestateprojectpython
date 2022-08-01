
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path

from listings.views import (Listing_list, 
Listing_retrieve, 
Listing_create, 
Listing_update, 
Listing_delete,
)
 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Listing_list),
    path('listings/<pk>/',  Listing_retrieve),
    path('listings/<pk>/edit/',  Listing_update),
    path('listings/<pk>/delete/',  Listing_delete),
    path('add-listing/', Listing_create)
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





