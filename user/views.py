from django.http import HttpResponse
from django.shortcuts import render
from .models import Profile, Relationship
from .forms import ProfileForm
from django.shortcuts import render, get_object_or_404


# Create your views here.

def profile_view(request):
    # data = Profile.objects.get(profile=request.user)
    data = get_object_or_404(Profile, username=request.user)
    context = {'username': data.username, 'fullname': data.full_name}
    return render(request, 'profile.html', context)


def profile_view_by_id(request, id):
    data = get_object_or_404(Profile, id=id)
    # context = {'username': data.username, 'fullname': data.full_name}
    return HttpResponse(data.full_name+data.username, status=200)


def profile_edit(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('successfull!')
        else:
            content = {
                'errors': form.errors
            }
            return render(request, 'profile_edit.html', content)
    else:
        form = ProfileForm()
        return render(request, 'profile_edit.html', {'form': form})
