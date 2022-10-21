from dataclasses import field
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .resources import PartnerResource
from tablib import Dataset
from .models import Partner, Workplan
from django.contrib import messages
from .forms import PartnerForm
# Create your views here.

def home(request):
    return render(request,'home.html',{})


def export(request):
    person_resource = PartnerResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xlsx"'
    return response

def upload_partners(request):
    person_form = PartnerResource()
    if request.method == 'POST':
        person_resource = PartnerResource()
        dataset = Dataset()
        
        if  dataset:
            new_persons = request.FILES['myfile']
            print(new_persons.name)
            if not new_persons.name.endswith('xlsx'):
                return  messages.info(request,'wrong Format, kindly Check again')

            else:
                imported_data = dataset.load(new_persons.read(),format='xlsx')
                #print(imported_data)
                for data in imported_data:
                    value = Partner(data[0],data[1],data[2],data[3],data[4],data[5])
                    value.save() 
               
        else:
            return redirect('partners-list')
        
        
        
    
        person_resource = PartnerResource()
        # result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        # if not result.has_errors():
        #    person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'partners/upload_partners.html')


    # partners list

def partners_list(request):
    all_partners=Partner.objects.all()
    return render(request,'partners/partner_list.html',{'all_partners':all_partners})

# add partner
def add_partner(request):
    form=PartnerForm()
    if request.method=='POST':
        form=PartnerForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request,'wrong Format, kindly Check again')
            return redirect('partners-list')
    else:
        form=PartnerForm()
    
    return render(request,'partners/add_partner.html',{'form':form})

def workplan_list(request):
    all_workplan=Workplan.objects.all()
    return render(request,'workplan/list_workplan.html',{'all_workplan':all_workplan})





