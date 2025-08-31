from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.forms.models import model_to_dict
import json

from .models import Issue
from .ai_utils import categorize

@ensure_csrf_cookie
def index(request):
    return render(request, 'index.html')

@require_GET
def list_issues(request):
    issues = Issue.objects.order_by('-created_at').values('id','title','description','category','status','upvotes','created_at','location_lat','location_lng')
    return JsonResponse(list(issues), safe=False)

@require_POST
def create_issue(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
    except Exception:
        return HttpResponseBadRequest('Invalid JSON')

    title = data.get('title','').strip()
    description = data.get('description','').strip()
    category = data.get('category','').strip() or None
    status = 'Pending'
    lat = data.get('location_lat')
    lng = data.get('location_lng')

    if not title or not description:
        return HttpResponseBadRequest('Title and description are required')

    # Auto-categorize if not provided
    if not category or category == 'other':
        category = categorize(description)

    issue = Issue.objects.create(
        title=title,
        description=description,
        category=category,
        status=status,
        location_lat=lat,
        location_lng=lng
    )
    return JsonResponse(model_to_dict(issue))

@require_POST
def upvote_issue(request, issue_id):
    issue = get_object_or_404(Issue, pk=issue_id)
    issue.upvotes += 1
    issue.save(update_fields=['upvotes'])
    return JsonResponse({'id': issue.id, 'upvotes': issue.upvotes})

@require_POST
def update_status(request, issue_id):
    issue = get_object_or_404(Issue, pk=issue_id)
    try:
        data = json.loads(request.body.decode('utf-8'))
        new_status = data.get('status')
    except Exception:
        return HttpResponseBadRequest('Invalid JSON')
    if new_status not in ['Pending','In Progress','Resolved']:
        return HttpResponseBadRequest('Invalid status')
    issue.status = new_status
    issue.save(update_fields=['status'])
    return JsonResponse({'id': issue.id, 'status': issue.status})
