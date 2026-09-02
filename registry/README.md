# Registry

Canonical records are JSON-per-record under this folder.

The CSV files and INDEX.md are generated compatibility views. Do not edit them manually; run scripts/generate_registry_views.py locally when canonical JSON changes, then commit the resulting views.

CI checks that committed views match the canonical JSON records.
