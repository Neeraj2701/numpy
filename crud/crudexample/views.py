from django.shortcuts import render,redirect
from crudexample.models import employee
from crudexample.forms import empform


#READ DATA/GET
def show(request):
	emps=employee.objects.all()
	return render(request,'show.html',{'emps':emps})



#CREATE DATA/POST
def create(request):
	if request.method=='POST':
		form=empform(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/show')
	else:
		form=empform()
	return render(request,'index.html',{'form':form})


#EDIT
def edit(request,id):
	emp=employee.objects.get(id=id)
	return render(request,'edit.html',{'emp':emp})


#UPDATE

def upd(request,id):
	emp=employee.objects.get(id=id)
	form=empform(request.POST,instance=employee)
	if form.is_valid():
		form.save()
		return redirect('/show')
	return render(request,'edit.html',{'emp':emp})


#DELETE
def destroy(request,id):
	emp=employee.objects.get(id=id)
	emp.delete()
	return redirect('/show')







	


