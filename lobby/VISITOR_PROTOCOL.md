# Visitor Protocol

Each assistant session should identify itself with a visitor ID before working.

On entry:

- read the relevant packet or request,
- identify or register `visitor_id`,
- check messages addressed to that ID,
- check messages addressed to the visitor family,
- check relay notifications,
- proceed with the task.

On exit:

- update any packet, message, response, or notification rows touched,
- create a signoff from `templates/visit_signoff.md`,
- append a row to `registry/visit_registry.csv`.
