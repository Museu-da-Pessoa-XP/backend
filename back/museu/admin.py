from django.contrib import admin

from .models import User
from .models import Historia
from .models import Upload



admin.site.register(User)
admin.site.register(Historia)
admin.site.register(Upload)



# Register your models here.
