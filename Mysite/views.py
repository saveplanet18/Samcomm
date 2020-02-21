from django.shortcuts import render,get_object_or_404,HttpResponse
from .models import Emp
from .forms import Empform

def create(request):
    context={}
    form=Empform(request.POST,None)
    if form.is_valid():
        form.save()


    context['form']=form
    return render(request,'Mysite/create.html',context)
def Emp(request):
    context={}
    context['dataset']=Emp.objects.all()
    return render(request,'Mysite/list_view.html',context)

def detail(request,id):
    context={}
    context['dataset']=Emp.objects.get(id=id)
    return render((request,''))

def delete_view(request,id):
    context={}
    obj=get_object_or_404(Emp,id=id)
    if request.method=='POST':
        obj.delete()
        return HttpResponse('/')
    return render(request,'Mysite/delete_view.html',context)






