from django.shortcuts import render, redirect
from .models import Listings
from .forms import ListingForm
# Create your views here.

# CRUD --CREATE, RETRIEVE, UPDATE, DELETE, LIST

        #  list
def Listing_list(request):
    listings = Listings.objects.all()
    context ={"listings": listings}
    return render(request, "listings.html", context)

    # Retrieve
def Listing_retrieve(request, pk):
    listing = Listings.objects.get(id=pk)
    context = {"listing": listing}

    return render(request, "listing.html", context)



      # create



def Listing_create(request):
    form = ListingForm()
    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {
        "form": form
    }

    return render(request, "listing_create.html", context)




                #  UPDATE

def Listing_update(request, pk):
    listing = Listings.objects.get(id=pk)
    form = ListingForm(instance= listing)
    if request.method == "POST":
        form = ListingForm(request.POST, instance= listing, files= request.FILES)
        # print(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {
        "form": form
    }

    return render(request, "listing_uptade.html", context)





def Listing_delete(request, pk):
    listing = Listings.objects.get(id=pk)
    listing.delete()
    return redirect("/")










    

    


