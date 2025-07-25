# Permissions and Groups Setup in `bookshelf`

## Model-Level Permissions (`Book` model)

Defined in `models.py > Book.Meta.permissions`:
- `can_view`: View book entries.
- `can_create`: Create new book entries.
- `can_edit`: Edit existing book entries.
- `can_delete`: Delete book entries.

## Groups and Roles

Created via Django Admin:
- **Viewers**: `can_view`
- **Editors**: `can_view`, `can_create`, `can_edit`
- **Admins**: All permissions

## View-Level Enforcement

Each sensitive view is protected using `@permission_required`:
- `/books/` → requires `can_view`
- `/books/create/` → requires `can_create`
- `/books/edit/<pk>/` → requires `can_edit`
- `/books/delete/<pk>/` → requires `can_delete`

## Usage Instructions

1. Create users via admin.
2. Assign them to one of the groups.
3. Log in as those users and attempt actions.
4. Permissions are enforced strictly with `raise_exception=True`.

# Django Security Enhancements

## 🔐 Security Settings in settings.py

- `DEBUG = False`: Hides debug data in production.
- `SECURE_BROWSER_XSS_FILTER`: Enables browser XSS protection.
- `SECURE_CONTENT_TYPE_NOSNIFF`: Prevents MIME-type sniffing.
- `X_FRAME_OPTIONS = 'DENY'`: Protects against clickjacking.
- `CSRF_COOKIE_SECURE`: Forces CSRF cookie over HTTPS.
- `SESSION_COOKIE_SECURE`: Forces session cookie over HTTPS.

## 🛡️ View Security

- All form views include `{% csrf_token %}` to prevent CSRF.
- ORM used for all data access — SQL injection is prevented.
- User input validated via Django forms.

## 🧱 Content Security Policy

Enabled using `django-csp`, limits which domains can load JS, CSS, images, etc., to prevent XSS.

## ✅ Manual Security Testing Steps

- Attempt form submission without CSRF token — should be rejected.
- Try injecting scripts in search — should be safely escaped.
- Use browser dev tools to test for blocked inline scripts (CSP enforcement).
- Test cookie security in browser → Cookies should be marked `Secure` and `HttpOnly`.
