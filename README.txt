CivicSense (Django + Frontend in one project)
=================================================

Quick start
-----------
1) Create a virtual environment and install requirements:
   python -m venv venv
   source venv/bin/activate   (Windows: venv\Scripts\activate)
   pip install -r requirements.txt

2) Run database migrations:
   python manage.py migrate

3) Start the server:
   python manage.py runserver

4) Open in your browser:
   http://127.0.0.1:8000/

What’s included
---------------
- Django backend with APIs:
    GET  /api/issues/                -> list issues
    POST /api/issues/create/         -> create issue (auto-categorized if category empty)
    POST /api/issues/<id>/upvote/    -> increment upvotes
    POST /api/issues/<id>/status/    -> update status (Pending/In Progress/Resolved)

- Frontend (HTML/CSS/JS) served by Django:
    /               -> index.html

- AI (rule-based):
    issues/ai_utils.py -> categorize(description) returns one of:
       road, garbage, water, electricity, other

Notes
-----
- This demo doesn’t include user authentication (kept simple for clarity).
- Image upload is omitted in MVP to avoid extra dependencies. Can be added later.
