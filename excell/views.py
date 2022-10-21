from django.shortcuts import render
from django.http import HttpResponse
from .models import PartnerFile
from .forms import PartnerFileForm
from th_digitized.models import Partner
import csv
# Create your views here.
def upload_partners(request):
    forms=PartnerFileForm(request.POST or None, request.FILES )
    if forms.is_valid():
        forms.save()
        forms=PartnerFileForm()
        obj=PartnerFile.objects.get(activated=False)

        with open(obj.file_name.path,'r') as f:

            reader=csv.reader(f)
            for i,row in enumerate(reader):

                if i==0:
                    pass
                else:
                    print(row)
                    row="".join(row)
                    print(row)
                    row=row.replace(";"," ")
                    row=row.split()
                    print(row)
                    # Partner.objects.create(
                    #     name=row[1],
                    #     logo=row[2],
                    #     website=row[3],
                    #     bio=row[4],
                    #     headquater=row[5])
            obj.activated=True
            obj.save()




    return render(request,'upload_partners.html',{'forms':forms})

