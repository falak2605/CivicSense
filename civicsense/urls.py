from django.contrib import admin
from django.urls import path
from issues.views import index, list_issues, create_issue, upvote_issue, update_status

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('api/issues/', list_issues, name='list_issues'),          # GET
    path('api/issues/create/', create_issue, name='create_issue'), # POST
    path('api/issues/<int:issue_id>/upvote/', upvote_issue, name='upvote_issue'), # POST
    path('api/issues/<int:issue_id>/status/', update_status, name='update_status'), # POST
]
