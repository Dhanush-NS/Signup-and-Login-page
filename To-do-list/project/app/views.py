from django.shortcuts import render

# Create your views here.
def index(request):
   
    return render(request, 'index.html')

def add(request):
    val1 = int(request.POST['val1'])
    val2 = int(request.POST['val2'])
    res = val1 +val2
    # add1 = add(val1 = val1,val2 = val2, res = res)
    # add1.save()
    return render(request,'result.html',{'result':res})
    