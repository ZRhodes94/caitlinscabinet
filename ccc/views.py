from django.shortcuts import render

# Create your views here.
def main(request):
   return render(request, 'ccc/main.html')

def form(request):
   return render(request, 'ccc/form.html')

def about(request):
   return render(request, 'ccc/about.html')

def minis(request):
   return render(request, 'ccc/minis.html')

def crystals(request):
   return render(request, 'ccc/crystals.html')

def faq(request):
   return render(request, 'ccc/faq.html')

def dungeonbox(request):
   return render(request, 'ccc/dungeonbox.html')