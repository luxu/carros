from django.contrib import admin

from core.models import Car, Manufacturer, State, City


class CarAdmin(admin.ModelAdmin):
    ...


admin.site.register(Car, CarAdmin)


class ManufacturerAdmin(admin.ModelAdmin):
    ...


admin.site.register(Manufacturer, ManufacturerAdmin)


class StateAdmin(admin.ModelAdmin):
    ...


admin.site.register(State, StateAdmin)


class CityAdmin(admin.ModelAdmin):
    ...


admin.site.register(City, CityAdmin)
