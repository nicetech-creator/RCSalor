from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'RCSalor/index.html', {})

def business_detail(request):
    """ Controller for business single detail page """
    return render(request, 'RCSalor/business-single-page.html', {})
