from django.shortcuts import render,redirect
from .models import Product,ProdBookingDetails
from .forms import BookingForm
from django.views.generic import ListView,DetailView
from django.contrib import messages
# Create your views here.



class Home(ListView):
    model=Product
    template_name='app/home.html' 
    context_object_name='item1'

class ProdDetailView(DetailView):
    model=Product
    template_name='app/detail.html'
    context_object_name='item1'

def NewBooking(req,pk):
    context={}
    if req.method=="POST":
        start_date = req.POST.get('bookdate')
        end_date = req.POST.get('booking_end')
        product1=req.POST.get('product')
        product2=Product.objects.get(id=int(product1))
        conflicting_rentals_samedate=ProdBookingDetails.objects.filter(
            product=product2,
            bookdate=start_date,
            booking_end=end_date,
        )
        conflicting_rentals_samestartdate=ProdBookingDetails.objects.filter(
            product=product2,
            bookdate=start_date,
        )
        conflicting_rentals_sameenddate=ProdBookingDetails.objects.filter(
            product=product2,
            booking_end=end_date,
        )
        print(conflicting_rentals_samedate,conflicting_rentals_samestartdate,conflicting_rentals_sameenddate)
        if conflicting_rentals_samedate.exists() or conflicting_rentals_samestartdate.exists() or conflicting_rentals_sameenddate.exists():
            context['message']="Car already booked in dates"
        else :
            form=BookingForm(req.POST)
            if form.is_valid():
                i1=form.save()
                i1.save()
                return redirect("app:home") 
    obj=Product.objects.filter(id=pk)
    objbookdetails=ProdBookingDetails.objects.filter(product__id=pk)
    context['form']=BookingForm()
        

    return render(req,"app/booking.html",context)