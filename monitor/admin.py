from django.contrib import admin

from .models import OperationLogger, TemperatureLogger, FlowmeterLogger, SingleSwitchLogger

# Register your models here.
admin.site.register(OperationLogger)
admin.site.register(TemperatureLogger)
admin.site.register(FlowmeterLogger)
admin.site.register(SingleSwitchLogger)
