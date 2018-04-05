
from django import forms
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from hotel.models import Hotel


class HotelModelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        exclude = ()
        widgets = {

        }


class HotelAdmin(ModelAdmin):
    """
    Hotel Admin
    """

    form = HotelModelForm


admin.site.register(Hotel, HotelAdmin)
