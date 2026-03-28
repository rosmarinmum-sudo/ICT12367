from django.shortcuts import render, redirect, get_object_or_404  
from django.http import HttpResponse
from myapp.models import Person

def index(request):
    all_Person = Person.objects.all()
    return render(request, "index.html", {"all_person": all_Person})

def about(request):
    return render(request, "about.html")

def form(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        age = request.POST.get("age", "").strip()

        if name and age.isdigit():
            Person.objects.create(name=name, age=int(age))
            return render(request, "form.html", {"success": True, "name": name})

        return render(request, "form.html", {"error": "กรุณากรอกข้อมูลให้ถูกต้อง เช่น ชื่อไม่ว่างและอายุเป็นตัวเลข"})

    return render(request, "form.html")



def edit_person(request, id):
    
    person = get_object_or_404(Person, pk=id)
    
    if request.method == "POST":
        
        person.name = request.POST.get("name", "").strip()
        person.age = request.POST.get("age", "").strip()
        person.save() 
        return redirect('index')
        
   
    return render(request, "edit.html", {"person": person})

def delete_person(request, id):
    
    person = get_object_or_404(Person, pk=id)
    person.delete() 
    return redirect('index') 