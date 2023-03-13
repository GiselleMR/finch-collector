from django.shortcuts import render


finches = [
    {'name': 'Chick', 'species': 'Evening Grosbeack', 'description': 'yellow finch with black and white wings', 'age': 3},
  {'name': 'Twitter', 'species': 'Pine Grosbeak', 'description': 'red finsc with grey wings', 'age': 2},
]
# Create your views here.

def home (request):
    return render(request, 'home.html') 

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })