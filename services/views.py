from django.shortcuts import render
from .models import ServiceProvider

def home(request):
    return render(request, 'home.html')

def provider_list(request):
    providers = ServiceProvider.objects.all()
    return render(request, 'provider_list.html', {'providers': providers})


from .forms import ServiceProviderForm
from .models import ServiceProvider
from django.contrib.auth.decorators import login_required

@login_required
def register_provider(request):
    if hasattr(request.user, 'serviceprovider'):
        return redirect('home')  # Already registered

    if request.method == 'POST':
        form = ServiceProviderForm(request.POST)
        if form.is_valid():
            provider = form.save(commit=False)
            provider.user = request.user
            provider.save()
            return redirect('home')
    else:
        form = ServiceProviderForm()
    return render(request, 'services/register_provider.html', {'form': form})


