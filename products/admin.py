from django.contrib import admin
from .models import Review, Computers, Made, CategoryComputer, ComputerMade


# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    # list_display = ('id', 'username', 'first_name', 'date_joined')
    # list_filter = ['is_staff', 'is_superuser', 'first_name', 'last_name']
    pass


admin.site.register(Made, CustomUserAdmin)
admin.site.register(CategoryComputer, CustomUserAdmin)
admin.site.register(Computers, CustomUserAdmin)
admin.site.register(ComputerMade, CustomUserAdmin)
admin.site.register(Review, CustomUserAdmin)
