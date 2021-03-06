from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import *
from .forms import AntibodyForm, AntibodyArcForm, AntibodyIndForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required

#main database/home view
@login_required(login_url="login")
def database(request):
    antibody = Antibody.objects.all().order_by('name')
    antibodyI = []
    #query associated entries in AntibodyInd databses to list the status of amount remaining
    for i in antibody:
        cat = i.cat_num
        ind_cat = AntibodyInd.objects.filter(cat_num=cat)
        amount_total=0
        staus = "None"
        for u in ind_cat:
            amount= int(u.amount_remaining)
            amount_total += amount
        if amount_total==0:
            status = "None"
        elif amount_total <=10:
            status = "Low"
        elif amount_total>10:
            status = "OK"
        antibodyI.append(status)
    #add AntibodyInd status to list of attributes from main database
    antibody1 = zip(antibody,antibodyI)
    context = {'antibody': antibody, 'antibodyI':antibodyI, 'antibody1':antibody1}
    return render(request,'abdb/database.html', context)

#query attributes from main database of specifc entries
@login_required(login_url="login")
def antibody(request, pk):
    antibody1 = Antibody.objects.get(id=pk)
    cat = antibody1.cat_num
    #calculate total amount remaing (from AntibodyInd entries) and output on template
    antibody3 = AntibodyInd.objects.filter(cat_num=cat)
    amount_total=0
    for i in antibody3:
        amount = int(i.amount_remaining)
        amount_total += amount
    context = {'antibody1':antibody1,'cat':cat,'antibody3':antibody3, "amount_total":amount_total}
    return render(request,'abdb/antibody.html', context)

#query associated antibodyInd entries for specifc Antibody selected
@login_required(login_url="login")
def antibodyInd(request, pk):
    antibody2 = AntibodyInd.objects.get(id=pk)
    context = {'antibody2':antibody2}
    return render(request,'abdb/antibody.html', context)

#add entry to main database (form)
@login_required(login_url="login")
def addEntry(request):
    form = AntibodyForm()
    if request.method == "POST":
        form= AntibodyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add2")
    context = {'form':form}
    return render(request, 'abdb/antibody_form.html', context)

#add entry to AntibodyInd database based on main database entry selected (queries catalog number of Antibody entry)
#for adding AntibodyInd to new Antibody entry
@login_required(login_url="login")
def addEntry2(request):
    cat = Antibody.objects.all().last()
    formInd = AntibodyIndForm(request.POST)
    if request.method == "POST":
        formInd= AntibodyIndForm(request.POST)
        if formInd.is_valid():
            object = formInd.save()
            object.cat_num = cat
            object.save()
            return redirect("database")
    context = {"formInd":formInd}
    return render(request, 'abdb/antibodyInd_form.html', context)

#add entry to AntibodyInd database based on main database entry selected (queries catalog number of Antibody entry)
#for adding AntibodyInd to already existing Antibody entry
@login_required(login_url="login")
def addEntry3(request, pk):
    cat = Antibody.objects.get(id=pk)
    formInd = AntibodyIndForm(request.POST)
    if request.method == "POST":
        formInd= AntibodyIndForm(request.POST)
        if formInd.is_valid():
            object = formInd.save()
            object.cat_num = cat
            object.save()
            return redirect("antibody", cat.id)
    context = {"formInd":formInd}
    return render(request, 'abdb/antibodyInd_form.html', context)

#update entry in main Antibody databse, autofills all fields with abilty to change
@login_required(login_url="login")
def updateEntry(request, pk):
    antibody2 = Antibody.objects.get(id=pk)
    form = AntibodyForm(instance=antibody2)
    if request.method == "POST":
        form= AntibodyForm(request.POST, instance=antibody2)
        if form.is_valid():
            form.save()
            return redirect("database")
    context = {'form':form}
    return render(request, 'abdb/antibody_form.html', context)

#update entry in main Antibody databse, autofills all fields with abilty to change
@login_required(login_url="login")
def updateEntry2(request, pk):
    antibody2 = Antibody.objects.get(id=pk)
    form = AntibodyForm(instance=antibody2)
    if request.method == "POST":
        form= AntibodyForm(request.POST, instance=antibody2)
        if form.is_valid():
            form.save()
            return redirect("antibody", antibody2.id)
    context = {'form':form}
    return render(request, 'abdb/antibody_form.html', context)

#update entry in AntibodyInd databse, autofills all fields with abilty to change
@login_required(login_url="login")
def updateEntry3(request, pk):
    antibody = AntibodyInd.objects.get(id=pk)
    cat = antibody.cat_num
    antibodyP = Antibody.objects.get(cat_num=cat)
    antibody3 = AntibodyInd.objects.get(id=pk)
    formInd = AntibodyIndForm(instance=antibody3)
    if request.method == "POST":
        formInd= AntibodyIndForm(request.POST, instance=antibody3)
        if formInd.is_valid():
            formInd.save()
            return redirect("antibody",antibodyP.id)
    context = {'formInd':formInd}
    return render(request, 'abdb/antibodyInd_form.html', context)

#update entry of Archived Antibody, autofills all fields with abilty to change
@login_required(login_url="login")
def updateEntryArc(request, pk):
    antibody2 = AntibodyArc.objects.get(id=pk)
    form = AntibodyArcForm(instance=antibody2)
    if request.method == "POST":
        form= AntibodyArcForm(request.POST, instance=antibody2)
        if form.is_valid():
            form.save()
            return redirect("antibody_archive", antibody2.id)
    context = {'form':form}
    return render(request, 'abdb/antibody_form.html', context)

#search funtion, can query name, company, host and catalog number
#returns results from main database and archives
@login_required(login_url="login")
def search(request):
    if request.method =="POST":
        searched = request.POST["searched"]
        antibody3 = Antibody.objects.filter(Q(host__contains=searched) | Q(name__contains=searched) | Q(company__contains=searched) | Q(cat_num__contains=searched))
        antibody4 = AntibodyArc.objects.filter(Q(host__contains=searched) | Q(name__contains=searched) | Q(company__contains=searched) | Q(cat_num__contains=searched))
        #returns number of results in both databases
        returns= len(antibody3)+len(antibody4)
        context = {"searched": searched,"antibody3":antibody3,"antibody4":antibody4, "returns":returns}
        return render (request,'abdb/search.html', context)
    #if nothing searhced
    else:
        return render (request,'abdb/search.html')

#Archives database, returns a table with all archives
@login_required(login_url="login")
def archives(request):
    antibody = AntibodyArc.objects.all().order_by("name")
    context = {'antibody': antibody}
    return render(request,'abdb/archives.html', context)

#query attributes from archives database of specifc entries
@login_required(login_url="login")
def antibodyArc(request, pk):
    antibody1 = AntibodyArc.objects.get(id=pk)
    context = {'antibody1':antibody1}
    return render(request,'abdb/antibody_archive.html', context)
    
#move antibody in main database to archives database
@login_required(login_url="login")
def archive(request, pk):
    antibody4 = Antibody.objects.get(id=pk)
    cat = antibody4.cat_num
    antibody3 = AntibodyInd.objects.filter(cat_num=cat)
    form = AntibodyArcForm(instance=antibody4)
    if request.method == "POST":
        form= AntibodyArcForm(request.POST)
        if form.is_valid():
            form.save()
            antibody4.delete()
            antibody3.delete()
        return redirect("archives")
    context = {'form':form, "antibody4":antibody4}
    return render(request, 'abdb/antibody_form.html', context)

#move antibody in archives database back to main database
@login_required(login_url="login")
def restore(request, pk):
    antibody4 = AntibodyArc.objects.get(id=pk)
    form = AntibodyForm(instance=antibody4)
    if request.method == "POST":
        form= AntibodyForm(request.POST)
        if form.is_valid():
            form.save()
            antibody4.delete()
            return redirect("add2")
    context = {'form':form, "antibody4":antibody4}
    return render(request, 'abdb/antibody_form.html', context)

#remove an entry from the archives databse
@login_required(login_url="login")
def removeEntry(request, pk):
    antibody2 = AntibodyArc.objects.get(id=pk)
    if request.method == "POST":
        antibody2.delete()
        return redirect("archives")
    context = {"antibody2": antibody2}
    return render(request,'abdb/remove.html', context)

#remove an AntibodyInd entry
@login_required(login_url="login")
def removeEntryInd(request, pk):
    antibodyI = AntibodyInd.objects.get(id=pk)
    cat = antibodyI.cat_num
    antibodyP = Antibody.objects.get(cat_num=cat)
    if request.method == "POST":
        antibodyI.delete()
        return redirect("antibody", antibodyP.id)
    context = {"antibodyI": antibodyI,"antibodyP":antibodyP}
    return render(request,'abdb/removeIND.html', context)

#login page
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('database')
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password )
            if user is not None:
                login(request, user)
                return redirect("database")
            else:
                messages.info(request, "username OR password incorrect")
        return render (request, 'abdb/login.html')

#logout path
def logoutUser(request):
    logout(request)
    return redirect('login')
