from django.shortcuts import render
from subprocess import run
from pymongo import MongoClient

def scrape_property_view(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query')
        run(['python', 'scrap_property.py', search_query])

        # Connect to MongoDB and fetch the property details
        client = MongoClient("mongodb://localhost:27017/")
        db = client["Scrap_Data"]
        collection = db["99acres"]
        property_details = collection.find()

        return render(request, 'scrape_success.html', {'property_details': property_details})

    return render(request, 'scrape_form.html')