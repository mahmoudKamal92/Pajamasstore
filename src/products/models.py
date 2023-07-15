from django.db import models
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey
from django.urls import reverse
from PIL import Image
from django.utils.translation import gettext as _ 


class category(MPTTModel):
    STATUS = (
        ('Active', 'Active'),
        ('Not Active', 'Not Active'),
    )
    parent = TreeForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.CASCADE)
    category_name = models.CharField(max_length=50, verbose_name=_("Category Name"))
    category_image = models.ImageField(blank=True, upload_to='Category Image/')
    category_description = models.TextField(max_length=255, null=True, blank=True, verbose_name=_("Description"))
    category_status=models.CharField(max_length=10, choices=STATUS, verbose_name=_("Status"))
    category_slug = models.SlugField(null=False, unique=True, verbose_name=_("Slug"))
    category_create_at=models.DateTimeField(auto_now_add=True)
    category_update_at=models.DateTimeField(auto_now=True)

    
    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")
     
    class MPTTMeta:
        order_insertion_by = ["category_name"]

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})
 



class product_image(models.Model):
    product=models.ForeignKey("Product",on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='Product images/')

    
    class Meta:
        verbose_name = _("product Image")
        verbose_name_plural = _("product Images")

    def __str__(self):
        return self.product

    def get_absolute_url(self):
        return reverse("product_Image_detail", kwargs={"pk": self.pk})


class product(models.Model):
    STATUS = (
        ('True', 'Available'),
        ('False', 'unavailable'),
    )

    VARIANTS = (
        ('None', 'None'),
        ('Size', 'Size'),
        ('Color', 'Color'),
        ('Size-Color', 'Size-Color'),

    )
    product_code = models.CharField(max_length=50,unique=True,verbose_name= _("Code"))
    product_category = models.ForeignKey(category, on_delete=models.CASCADE, verbose_name= _("Category"))
    product_name_english = models.CharField(max_length=150,verbose_name= _("Name English"))
    product_name_arabic = models.CharField(max_length=150,verbose_name= _("Name Arabic"))
    product_description_englih = models.TextField(max_length=255,verbose_name= _("Description EN"))
    product_description_arabic = models.TextField(max_length=255,verbose_name= _("Description AR"))
    product_cost = models.DecimalField(max_digits=5, decimal_places=2,verbose_name= _("Cost"))
    product_price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name= _("Price"))
    product_price_after_discount = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name=_("Price Ater Discount"))
    product_discount_start_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name=_("Discount Start Date"))
    product_discount_start_enddate = models.DateField(auto_now=False, auto_now_add=False, verbose_name=_("Discount End Date"))
    product_variant=models.CharField(max_length=10,choices=VARIANTS, default='None', verbose_name=_("Product Variant"))
    product_slug = models.SlugField(null=False, unique=True,verbose_name=_("Slug"))
    product_status= models.BooleanField(choices=STATUS, verbose_name=_("Product Status"))
    product_create_at=models.DateTimeField(auto_now_add=True)
    product_update_at=models.DateTimeField(auto_now=True)

    

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})





class color(models.Model):
    color_name = models.CharField(max_length=20, verbose_name=_("Color Name"))
    color_code = models.CharField(max_length=10,blank=True, null=True, verbose_name=_("Color Code"))

    

    class Meta:
        verbose_name = _("Color")
        verbose_name_plural = _("Colors")

    def __str__(self):
        return self.color_name

    def get_absolute_url(self):
        return reverse("Color_detail", kwargs={"pk": self.pk})




class size(models.Model):
    size_name = models.CharField(max_length=20, verbose_name=_("Color Name"))
    size_code = models.CharField(max_length=10,blank=True, null=True, verbose_name=_("Color Code"))
   

    class Meta:
        verbose_name = _("size")
        verbose_name_plural = _("sizes")

    def __str__(self):
        return self.size_name

    def get_absolute_url(self):
        return reverse("size_detail", kwargs={"pk": self.pk})

class variant(models.Model):
    variant_product = models.ForeignKey(product, on_delete=models.CASCADE, verbose_name=_("Product"))
    variant_color = models.ForeignKey(color, on_delete=models.CASCADE,blank=True,null=True, verbose_name=_("Color"))
    variant_size = models.ForeignKey(size, on_delete=models.CASCADE,blank=True,null=True, verbose_name=_("Size"))
    variant_quantity = models.IntegerField(default=1, verbose_name=_("Quantitiy"))
    variant_price = models.DecimalField(max_digits=12, decimal_places=2,default=0, verbose_name=_("Price"))

   
    class Meta:
        verbose_name = _("Variant")
        verbose_name_plural = _("Variants")

    def __str__(self):
        return self.variant_product

    def get_absolute_url(self):
        return reverse("Variants_detail", kwargs={"pk": self.pk})
