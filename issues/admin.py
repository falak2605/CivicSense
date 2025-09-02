from django.contrib import admin
from .models import Issue

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('id','title','category','status','upvotes','created_at')
    list_filter = ('category','status')
    search_fields = ('title','description')
