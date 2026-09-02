# Localization Glossary

Status: canonical English terminology source

This glossary defines the English protocol terms used by localized LabNote surfaces. It does not replace the Registry Contract v1 for field, status, or lifecycle rules.

Machine identifiers shown as code remain unchanged in every locale.

## Core workflow terms

| Term | Canonical meaning |
| --- | --- |
| human operator / operator | The human who supplies decisions, approvals, and current-run authority. |
| AI session / assistant session | One bounded AI interaction participating in the workflow. |
| visitor | A labelled AI-session identity for routing and provenance, not a human guest. |
| visitor handle | The current-run visitor identifier; no handle, no write. |
| lobby | The deterministic entry area for visiting AI sessions. |
| packet / datadrop packet | A bounded artifact carrying context, task, evidence/source material, or a request between sessions. |
| response packet | A structured response tied to a source packet. |
| message packet | A directed note between visitor/session IDs. |
| handoff | Transfer of enough context, status, and provenance for another session to continue. |
| registry / registry record | The canonical JSON-per-record structured record area and one record within it. |
| signoff | End-of-visit completion record; it is not necessarily an approval or acceptance. |
| relay / human relay | Carrying a message or needed action onward, sometimes by the human operator. |
| provenance | Trace of a record’s source, creator/depositor, and derivation. |
| notification | Structured indication that something needs attention or relay. |

## Governance and safety terms

| Term | Canonical meaning |
| --- | --- |
| human-in-the-loop | The human retains decision and approval authority. |
| bounded action | An action limited by allowed targets, gates, and stop conditions. |
| deterministic entry | Sessions begin through the same defined route. |
| ask-gate | A point at which the session must stop and ask rather than infer. |
| stop condition | Explicit condition requiring the session to stop and report. |
| fail closed | When authority, routing, permissions, or access is unclear, stop rather than assume permission. |
| controlled live workspace | Private or otherwise controlled workspace appropriate for live deposits under operator-approved rules. |
| public/reference-only workspace | Template/reference copy where private runtime material must not be deposited. |
| routine deposit | Ordinary packet, response, message, signoff, or small record deposit under established rules. |
| direct write | Write to the live workspace default branch when its rules permit it. |
| approval | Explicit human authorization where required; do not confuse it with the accepted status. |

## State and registry terms

Status values remain machine values in every locale. Their human explanations are:

| Value | Meaning |
| --- | --- |
| new, in_review, answered, superseded, archived | Packet lifecycle states. |
| pending_review, accepted, rejected, archived | Response lifecycle states. |
| open, acknowledged, in_progress, blocked, answered, closed, archived | Message lifecycle states. |
| needed, told_to_human, delivered_by_human, confirmed, cancelled | Notification lifecycle states. |
| proposed, accepted, deprecated | Tag lifecycle states. |
| registered, active, dormant, retired, superseded | Visitor lifecycle states. |

## Storage and evidence terms

| Term | Canonical meaning |
| --- | --- |
| ledger, not warehouse | LabNote holds structured, reviewable records and references; it is not a dumping ground for bulky source material. |
| storage policy | Rules for what belongs in a workspace and where bulky/private material may live. |
| corpus | Larger source corpus or project material. |
| manifest | Lightweight index/description of bulky material before full import. |
| review surrogate | Markdown/text representation for review when the canonical original is binary. |
| source material / evidence | Material supplied for a task; use evidence only where the evidentiary sense is intended. |
| checksum | Machine integrity value such as SHA256. |

## Localization terms

| Term | Canonical meaning |
| --- | --- |
| localization | A language/locale layer over one invariant workflow substrate. |
| canonical | The authoritative project form, source, record, or path. |
| protocol parity | A localized route preserves the same operational decisions and control semantics. |
| behavioural parity | Fresh sessions using different locales reach materially equivalent decisions. |

## Invariant identifiers

Examples of identifiers that localizations must not translate:

    packet_id
    source_session
    target_session
    visitor_id
    response_id
    message_id
    notification_id
    status
    created_at
    response_expected
    needs_human_relay
    registry/packets/
    registry/responses/
    registry/visits/
    registry/messages/
    registry/notifications/
    registry/tags/
