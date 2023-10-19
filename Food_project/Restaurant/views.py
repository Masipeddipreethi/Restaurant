from django.shortcuts import render

# Create your views here.
def first_page(request):
    return render(request,"recipe.html")
def second_page(request):
    return render(request,"lists.html")
def third_page(request):
    return render(request,"types.html")
def fourth_page(request):
    return render(request,"contact.html")
def fifth_page(request):
    return render(request,"address.html")