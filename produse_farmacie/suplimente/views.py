from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Medicamente
from .forms import MedicamenteForm
med = [
    {
        'id': 1,
        'nume':'VITAMINE',
        'otc': 'DA',
        'nr':'100'
    },
    {
        'id': 2,
        'nume':'PRADAXA',
        'otc':'NU',
        'nr':'0'
    },
    {
        'id': 3,
        'nume':'MAGNEZIU',
        'otc':'DA',
        'nr':'45'
    }
]
def home(request):
    # return HttpResponse('<h2> Aici vor fi medicamentele</h2>')
    medicamente = Medicamente.objects.all()
    form = MedicamenteForm()
    if request.method == 'POST':
        Medicamente.objects.create(medicament=request.POST.get('medicament'),comandat=request.POST.get('comandat') )
        return redirect('home')
    context = {'med': medicamente ,'form':form}
    return render(request,'suplimente/home.html',context)

def about(request):
    # return HttpResponse('<h2>About my app</h2>')
    return render (request,'suplimente/about.html')



