from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publish)
admin.site.register(AddBook)
admin.site.register(BookMark)
admin.site.register(Review)
admin.site.register(WriteReview)

