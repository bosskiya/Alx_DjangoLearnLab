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