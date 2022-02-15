from django.contrib import admin
from .models import User,ServiceDetails,ClothDetails,PriceDetails,AccountDetails,PlantDetails
# Register your models here.
admin.site.register(User)
admin.site.register(ServiceDetails)
admin.site.register(ClothDetails)
admin.site.register(PriceDetails)
admin.site.register(AccountDetails)
admin.site.register(PlantDetails)