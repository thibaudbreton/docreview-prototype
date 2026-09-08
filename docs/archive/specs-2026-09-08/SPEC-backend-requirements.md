# Backend SRM — Feature Specification

> **Provenance note (added during the docs cleanup, 2026-08-16):** this file was not previously tracked in the `SRM-PROTO` git repository. It was located outside the repo (on the author's Desktop and Downloads, in two byte-identical copies) during a corpus-wide inventory. Several other documents in this repo — `docs/specs/SPEC-domain-model.md` §9.1/§9.2, `docs/specs/SPEC-expert-space.md`, and multiple tickets in `docs/archive/` — cite a file named `SPEC-backend-requirements.md` by section number (e.g. "§11," "§12," "§8," "§5") for exactly this kind of content (compliance-matrix export, restricted-view access, notification triggers, scale targets). This document's subject matter, section numbering, and content are a strong match for those citations. **This is not confirmed to be byte-identical to whatever file those citations originally pointed to** — treat the match as very likely, not proven. The real client company name has been replaced with "the client" throughout, per this repo's standing confidentiality convention (see `HANDOVER.md`).

## User Stories

- As a **Project Manager**, I want to create and manage a SRM project in manual or AI-assisted mode so that I can control how requirements are processed for a given tender.
- As a **Requirement Manager (contributor)**, I want to create, modify, and delete requirements from image or human input, within my assigned scope (SIG or RSC), so that I can contribute accurately to a project.
- As an **Expert Reviewer**, I want to review and manually rework compliance results, with locking and audit logs, so that I can validate or override AI outputs.
- As a **VIP**, I want access to a KPI dashboard so that I can monitor project health and AI performance without editing data.
- As an **Admin**, I want to manage users, roles, authorizations, and system configuration so that the platform operates securely and correctly.
- As any **authenticated user**, I want to receive in-app and email notifications about relevant project events so that I stay informed without polling the interface.
- As a **Requirement Manager**, I want to import and export requirements and compliance matrices from/to DOORS 9 and DOORS NG so that I can synchronize with existing toolchains.
- As a **Project Manager**, I want the system to apply the "most restrictive wins" rule across multi-allocation compliance results so that non-compliant outcomes always surface correctly.
- As a **user**, I want Q&A access to expert knowledge and to customer feedback (including competitor references) so that I can make informed decisions during requirement analysis.

---

## Functional Requirements

### Frontend & Connectivity
1. The backend must support a modern Node.js-based frontend (Vite or React).

### Requirement Management
2. The system must support requirement creation from an image (OCR/AI capture) and from manual human input (text entry or structured form).
3. The system must support requirement modification (re-assignment/review) and deletion.
4. Requirement creation and processing must be available in two modes — **manual** and **AI-assisted** — selected once at project creation and applied for the lifetime of that project.

### Compliance Management
5. The system must support manual compliance rework by authorized users, with an audit log of every change and a locking mechanism to prevent concurrent edits.
6. The system must implement a "most restrictive wins" compliance model: when a requirement has multiple allocations (e.g. RSC and SIG) with differing compliance results, the non-compliant result takes precedence.

### Notifications
7. The system must support in-app and email notifications; detailed notification triggers to be specified in a follow-up iteration.

### Performance
8. Operations on the central requirement table must respond within **300 ms** (P95); 100 ms is the stretch target.
9. File loading must complete in under **3 seconds** for files of up to **10,000 lines**.

### AI Capabilities
10. In AI-assisted mode, the system must support automated **capture**, **characterisation**, and **allocation** of requirements, with full tracking and storage of AI outputs.
11. The system must support **human-in-the-loop** review at each AI processing stage.
12. The system must support **gap analysis** between captured requirements and reference documents or compliance rules.
13. AI outputs must expose a **confidence score**, KPIs, and the raw characterizer and allocator outputs for each requirement.

### Data & Allocation
14. The system must support **manual allocation** and **multiple allocation** (a single requirement assigned to more than one entity).
15. All requirements, associated data, and current status must be persisted and queryable.

### Document Management
16. The system must support upload of up to **30 documents per turnkey project**, with document order preserved (order affects document view and export output).
17. All documents must be stored with **versioning** and a **full change log** (who changed what, when, and how — machine or human).
18. The system must provide **SQL-based filtering** over the document and requirement dataset.

### Q&A
19. The system must provide a **Q&A interface with the client's experts** linked to specific requirements or documents.
20. The system must provide a **Q&A interface for customer feedback**, including the ability to capture and associate feedback that references competitor products or specifications.

### Scalability
21. The system must support up to **10,000 users** via a phased ramp-up, with up to **30,000 requirements** per deployment (average project size: ~5,000 requirements).

### Observability
22. The system must log all **agent and LLM calls**, including cost attribution and agentic chain traceability.
23. The system must log every change to a file — machine-generated or human-initiated — with full session-level tracking per user (all actions a user takes within a session are recorded).

### User Management & Access Control
24. The system must support five roles with the following access scopes:
    - **Project Manager (tender):** full access restricted to their assigned project.
    - **Requirement Manager (contributor):** restricted to SIG or RSC requirement activities within assigned projects.
    - **Expert Reviewer:** restricted to review and compliance validation activities.
    - **Admin:** unrestricted access to all system functions.
    - **VIP:** read-only access to KPI dashboard.
25. All users must authenticate via **SSO** (the client's identity provider).
26. The system must expose user authorization management for Admins (grant, revoke, modify roles).

### Security & Privacy
27. The system must comply with applicable **cybersecurity** standards and **data privacy** regulations (specific standards to be confirmed with the security team).

### DOORS Integration
28. The system must support **bidirectional integration with DOORS 9 and DOORS NG**: import of requirements and compliance matrices from DOORS, and export back to DOORS 9/NG.
29. The system must support **Excel export** of requirements and compliance matrices.

---

## Acceptance Criteria

- **FR1:** The application builds and runs against the latest LTS Node.js version using Vite or React without deprecation errors.
- **FR2–3:** A requirement can be created from an uploaded image (AI-extracted) and from manual input; existing requirements can be modified and deleted with changes reflected immediately in the central table.
- **FR4:** Mode (manual / AI-assisted) is set at project creation, cannot be changed mid-project, and all subsequent processing respects that mode.
- **FR5:** A compliance result can be manually edited by an authorized user; the change is logged with timestamp, user ID, previous and new values; the record is locked during editing and unlocked on save or cancel.
- **FR6:** Given two allocations on one requirement — one compliant, one non-compliant — the system displays and exports the result as non-compliant.
- **FR7:** Users receive in-app and email notifications for events defined in the notification trigger spec (to be validated in next iteration).
- **FR8:** P95 response time for central table operations is ≤ 300 ms under load, measured by automated performance tests.
- **FR9:** A 10,000-line file loads completely in the UI in under 3 seconds, verified by load test.
- **FR10–13:** In AI-assisted mode, the system completes capture → characterisation → allocation for a sample document and stores outputs; gap analysis report is generated; confidence scores and KPIs are visible per requirement.
- **FR14:** A requirement can be assigned to multiple entities; all allocations are visible and stored.
- **FR15:** All requirements and their statuses are queryable via the data layer with no data loss on restart.
- **FR16:** Up to 30 documents can be uploaded to a single turnkey project; reordering documents changes their sequence in the document view and in exports.
- **FR17:** Every document change (upload, edit, delete, version bump) is recorded in the audit log with actor, timestamp, and change type.
- **FR18:** A SQL-style filter applied to the requirement table returns the correct filtered set within the latency SLA.
- **FR19–20:** An expert can respond to a Q&A thread linked to a requirement; a customer feedback entry can be created and tagged with a competitor reference.
- **FR21:** The system handles 10,000 concurrent users and 30,000 requirements without degradation below the latency SLA, validated by stress test.
- **FR22:** Each LLM/agent call produces a log entry with model ID, token count, cost estimate, and chain position.
- **FR23:** A per-session activity log exists for each user, capturing every action with timestamp and context.
- **FR24–26:** Each role can only access and perform actions within its defined scope; SSO login is required for all users; Admins can modify user roles without requiring a code change.
- **FR27:** A security review sign-off is obtained before production deployment.
- **FR28–29:** A DOORS-exported file can be re-imported without data loss; an Excel export contains all requirement fields and compliance status.

---

## Success Criteria

- All P95 latency targets (≤ 300 ms for table operations, < 3 s for file loading) are met under realistic load.
- End-to-end AI pipeline (capture → characterisation → allocation → gap analysis) runs without manual intervention in AI-assisted mode.
- Role-based access is verified by penetration test or security review with zero critical findings.
- DOORS round-trip (import → edit → export → re-import) produces no data loss or corruption.
- System sustains 10,000 concurrent users and 30,000 requirements with no SLA breach.
- Audit log captures 100% of human and machine changes with no gaps.

---

## Out of Scope

- Requirement creation via **copy** (deferred to a future iteration).
- Detailed notification trigger rules (to be specified separately).
- Specific cybersecurity standard selection (to be confirmed with the security team).
- Mobile or native application support.
- Integration with tools other than DOORS 9, DOORS NG, and Excel.
