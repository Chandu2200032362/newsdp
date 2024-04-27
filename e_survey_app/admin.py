from django.contrib import admin
from .models import User,Feedback,Address
admin.site.register(User)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'feedback')
    list_filter = ('created_at',)

admin.site.register(Feedback, FeedbackAdmin)



class AddressAdmin(admin.ModelAdmin):
    list_display = ('street', 'city', 'state', 'zipcode')
    search_fields = ['street', 'city', 'state', 'zipcode']
    list_filter = ['city', 'state', 'zipcode']

admin.site.register(Address, AddressAdmin)