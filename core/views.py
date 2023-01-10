from django.shortcuts import render, redirect
from .models import Institution, Store, Cart, Category, Product, User
from .forms import InstitutionCreationForm, StoreCreationForm, ProductCreationForm
from django.contrib import messages
import random
import string

# Create your views here.


def landing_page(request):
    return render(request, 'landing_page.html')


def partnership(request):
    institution = Institution.objects.all()
    return render(request, 'core/partnership.html', {"institution": institution})


def institution(request, name):
    institute = Institution.objects.get(name=name)

    store_list = []

    store = Store.objects.all()
    for i in store:
        if i.institution.uuid == institute.uuid:
            store_list.append(i)

    return render(request, 'core/institution-detail.html', {"institute": institute, "store": store_list})


def create_partnership(request):
    form = InstitutionCreationForm()
    if request.method == "POST":
        form = InstitutionCreationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            manager = form.cleaned_data['institution_manager']

            new_institution = Institution.objects.create(name=name, address=address, institution_manager=manager)
            new_institution.save()

            messages.success(request, "Partnership Achieved Successfully")
            return redirect('core:partner')
        else:
            messages.info(request, "Error in field inputation")

    return render(request, "core/create-partnership.html", {"form": form})


def stores(request):
    stores = Store.objects.all()
    return render(request, "core/stores.html", {"stores": stores})


def create_store(request, name):
    institution_name = name

    form = StoreCreationForm()
    if request.method == "POST":
        form = StoreCreationForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            owner = form.cleaned_data['owner']
            cover_art = form.cleaned_data['cover_art']

            if Store.objects.filter(name=name).exists():
                messages.success(request, "A store with this name already exists")

            elif Store.objects.filter(owner=owner).exists():
                messages.success(request, "A trader can't have more than one store")

            elif Institution.objects.filter(name=institution_name).exists():
                institute = Institution.objects.get(name=institution_name)
                    
                new_store = Store.objects.create(name=name, institution=institute, owner=owner, description=description, cover_art=cover_art, verified=True)
                new_store.save()

                messages.success(request, "Store Created and Verified Successfully")
                return redirect('core:institution', institute.name)
            else:
                messages.error(request, "No Institution of such exists")
                return redirect('core:partner')

        else:
            messages.info(request, "Error in field inputation")

    return render(request, "core/create-store.html", {"form": form})


def store_detail(request, name):
    store = Store.objects.get(name=name)
    return render(request, "core/store-detail.html", {"store": store})


def create_product(request, store_name):
    store = Store.objects.get(name=store_name)

    form = ProductCreationForm()

    if request.method == "POST":
        form = ProductCreationForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data["product_name"]
            price = form.cleaned_data["product_price"]
            category = form.cleaned_data["product_category"]
            quantity = form.cleaned_data["product_quantity"]
            description = form.cleaned_data["product_description"]

            # Creating a random id for product
            data_type = string.digits
            id_length = random.sample(data_type, 7)

            generated_id = "".join(id_length)


            new_product = Product.objects.create(store=store, product_name=name, product_id=generated_id,
                                                 product_price=price, product_category=category, 
                                                 product_quantity=quantity, product_description=description)
            new_product.save()



    return render(request, "core/create-product.html", {"form": form, "store": store})


def terminate_partnership(request, name):
    institute = Institution.objects.get(name=name)

    if request.GET.get("delete"):
        institute.delete()
        messages.success(request, f"Contract Terminated with {institute.name}")
        return redirect("core:partner")
    
    return render(request, "core/terminate-partnership.html", {"institute": institute})