from django.shortcuts import render
import urllib.parse
import urllib.request
import ast
# Create your views here.
def venue_view(request):
    hku_id = request.GET.get('hku_id', None)
    diagoseDateString = request.GET.get('diagnose_date', None)
    print(hku_id)
    print(diagoseDateString)
    with urllib.request.urlopen('https://ancient-lake-43959.herokuapp.com/core/api/venues_visited?hku_id='+hku_id+"&diagnose_date="+diagoseDateString) as response:
        r = response.read()
        code=response.getcode()
    r=r.decode('utf-8')
    r=ast.literal_eval(r)
    template_name='venues.html'
    context={
        'subject':hku_id,
        'date': diagoseDateString,
        'venues':r
    }

    return render(request, template_name, context)

def contact_view(request):
    hku_id = request.GET.get('hku_id', None)
    diagoseDateString = request.GET.get('diagnose_date', None)
    print(hku_id)
    print(diagoseDateString)
    with urllib.request.urlopen('https://ancient-lake-43959.herokuapp.com/core/api/close_contacts?hku_id='+hku_id+"&diagnose_date="+diagoseDateString) as response:
        r = response.read()
        code=response.getcode()
    r=r.decode('utf-8')
    r=ast.literal_eval(r)
    template_name='contacts.html'
    context={
        'subject':hku_id,
        'date': diagoseDateString,
        'contacts':r
    }

    return render(request, template_name, context)


'''
http://127.0.0.1:8000/trace/venue?hku_id=3025704501&diagnose_date=2022-05-04
http://127.0.0.1:8000/core/api/venues_visited?hku_id=3025704501&diagnose_date=2022-05-04
http://127.0.0.1:8000/trace/contact?hku_id=3025704501&diagnose_date=2022-05-04

'''