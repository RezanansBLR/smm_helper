from django.shortcuts import redirect, render
from .forms import Search
from .models import Bloger

def index_page(request):
    if request.method == 'POST':
        form = Search(request.POST)
        if form.is_valid():
            try:
                bloger = Bloger.objects.get(url_inst=form.cleaned_data['url'])
                if bloger.url_inst == form.cleaned_data['url']:
                    return redirect('bloger', slug=bloger)
                else:
                    
            except:
                print('Error')
            
    else:
        form = Search()
    return render(request, "index.html", context={'form': form})

def bloger_page(request, slug):
    bloger = Bloger.objects.get(slug=slug)
    return render(request, "bloger.html", context={'bloger':bloger})