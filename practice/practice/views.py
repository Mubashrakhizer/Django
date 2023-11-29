from django.shortcuts import render

def indexpage(request):
    return render(request, 'index.html')

def homepage(request):
    return render(request, 'home.html')  
def input(request):
    return render(request, 'input.html')
def viewdata(request):
    email= request.GET['email']
    pas= request.GET['pass']
    data={
        'email':email,
        'password':pas
        
    }
    return render(request, 'viewdata.html',data) 