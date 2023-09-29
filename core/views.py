from django.shortcuts import HttpResponse
from django.shortcuts import render , redirect
from core.froms import *
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils import timezone

from core.models import *
                          


                          
# Create your views here.



def home(request):
        products = Product.objects.all().order_by('created_at')[:4]
        categories = Category.objects.all()
        categories_count = Category.objects.all().count()
        testimonials = Testimonial.objects.all()

        context = {
            "name": "django",
            "title": "Home Page",
            "products": products,
            'categories': categories,
            'categories_count': categories_count,
            'testimonials': testimonials
        }
        return render(request, "index.html", context)





def contact(request):
    contact_model = ContactUsForm()
    if request.method == 'POST':
        contact_model = ContactUsForm(request.POST)
        if contact_model.is_valid():
            contact_model.save()
            contact_model = ContactUsForm()

    context = {
        'contactus_form' : contact_model,
    }
    return render(request, 'contact.html', context)

def products(request):

    context = {
        "title" : "Products Page",
        "products" : Product.objects.all().order_by('created_at'),
    }
    return render(request, "shop.html", context)



def product_detail(request, slug  ):
    context = {
        "title" : "Product Detail  Page",
        "product" : Product.objects.get(slug=slug),
    }
    return render(request, "product_detail.html", context)






class ProductListView(ListView):
    model = Product
    template_name = 'shop.html'
    context_object_name = 'products'
    ordering = ['-created_at']
    paginate_by = 1  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Products Page'
        context['categories'] = Category.objects.all()
        context['categories_count'] = Category.objects.all().count()
        context['testimonials'] = Testimonial.objects.all()
        return context


          






    
def search_view(request):
    search_input = request.GET.get('products')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    category_id = request.GET.get('category')
    
    if end_date == '':
        end_date = timezone.now().date()
    print('1', Product.objects.first().created_at)
    if category_id:
        all_products = Product.objects.filter(category=category_id)
    if search_input and start_date:
        all_products = Product.objects.filter(title__icontains=search_input , created_at__range=[start_date, end_date], category=category_id)
    if search_input and category_id:
        all_products = Product.objects.filter(title__icontains=search_input , category=category_id)
    if start_date and category_id:
        all_products = Product.objects.filter(created_at__range=[start_date, end_date], category=category_id)
        print('4' , all_products)
    elif search_input:
        all_products = Product.objects.filter(title__icontains=search_input)
        print('2' , all_products)
    elif start_date:
        all_products = Product.objects.filter(created_at__range=[start_date, end_date])
        print('3' , all_products)
        print('start_date , start_date' , start_date , end_date)
    else:
        all_products = Product.objects.all()
    
    context = {
        "title" : 'Products Page',
        'start_date' : start_date,
        'end_date' : end_date,
        'search_input' : search_input,
        'categories': Category.objects.all(is_active=True),
        'all_proroducts': all_products,
        'products_count': all_products.count(),
        "empty_message": "No Products Found"
    }
    return render(request, "shop.html", context)




def search(request):
    print("request get: ", request.GET)
    query = request.GET.get('query')

    if query:
        products = Product.objects.filter(title__icontains=query)

        context = {
            'title': 'Search',
            'query': query,
            'products': products,
       
        }
        return render(request, 'search.html', context)
    else:
        return HttpResponseRedirect(reverse('home'))
    
