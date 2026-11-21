# Example 3 — A non-owner application role

## Before

```text
DATABASE_URL=postgres://postgres:secret@db.internal:5432/app
-- The application connects as the superuser/owner. RLS is enabled on every
-- table and bypassed on every query; the policies are decoration.
```

## After

```sql
-- A dedicated role that owns nothing and cannot bypass RLS:
CREATE ROLE app_user LOGIN PASSWORD 'set-via-secret-manager' NOBYPASSRLS;
GRANT CONNECT ON DATABASE app TO app_user;
GRANT USAGE ON SCHEMA public TO app_user;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO app_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public
  GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO app_user;
```

```text
DATABASE_URL=postgres://app_user:secret@db.internal:5432/app
-- Migrations still run as the owner; request traffic never does (gate G-DB-053
-- asserts rolbypassrls = false and zero owned tables for this role).
```

Corrects DB-104 (the application connects as a non-owner role without BYPASSRLS; owner connections never serve request traffic).
