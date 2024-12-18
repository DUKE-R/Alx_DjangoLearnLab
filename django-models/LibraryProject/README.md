# LibraryProject

# Permissions Setup
- `can_view`: Allows the user to view the book.
- `can_create`: Allows the user to create new books.
- `can_edit`: Allows the user to edit book details.
- `can_delete`: Allows the user to delete books.

# Groups Setup
- Editors: Can create and edit books.
- Viewers: Can view books.
- Admins: Can view, create, edit, and delete books.

# Security Best Practices in Django

## Settings
- `DEBUG`: Disabled in production.
- `SECURE_BROWSER_XSS_FILTER`, `X_FRAME_OPTIONS`, `SECURE_CONTENT_TYPE_NOSNIFF`: Configured for browser-side protections.
- `CSRF_COOKIE_SECURE`, `SESSION_COOKIE_SECURE`: Ensure cookies are transmitted over HTTPS.

## CSRF Protection
- CSRF tokens are added to all forms using `{% csrf_token %}`.

## Secure Queries
- Replaced raw SQL queries with Django ORM parameterized queries.
- Validated user input using Django forms.

## Content Security Policy (CSP)
- Implemented using `django-csp` middleware with restrictive defaults.
