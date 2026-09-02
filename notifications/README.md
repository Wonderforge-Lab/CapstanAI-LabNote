# Notifications

Notifications record manual relay requests for the human operator.

Use a notification when a message needs to be carried between sessions that cannot see each other directly.

Create the file from `templates/notification_request.md`, put it in `notifications/open/`, and create the canonical JSON notification record under `registry/notifications/`.

CSV notification registries and `registry/INDEX.md` are generated, read-only compatibility views. Do not edit them manually.
