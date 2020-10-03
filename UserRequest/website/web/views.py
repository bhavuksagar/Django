from django.shortcuts import render,redirect
from .models import Video
from .forms import projectform
# Create your views here.
def index(request):
    vid=Video.objects.order_by('-date')
    context={'vid':vid}
    return render(request, 'index.html',context)

def vrform(request):
    if request.method == 'POST':
        form = projectform(request.POST)

        if form.is_valid():
            new_req = Video(title=request.POST['projectname'], text=request.POST['projectdesc'],
            name=request.POST['name'],email=request.POST['email'])
            new_req.save()
            return redirect('index')
    else:
        form = projectform()

    context={'form': form}


    return render(request, 'vrform.html',context)
