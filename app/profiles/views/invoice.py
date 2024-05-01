from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from user_profile.models.profile import Invoice
from user_profile.models.artist import Artist
from user_profile.models.partner import Partner

from django.http import HttpResponse
from django.template.loader import render_to_string
from django.template.loader import get_template
from django.conf import settings
from datetime import date, timedelta
from xhtml2pdf import pisa
from io import BytesIO
import json

@login_required
def create_invoice(request):
    try:
        artist_id = request.GET.get('artist_id', None)
        invoice_data = Invoice.objects.filter(artistname_id=artist_id, created_by=request.user) if artist_id else Invoice.objects.filter(created_by=request.user)
        artist = Artist.objects.all()
        partner = Partner.objects.all()
        invoice_amount = []
        paid_invoices = Invoice.objects.filter(paid=False)
        for invoice in invoice_data:
            invoice_dict={}
            amount = list(invoice.amounts.values())
            sum_result = sum(int(x) for x in amount)
            invoice_dict['total'] = sum_result
            invoice_dict['invoice_id'] = invoice.id
            invoice_amount.append(invoice_dict)
    except:
        pass
          
    if request.method == "POST":
        serviceData=json.loads(request.POST['values'])
        services_dict = {}
        amounts_dict = {}

        def get_index(key):
            return int(key.replace("servicesname", "").replace("amount", ""))

        for data in serviceData:
            key = data["name"]
            value = data["value"]

            if "servicesname" in key:
                index = get_index(key)

                services_dict[index] = value
            elif "amount" in key:
                index = get_index(key)

                amounts_dict[index] = value

        services_list = dict(sorted(services_dict.items()))
        amounts_dict = dict(sorted(amounts_dict.items()))
        invoice_name=request.POST['invoice_name']
        duedate=request.POST['duedate']
        partnername=Partner.objects.get(id = request.POST['partnername'])
        artistname =Artist.objects.get(id = request.POST['artistname'])
        paid = request.POST.get('paid', False)
        if paid == 'on':
            paid=True
        vat = request.POST.get('vat', False)
        if vat == 'on':
            vat=True
        Invoice.objects.create(
            created_by = request.user,
            invoice_name=invoice_name, 
            duedate=duedate,
            partnername=partnername, 
            artistname=artistname, 
            services=services_list, 
            amounts=amounts_dict,
            paid=paid,
            vat=vat
            )
    return render(request, 'invoice_details.html', {"datas": invoice_data, "artists": artist, "partners":partner, "amounts":invoice_amount, "paid_invoices":paid_invoices}) 

@login_required
def download_invoices(request, pk):
    invoice_data=Invoice.objects.get(id=pk)
    invoice_dict={}
    invoice_date = str(date.today().year) +"-"+str(date.today().month)+"-"+str(date.today().day)
    due_date = date.today()+timedelta(days=14)
    dueDate = str(due_date.year)+"-"+str(due_date.month)+"-"+str(due_date.day)
    amount = list(invoice_data.amounts.values())
    subtotal = sum(int(x) for x in amount)
    invoice_dict['total'] = subtotal
    invoice_dict['invoice_id'] = invoice_data.id
    tax = (21 if invoice_data.vat else 0)
    tax_amount = round((subtotal*tax)/100)
    finalamount = round((subtotal + tax_amount))
    services = list(invoice_data.services.values())
    amounts = list(invoice_data.amounts.values())     
    dictionary = dict(zip(services, amounts))
    data = {"data":invoice_data, "subtotal":subtotal, "tax":tax, "tax_amount":tax_amount, "finalamount":finalamount, "values": dictionary, "invoice_date":invoice_date, "dueDate":dueDate}
    template = get_template('invoice.html')
    html = template.render(data)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    
    if not pdf.err:
        response = HttpResponse(result.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'
        return response
    return HttpResponse('Error creating PDF')

@login_required
def view_invoices(request, pk):
    invoice_data=Invoice.objects.get(id=pk)
    invoice_dict={}
    invoice_date = str(date.today().year) +"-"+str(date.today().month)+"-"+str(date.today().day)
    due_date = date.today()+timedelta(days=14)
    dueDate = str(due_date.year)+"-"+str(due_date.month)+"-"+str(due_date.day)
    amount = list(invoice_data.amounts.values())
    subtotal = sum(int(x) for x in amount)
    invoice_dict['total'] = subtotal
    invoice_dict['invoice_id'] = invoice_data.id
    tax = (21 if invoice_data.vat else 0)
    tax_amount = round((subtotal*tax)/100)
    finalamount = round((subtotal + tax_amount))
    services = list(invoice_data.services.values())
    amounts = list(invoice_data.amounts.values())     
    dictionary = dict(zip(services, amounts))
    return render(request, 'invoice.html', {"data":invoice_data, "subtotal":subtotal, "tax":tax, "tax_amount":tax_amount, "finalamount":finalamount, "values": dictionary, "invoice_date":invoice_date, "dueDate":dueDate})

@login_required
def update_invoice(request, pk):
    invoice_data=Invoice.objects.get(id=pk)
    artist = Artist.objects.all()
    partner = Partner.objects.all()
    if request.method == 'POST':
        serviceData=json.loads(request.POST['values'])
        services_dict = {}
        amounts_dict = {}

        def get_index(key):
            return int(key.replace("servicesname", "").replace("amount", ""))

        for data in serviceData:
            key = data["name"]
            value = data["value"]

            if "servicesname" in key:
                index = get_index(key)

                services_dict[index] = value
            elif "amount" in key:
                index = get_index(key)

                amounts_dict[index] = value

        services_list = dict(sorted(services_dict.items()))
        amounts_dict = dict(sorted(amounts_dict.items()))
        invoice_name=request.POST['invoice_name']
        duedate=request.POST['duedate']
        partnername=Partner.objects.get(id = request.POST['partnername'])
        artistname =Artist.objects.get(id = request.POST['artistname'])
        paid = request.POST.get('paid', False)
        if paid == 'on':
            paid=True
            
        vat = request.POST.get('vat', False)
        if vat == 'on':
            vat=True
        invoice_data.invoice_name = invoice_name
        invoice_data.duedate = duedate
        invoice_data.partnername = partnername
        invoice_data.artistname = artistname
        invoice_data.services = services_list
        invoice_data.amounts = amounts_dict
        invoice_data.paid = paid
        invoice_data.vat = vat
        invoice_data.save()
        return redirect('profiles:invoice')
    return render(request, 'update_invoice.html', {"data":invoice_data, "artists": artist, "partners":partner,})

@login_required
def delete_invoice(request, invoice_id):
    if request.method == 'DELETE':
        invoice = get_object_or_404(Invoice, id=invoice_id)
        invoice.delete()
        return JsonResponse({'message': 'Invoice deleted successfully.'}, status=200)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)

@login_required
def update_status(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            is_paid = data.get("is_paid")
            if is_paid is not None:
                is_paid = is_paid.lower() == "true"
                invoice.paid = is_paid
                invoice.save()
                return JsonResponse({"message": "Status updated successfully."}, status=200)
            else:
                return JsonResponse({"error": "Invalid 'is_paid' value in the request."}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data in the request."}, status=400)
    return JsonResponse({"error": "Invalid request method."}, status=400)
