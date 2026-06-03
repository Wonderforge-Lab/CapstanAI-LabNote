# Quickstart

1. Decide where bulky supporting material will live if the work needs it. Use external storage such as Google Drive, Dropbox, OneDrive, S3-compatible storage, a local folder, or another blob vault your assistant/session can access.
2. Create or identify a visitor/session ID.
3. Copy `templates/datadrop_packet.md`.
4. Fill in the packet header and task sections.
5. If the packet depends on larger files, add a stable storage reference and a short summary instead of committing the raw dump.
6. Register the packet in `registry/packet_registry.csv`.
7. Give the packet to the target assistant session.
8. Copy `templates/ai_response_packet.md` for the answer.
9. Register the response in `registry/response_registry.csv`.
10. Review the response before marking anything accepted.

Small files, clear labels, no mystery memory. That is the trick.
