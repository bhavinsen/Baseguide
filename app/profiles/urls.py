from django.urls import path 
from .views import profile_views, api_views
from profiles.views.invoice import create_invoice, download_invoices,view_invoices, update_invoice, delete_invoice, update_status
from profiles.views import booking

app_name = "profiles"

urlpatterns = [
    #profile
    path("create-profile/", profile_views.create_profile, name="create_profile"),
    path("profile-details/<int:pk>/", profile_views.details_profile, name="details_profile"),
    path("profile-update/<int:pk>/", profile_views.update_profile, name="update_profile"),
    path("profile-delete/<int:pk>/", profile_views.delete_profile, name="delete_profile"),

    #API
    path("api/", api_views.ProfilesApi.as_view()),
    path("api/create-profile/", api_views.ProfileCreateApi.as_view(), name='create_profile_api'),
    path("api/update-profile/<int:pk>/", api_views.ProfileUpdateApi.as_view()),
    path("api/delete/<int:pk>/", api_views.ProfileDeleteApi.as_view()),
    
    path("artist_api/", api_views.ArtistApi.as_view()),
    path("artist_api/create-artist/", api_views.ArtistCreateApi.as_view()),
    path("artist_api/update-artist/<int:pk>/", api_views.ArtistUpdateApi.as_view()),
    path("artist_api/delete/<int:pk>/", api_views.ArtistDeleteApi.as_view()),
    
    path("partner_api/", api_views.PartnerApi.as_view()),
    path("partner_api/create-partner/", api_views.PartnerCreateApi.as_view()),
    path("partner_api/update-partner/<int:pk>/", api_views.PartnerUpdateApi.as_view()),
    path("partner_api/delete/<int:pk>/", api_views.PartnerDeleteApi.as_view()),
    
    path("invoice_api/create-invoice/", api_views.InvoiceCreateApi.as_view()),
    
    #Invoice
    path("invoice/", create_invoice, name='invoice'),
    path("download-invoice/<int:pk>/", download_invoices, name='download_invoice'),
    path("view_invoices/<int:pk>/", view_invoices, name='view_invoices'),
    path("update_invoices/<int:pk>/", update_invoice, name='update_invoices'),
    path('delete-invoice/<int:invoice_id>/', delete_invoice, name='delete_invoice'),
    path("update-status/<int:invoice_id>/", update_status, name="update_status"),
    
    #Booking
    path('bookings/', booking.booking_create, name='booking_list'),
    path('bookings/update/<int:pk>/', booking.booking_update, name='booking_update'),
    path('delete-booking/<int:pk>/', booking.booking_delete, name='booking_delete'),
    

]
