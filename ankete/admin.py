from django.contrib import admin
from .models import Inquiry, Question, Choice, Answer

# Register your models here.

admin.site.register(Inquiry) 
admin.site.register(Question) 
admin.site.register(Choice) 
admin.site.register(Answer)