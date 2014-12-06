from django.contrib import admin

from . import models


admin.site.register(models.Member)
admin.site.register(models.Organization)
admin.site.register(models.SalesChannel)
admin.site.register(models.Carrier)
admin.site.register(models.Plan)
admin.site.register(models.Level)
admin.site.register(models.PlanType)
admin.site.register(models.PlanMetaInfo)