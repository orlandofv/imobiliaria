from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages #import messages

from .models import Settings
from .forms import SettingsForm


# Create your views here.
########################## Settings ##########################
@login_required
def settings_create_view(request):
    obj = Settings.objects.first()
    form = SettingsForm(request.POST or None, request.FILES or None, instance=obj)

    if request.method == 'POST':
       
        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_by = instance.modified_by = request.user
            instance.date_created = instance.date_modified = datetime.datetime.now()
            instance = instance.save()
            messages.success(request, _("Settings added successfully!"))

            if request.POST.get('save_settings'):
                return redirect('asset_app:home')
            else:
                return redirect('asset_app:settings_create')
        else:
            for error in form.errors.values():
                messages.error(request, error)
            return redirect('asset_app:settings_create')
    
    context = {'form': form}
    return render(request, 'asset_app/createviews/settings_create.html', context)


