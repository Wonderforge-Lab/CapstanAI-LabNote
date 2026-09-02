# Status Lifecycle Matrix

## Packets

`new -> in_review -> answered`. Any non-archived packet may become `superseded` or `archived`.

## Responses

`pending_review -> accepted | rejected`. Any non-archived response may become `archived`.

## Messages

| Status | Content and registry bucket |
|---|---|
| open, acknowledged, in_progress, blocked | `messages/open/` and `registry/messages/open/` |
| answered | `messages/answered/` and `registry/messages/answered/` |
| closed | `messages/closed/` and `registry/messages/closed/` |
| archived | `messages/archived/` and `registry/messages/archived/` |

A message may move through acknowledgement, work, block, answer, close, or archive. Archived is terminal. A materially new request is a new message, not an implicit reopen.

## Notifications

| Status | Content and registry bucket |
|---|---|
| needed, told_to_human | `notifications/open/` and `registry/notifications/open/` |
| delivered_by_human | `notifications/delivered/` and `registry/notifications/delivered/` |
| confirmed, cancelled | `notifications/closed/` and `registry/notifications/closed/` |

Confirmed and cancelled are terminal.

## Visitors, tags, and visits

Visitors: `registered -> active <-> dormant`; `retired` and `superseded` are terminal.

Tags: `proposed -> accepted | deprecated`; `accepted -> deprecated`. An AI-created proposal cannot become accepted in the same change set.

Visits are append-only signoff records with no lifecycle status.

The validator will enforce status/path consistency and legal state transitions where the prior record is available in the comparison base.
