from django.http import HttpResponse, JsonResponse
from rest_framework import generics
from profiles.serializers.serializers_profile import ProfileSerializer
from profiles.serializers.serializer_artist import ArtistSerializer
from profiles.serializers.serializers_partner import PartnerSerializer
from profiles.serializers.serializers_invoice import InvoiceSerializer
from user_profile.models.partner import Partner
from user_profile.models.artist import Artist
from user_profile.models.profile import Invoice
from profiles.models.profile import Profile
from rest_framework import permissions

class ProfileCreateApi(generics.CreateAPIView):
    """
    API endpoint that allows users to be created.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProfilesApi(generics.ListAPIView):
    """
    API endpoint that allows users to get profile list.
    """
    queryset =Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProfileUpdateApi(generics.RetrieveUpdateAPIView):
    """
    API endpoint that allows users to update profile.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProfileDeleteApi(generics.DestroyAPIView):
    """
    API endpoint that allows users to delete a profile.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    

class ArtistCreateApi(generics.CreateAPIView):
    """
    API endpoint that allows users to be created.
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class ArtistApi(generics.ListAPIView):
    """
    API endpoint that allows users to get Artist list.
    """
    queryset =Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class ArtistUpdateApi(generics.RetrieveUpdateAPIView):
    """
    API endpoint that allows users to update Artist.
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class ArtistDeleteApi(generics.DestroyAPIView):
    """
    API endpoint that allows users to delete a profile.
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [permissions.IsAuthenticated]
    
# Partner 
class PartnerCreateApi(generics.CreateAPIView):
    """
    API endpoint that allows users to be created.
    """
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class PartnerApi(generics.ListAPIView):
    """
    API endpoint that allows users to get Artist list.
    """
    queryset =Partner.objects.all()
    serializer_class = PartnerSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class PartnerUpdateApi(generics.RetrieveUpdateAPIView):
    """
    API endpoint that allows users to update Artist.
    """
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class PartnerDeleteApi(generics.DestroyAPIView):
    """
    API endpoint that allows partner to delete a profile.
    """
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
class InvoiceCreateApi(generics.CreateAPIView):
    """
    API endpoint that allows invoice to be created.
    """
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]