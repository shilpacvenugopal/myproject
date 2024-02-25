from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Table2, Table1
from .forms import Table2ImportForm
from .resources import Table2Resource

class Table2Admin(ImportExportModelAdmin):
    resource_class = Table2Resource
    form = Table2ImportForm

admin.site.register(Table2, Table2Admin)
admin.site.register(Table1)



#### Create the image upload model ###
from .models import ImageModel

class ImageModelAdmin(admin.ModelAdmin):
    list_display = ('display_image',)

    def display_image(self, obj):
        return '<img src="{}" style="max-height:100px; max-width:100px;" />'.format(obj.image.url)

    display_image.allow_tags = True
    display_image.short_description = 'Image'

admin.site.register(ImageModel, ImageModelAdmin)