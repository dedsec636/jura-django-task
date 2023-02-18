from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

class Product(models.Model):
    product_name=models.CharField(max_length=255)
    product_desc=models.TextField(max_length=200,default=" ")
    price=models.DecimalField(max_digits=8,decimal_places=2)
    product_booked=models.BooleanField(default=False)
    

    def __str__(self) -> str:
        return self.product_name

class ProdBookingDetails(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    bookdate=models.DateField()
    booking_end=models.DateField()

    def clean(self):
        super().clean()

        conflicting_rentals = ProdBookingDetails.objects.filter(
            product=self.product,
            bookdate=self.bookdate,
            booking_end=self.booking_end,
        )

        if conflicting_rentals.exists():
            raise ValidationError('Car already booked during specified dates')



    def __str__(self) -> str:
        return self.product.product_name+" booking from "+self.bookdate.strftime('%Y-%m-%d')+ " to "+self.booking_end.strftime('%Y-%m-%d')