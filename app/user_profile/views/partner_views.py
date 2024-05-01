from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from authentication.models import CustomUser
from user_profile.models.artist import Artist
from django.http import HttpResponse, HttpResponseRedirect
from user_profile.forms import CreateProfile, CreatePartner, CreateUserForm
from user_profile.models.partner import Partner
from user_profile.models import Profile
from django.db import transaction
# Create your views here.

@login_required
@transaction.atomic
def create_partner(request):
    if request.method == "POST":
        # Personal Information
        user_form = CreateUserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data['username']
            email = user_form.cleaned_data['email']
            owner_id = CustomUser.objects.get(username=username, email=email, is_staff=False)

            # Profile Information
            name = request.POST['name']
            phone_number = request.POST['phone_number']
            bio = request.POST['bio']
            location = request.POST['location']
            is_verified = request.POST.get('is_verify', False)
            if is_verified == 'on':
                is_verified=True
            gender = request.POST['gender']
            date_of_birth = request.POST['date_of_birth']
            type = request.POST['type']
            profile_photo = request.FILES['profile_photo']
            
            profile = Profile.objects.create(
                owner_id=owner_id,
                bio=bio,
                location=location,
                is_verified=is_verified,
                date_of_birth=date_of_birth,
                gender=gender,
                profile_photo=profile_photo if profile_photo else None,
                type=type,
                name=name,
                phone_number=phone_number
            )
        
            # Company Details
            company_name = request.POST['company_name']
            coc_number = request.POST['coc_number']
            street = request.POST['street']
            city = request.POST['city']
            country = request.POST['country']
            zipcode = request.POST['zipcode']
            
            # Payment Information
            accountholder = request.POST['accountholder']
            bankaccount_number = request.POST['bankaccount_number']
            bic_code = request.POST['bic_code']
            
            # Partner Details
            phone_number = request.POST['phone_number']
            partner = Partner.objects.create(
                company_name=company_name,
                coc_number=coc_number,
                street=street,
                city=city,
                country=country,
                zipcode=zipcode,
                accountholder=accountholder,
                bankaccount_number=bankaccount_number,
                bic_code=bic_code,
                profile = profile,
                phone_number=phone_number,
            )
            partner.artist.set([int(request.POST['artists'])])
            partner.save()
            messages.success(request,"Your Partner has been created")
            return HttpResponseRedirect("/profile1/partner-list/")

    user_form = CreateUserForm()
    artists = Artist.objects.all()
    return render(request, "partner/create_partner.html", {"user_form": user_form, "artists":artists}) 


@login_required
def partner_list(request):
    partners = Partner.objects.all()
    context = {
        "partners": partners,
    }
    return render(request, "partner/partner_list.html", context) 


@login_required
def partner_details(request, pk):
    partner = Partner.objects.get(pk=pk)
    context = {
        "partner": partner
    }
    return render(request, "partner/partner_details.html", context)


@login_required
def update_partner(request, pk, user_pk):
    partner = Partner.objects.get(id=pk)
    user = CustomUser.objects.get(id=user_pk)
    profile = Profile.objects.get(owner_id=user)
    partner_form = CreatePartner(request.POST or None, instance= partner)
    profile_form = CreateProfile(request.POST or None, instance=profile)
    user_form = CreateUserForm(request.POST or None, instance=user)

    if partner_form.is_valid() and profile_form.is_valid() and user_form.is_valid():
        partner_form.save()
        profile_form.save()
        user_form.save()
        messages.success(request,"Profile has been updated")
        return HttpResponseRedirect(request.path_info)
    context = {
        "partner_form":partner_form,
        "profile_form":profile_form,
        "user_form":user_form
    }   
    return render(request, "partner/partner_update.html", context)


@login_required
def delete_partner(request, pk):
    user = CustomUser.objects.get(pk=pk)
    user.delete()
    return HttpResponseRedirect("/profile1/partner-list/")