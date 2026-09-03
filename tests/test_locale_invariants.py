#!/usr/bin/env python3
"""Check declared zh-CN counterparts and language-invariant protocol literals.

This is deliberately an invariant check, not an attempt to compare translated
prose mechanically.  Each mapped surface names the paths, field keys, enum
values, or tag slugs whose literal form must survive localization.
"""
from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

SURFACES: dict[str, dict[str, object]] = {
    "AI_ENTRYPOINT.md": {
        "locale": "locales/zh-CN/AI_ENTRYPOINT.md",
        "literals": (
            "en",
            "zh-CN",
            "AI_ENTRYPOINT.md",
            "datadrops/",
            "responses/",
            "messages/",
            "notifications/",
            "registry/packets/",
            "registry/responses/",
            "registry/messages/",
            "registry/notifications/",
            "registry/visits/",
            "registry/visitors/",
            "registry/tags/proposed/",
            "registry/tags/accepted/",
            "registry/INDEX.md",
            "registry/*_registry.csv",
            "scripts/generate_registry_views.py",
            "bridge_config.json",
        ),
    },
    "docs/localization/GLOSSARY.md": {
        "locale": "locales/zh-CN/GLOSSARY.md",
        "literals": (
            "content_origin",
            "source_refs",
            "source_note",
            "derivative_of",
            "provenance_coverage",
            "operator_authored",
            "third_party",
            "web",
            "model_generated",
            "mixed",
            "unknown",
        ),
    },
    "docs/localization/TAG_DISPLAY_CATALOG.md": {
        "locale": "locales/zh-CN/registry/TAG_DISPLAY_CATALOG.md",
        "literals": (
            "capstanai-labnote",
            "example-project",
            "human-in-the-loop",
            "provenance",
            "workflow-testing",
        ),
    },
    "docs/REGISTRY_RECORDS.md": {
        "locale": "locales/zh-CN/docs/REGISTRY_RECORDS.md",
        "literals": (
            "registry/REGISTRY_CONTRACT_V1.md",
            "registry/schemas/",
            "scripts/validate_repo.py",
            "registry/packets/<year>/<packet_id>.json",
            "registry/responses/<year>/<response_id>.json",
            "registry/visits/<year>/<visit_id>.json",
            "registry/visitors/<visitor_id>.json",
            "registry/messages/archived/<message_id>.json",
            "registry/notifications/delivered/<notification_id>.json",
            "registry/tags/proposed/<tag_slug>.json",
            "registry/tags/accepted/<tag_slug>.json",
            "registry/tags/deprecated/<tag_slug>.json",
            "acceptance_basis: operator_supplied",
            "branch + PR",
            "registry/INDEX.md",
            "scripts/generate_registry_views.py",
        ),
    },
    "lobby/ROUTINE_DEPOSIT_QUICKSTART.md": {
        "locale": "locales/zh-CN/lobby/ROUTINE_DEPOSIT_QUICKSTART.md",
        "literals": (
            "branch + PR",
            "registry/INDEX.md",
            "README_FIRST",
            "YYYYMMDD-<visitor_id>-<short-topic>",
            "datadrops/shared/inbox/<packet_id>.md",
            "registry/packets/YYYY/<packet_id>.json",
            "responses/signoffs/<packet_id>-signoff.md",
        ),
    },
    "lobby/TAGGING_PROTOCOL.md": {
        "locale": "locales/zh-CN/lobby/TAGGING_PROTOCOL.md",
        "literals": (
            "registry/tags/accepted/*.json",
            "registry/tags/proposed/<tag_slug>.json",
            "registry/tags/accepted/<tag_slug>.json",
            "acceptance_basis: operator_supplied",
            "branch + PR",
            "proposed",
            "accepted",
        ),
    },
    "registry/README.md": {
        "locale": "locales/zh-CN/registry/README.md",
        "literals": (
            "INDEX.md",
            "scripts/generate_registry_views.py",
        ),
    },
    "docs/UPGRADING.md": {
        "locale": "locales/zh-CN/docs/UPGRADING.md",
        "literals": (
            "schema_version",
            "bridge_config.json",
            "registry/INDEX.md",
            "CI",
        ),
    },
    "SECURITY.md": {
        "locale": "locales/zh-CN/SECURITY.md",
        "literals": (),
    },
    "templates/datadrop_packet.md": {
        "locale": "locales/zh-CN/templates/datadrop_packet.md",
        "literals": (
            "packet_id",
            "source_session",
            "target_session",
            "created_by",
            "deposited_by",
            "content_origin",
            "source_refs",
            "derivative_of",
            "provenance_coverage",
        ),
    },
    "templates/ai_response_packet.md": {
        "locale": "locales/zh-CN/templates/ai_response_packet.md",
        "literals": (
            "response_id",
            "responding_session",
            "source_packet_id",
            "created_by",
            "deposited_by",
            "content_origin",
            "source_refs",
            "derivative_of",
            "provenance_coverage",
            "confidence: low | medium | high",
            "response_type: answer | critique | synthesis | counterproposal | review",
        ),
    },
    "templates/message_packet.md": {
        "locale": "locales/zh-CN/templates/message_packet.md",
        "literals": (
            "message_id",
            "from_visitor_id",
            "to_visitor_id",
            "to_group",
            "reply_to",
            "reply_expected",
            "response_message_id",
            "needs_human_relay",
        ),
    },
    "templates/notification_request.md": {
        "locale": "locales/zh-CN/templates/notification_request.md",
        "literals": (
            "notification_id",
            "from_visitor_id",
            "to_visitor_id",
            "message_id",
            "needs_human_action",
        ),
    },
    "templates/visit_signoff.md": {
        "locale": "locales/zh-CN/templates/visit_signoff.md",
        "literals": (
            "visit_id",
            "created_at",
            "visitor_id",
            "session_family",
            "relay_needed",
            "signoff_path",
        ),
    },
    "templates/visitor_registration.md": {
        "locale": "locales/zh-CN/templates/visitor_registration.md",
        "literals": (
            "visitor_id",
            "created_at",
            "session_family",
            "session_type",
            "display_name",
            "profile_path",
        ),
    },
}


def main() -> int:
    failures: list[str] = []
    for source_rel, definition in SURFACES.items():
        source = ROOT / source_rel
        locale = ROOT / str(definition["locale"])
        if not source.is_file():
            failures.append(f"canonical surface is missing: {source_rel}")
            continue
        if not locale.is_file():
            failures.append(f"localized counterpart is missing: {locale.relative_to(ROOT)}")
            continue

        source_text = source.read_text(encoding="utf-8")
        localized_text = locale.read_text(encoding="utf-8")
        for literal in definition["literals"]:
            if literal not in source_text:
                failures.append(
                    f"test map is stale: {literal!r} is not present in {source_rel}"
                )
                continue
            if literal not in localized_text:
                failures.append(
                    f"{locale.relative_to(ROOT)} is missing invariant literal {literal!r} "
                    f"from {source_rel}"
                )

    if failures:
        raise AssertionError("Locale invariant check failed:\n" + "\n".join(failures))

    print(f"locale invariant check passed ({len(SURFACES)} mapped surfaces)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
