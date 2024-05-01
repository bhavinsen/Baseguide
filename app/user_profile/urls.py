from django.urls import path
from .views.profile_views import create_profile
from .views.artist_views import create_artist, artist_list, update_artist, delete_artist, artist_details
from .views.partner_views import create_partner, partner_list, update_partner, delete_partner, partner_details
from profiles.views.invoice import create_invoice

app_name = "user_profile"

urlpatterns = [
    path("create-profile/", create_profile, name="create-profile"),
    #artist
    path("create-artist/", create_artist, name="create_artist"),
    path("artist-list/", artist_list, name="artist_list"),
    path("artist/<int:pk>/", artist_details, name="artist_details"),
    path("update-artist/<int:pk>/<str:user_pk>/", update_artist, name="update_artist"),
    path("delete-artist/<str:pk>/", delete_artist, name="delete_artist"),

    #partner
    path("create-partner/", create_partner, name="create_partner"),
    path("partner-list/", partner_list, name="partner_list"),
    path("partner/<int:pk>/", partner_details, name="partner_details"),
    path("update-partner/<int:pk>/<str:user_pk>/", update_partner, name="update_partner"),
    path("delete-partner/<str:pk>", delete_partner, name="delete_partner"),
    
    path("invoice/", create_invoice, name='invoice'),
]
