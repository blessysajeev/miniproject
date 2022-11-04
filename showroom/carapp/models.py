from django.db import models 
# from django.contrib.auth.models import AbstractUser



# Create your models here.
class Vehicles(models.Model):
    name=models.CharField(max_length=250,unique=True)
    #slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2,default=True)
    # category=models.ForeignKey(Category,on_delete=models.CASCADE)
    # subcategory=models.ForeignKey(Subcategory,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='product',blank=True)
    #stock=models.CharField(max_length=250,default="null")
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('name',)
        verbose_name='Vehicle'
        verbose_name_plural='Vehicles'

    def _str_(self):
        return '{}'.format(self.name)




    
# class CustomUser(AbstractUser):
