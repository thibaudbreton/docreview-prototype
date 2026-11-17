"""Content of the Smart Req notification email samples. Fictional data only.

Built by build_emails.py. Inline markup: **bold**, [[SRM-00042]] for a requirement ID.
A row is (text, link label, link URL). Dates follow the 2026 calendar (Tue 17 Nov 2026).
"""

BASE = "https://smartreq.example"
SETTINGS = BASE + "/settings/notifications"

SMART_REQ = ("Smart Req", "no-reply@smartreq.example")
LOUIS = ("Louis Renaud", "louis.renaud@example.com")
THIBAUD = ("Thibaud Breton", "thibaud.breton@example.com")

STB = "STB-2026 · Energy Monitoring System"
RFP = "RFP-2026-114 · Line 4 Resignalling — ETCS L2"

SETTINGS_LINK = ("Notification settings", SETTINGS, "")
UNATTENDED = "Sent by Smart Req from an unattended mailbox: replies aren't read."
SUMMARY_WHEN = ("Working days at 08:00 in the person's time zone, only if something new "
                "for them hasn't been seen in Smart Req. One email for all their tenders.")
SUMMARY_FOOTER = [
    "You get this summary on working days when something new for you hasn't been seen "
    "in Smart Req. What you've already seen there isn't repeated.",
    ("Notification settings", SETTINGS, " — change the frequency, or stop emails for one tender"),
    UNATTENDED,
]


def t(tender, path=""):
    return f"{BASE}/tenders/{tender}{path}"


EMAILS = [
    # ------------------------------------------------------------------ pilot
    dict(
        slug="added-to-tender", title="Added to a tender", phase="Pilot", klass="A — immediate",
        when="When someone adds you to a tender. Always sent, even with emails turned off: "
             "it's often the first contact with the tender.",
        reason="added", tenders=["STB-2026"], sender=SMART_REQ, to=LOUIS, date=(2026, 11, 10, 10, 25),
        subject="STB-2026 — You've been added as a contributor for SIG",
        preheader="Energy Monitoring System · submission Fri 11 Dec · nothing to do yet",
        blocks=[
            ("eyebrow", STB),
            ("h1", "Thibaud Breton added you to this tender"),
            ("p", "You're a contributor for the **SIG** sub-system. When requirements reach SIG, "
                  "you'll check who in SIG takes each one, and later answer the ones assigned to you."),
            ("p", "**Nothing to do yet.** Smart Req will tell you when there is."),
            ("facts", [("Tender manager", "Thibaud Breton"), ("Your sub-system", "SIG"),
                       ("Submission", "Fri 11 Dec 2026")]),
            ("button", ("Open STB-2026", t("STB-2026"))),
            ("muted", "New to Smart Req? It's where this tender's requirements are captured, routed to "
                      "the people who answer them, and prepared for the client. Sign in with your "
                      "company account."),
            ("muted", "Everything appears in Smart Req, under the bell. By email, you get at most one "
                      "summary a day, only about what you haven't seen there, and a message when "
                      "someone mentions you."),
        ],
        footer=["You get this email because you were added to a tender. This one is always sent.",
                SETTINGS_LINK, UNATTENDED],
    ),
    dict(
        slug="processing-finished", title="Processing finished", phase="Pilot", klass="A — immediate",
        when="To the tender manager who launched a capture, an added document or a new version, "
             "if the result is still unseen in Smart Req 10 minutes after it finished.",
        reason="processing", tenders=["STB-2026"], sender=SMART_REQ, to=THIBAUD, date=(2026, 11, 17, 9, 34),
        subject="STB-2026 — Functional Specification v2.1 is processed: 7 requirements changed",
        preheader="4 requirements back to review in Allocation · see what changed",
        blocks=[
            ("eyebrow", STB),
            ("h1", "Functional Specification v2.1 is processed"),
            ("p", "The new version you uploaded at 08:51 finished processing at 09:24."),
            ("rows", [
                ("**7 requirements changed:** 2 added, 4 modified, 1 removed.", "See the changes",
                 t("STB-2026", "/documents/changes?from=v2.0&to=v2.1")),
                ("**4 requirements** went back to review in Allocation.", "Open them",
                 t("STB-2026", "/allocation?show=back-to-review")),
            ]),
        ],
        footer=["Sent because you launched this processing and hadn't seen the result in Smart Req "
                "10 minutes after it finished.", SETTINGS_LINK, UNATTENDED],
    ),
    dict(
        slug="processing-failed", title="Processing failed", phase="Pilot", klass="A — immediate",
        when="Same rule as a finished processing: to the tender manager who launched it, "
             "if the failure is still unseen in Smart Req 10 minutes later.",
        reason="processing", tenders=["STB-2026"], sender=SMART_REQ, to=THIBAUD, date=(2026, 11, 19, 10, 15),
        subject="STB-2026 — Interface Control Document couldn't be processed",
        preheader="The PDF is password-protected · nothing else in the tender changed",
        blocks=[
            ("eyebrow", STB),
            ("h1", "Interface Control Document couldn't be processed"),
            ("p", "The document you added at 10:02 couldn't be read: **the PDF is password-protected**."),
            ("p", "Nothing else in the tender changed: the other documents and the work on them are "
                  "untouched. Upload a copy without a password and Smart Req will process it."),
            ("button", ("Open Documents", t("STB-2026", "/documents"))),
        ],
        footer=["Sent because you added this document and hadn't seen the result in Smart Req "
                "10 minutes later.", SETTINGS_LINK, UNATTENDED],
    ),
    dict(
        slug="mention", title="Mention in a comment", phase="Pilot", klass="A — immediate",
        when="When someone mentions you with @ in a comment, if you haven't seen it in Smart Req "
             "within 10 minutes.",
        reason="mention", tenders=["STB-2026"], sender=SMART_REQ, to=LOUIS, date=(2026, 11, 18, 11, 15),
        subject="STB-2026 — Claire Moreau mentioned you on SRM-00057",
        preheader="“Is this one for SIG or for TRK? Since v2.1 it also covers the track circuits.”",
        blocks=[
            ("eyebrow", STB),
            ("h1", "Claire Moreau mentioned you in a comment"),
            ("reqs", [("SRM-00057", "Train detection shall remain available when one of the two "
                                    "field units is out of service.", "In Allocation · sub-system SEN")]),
            ("quote", {"text": "@Louis Renaud is this one for SIG or for TRK? Since v2.1 it also "
                               "covers the track circuits.",
                       "by": "Claire Moreau · SEN · 11:05"}),
            ("button", ("Reply in Smart Req", t("STB-2026", "/requirements/SRM-00057?comment=1842"))),
        ],
        footer=["You get an email for a mention only when you haven't seen it in Smart Req within "
                "10 minutes.", SETTINGS_LINK, UNATTENDED],
    ),
    dict(
        slug="daily-summary-contributor", title="Daily summary — contributor", phase="Pilot",
        klass="B — daily summary", when=SUMMARY_WHEN,
        reason="summary", tenders=["STB-2026"], sender=SMART_REQ, to=LOUIS, date=(2026, 11, 18, 8, 0),
        subject="STB-2026 — 23 requirements to allocate in SIG and 1 more update",
        preheader="Since Tue 08:00 · STB-2026",
        blocks=[
            ("eyebrow", "Daily summary · Wed 18 Nov"),
            ("h1", "2 updates for you since Tue 08:00"),
            ("p", "Louis, here's what's new for you on STB-2026."),
            ("group", {"title": STB, "context": "Contributor · SIG · submission Fri 11 Dec, 23 days left",
                       "rows": [
                           ("**23 requirements** reached SIG and need allocating.", "Open them in Allocation",
                            t("STB-2026", "/allocation?subsystem=SIG&show=to-allocate")),
                           ("Your reallocation request for [[SRM-00042]] was declined: it stays with SIG. "
                            "Thibaud Breton: “The interface part is ours.”", "Open SRM-00042",
                            t("STB-2026", "/requirements/SRM-00042")),
                       ]}),
        ],
        footer=SUMMARY_FOOTER,
    ),
    dict(
        slug="daily-summary-tender-manager", title="Daily summary — tender manager", phase="Pilot",
        klass="B — daily summary", when=SUMMARY_WHEN,
        reason="summary", tenders=["STB-2026", "RFP-2026-114"], sender=SMART_REQ, to=THIBAUD,
        date=(2026, 11, 18, 8, 0),
        subject="STB-2026 — 5 reallocation requests to decide and 2 more updates",
        preheader="Since Tue 08:00 · STB-2026, RFP-2026-114",
        blocks=[
            ("eyebrow", "Daily summary · Wed 18 Nov"),
            ("h1", "3 updates for you since Tue 08:00"),
            ("p", "Thibaud, here's what's new for you on 2 tenders."),
            ("group", {"title": STB,
                       "context": "Tender manager · 61 of 104 requirements allocated · "
                                  "submission Fri 11 Dec, 23 days left",
                       "rows": [
                           ("**5 reallocation requests** to decide: 3 from SIG, 2 from SEN.", "Decide",
                            t("STB-2026", "/allocation?show=requests")),
                           ("**1 missing sub-system** proposed: TRK, on [[SRM-00063]].", "Review it",
                            t("STB-2026", "/requirements/SRM-00063")),
                       ]}),
            ("group", {"title": RFP, "context": "Tender manager · submission Fri 29 Jan 2027",
                       "rows": [
                           ("**Allocation is complete:** all 318 requirements are allocated.",
                            "Open the dashboard", t("RFP-2026-114", "/dashboard")),
                       ]}),
        ],
        footer=SUMMARY_FOOTER,
    ),
    # ------------------------------------------------------------ after the pilot
    dict(
        slug="reminder", title="Reminder from a tender manager", phase="After the pilot",
        klass="A — immediate",
        when="When a tender manager sends a reminder from Compliance, if it's unseen in Smart Req "
             "10 minutes later. One email per reminder, listing every assignment it covers.",
        reason="reminder", tenders=["STB-2026"], sender=("Thibaud Breton via Smart Req", "no-reply@smartreq.example"),
        reply_to=THIBAUD, to=LOUIS, date=(2026, 12, 1, 14, 42),
        subject="STB-2026 — Reminder: 4 assignments waiting on your answer",
        preheader="“We need SIG's answers before the QCD review on Thursday.” — Thibaud Breton",
        blocks=[
            ("eyebrow", STB),
            ("h1", "Thibaud Breton is waiting on your answer for 4 assignments"),
            ("quote", {"text": "We need SIG's answers before the QCD review on Thursday.",
                       "by": "Thibaud Breton · Tender manager"}),
            ("reqs", [
                ("SRM-00001", "The system shall record the energy consumed by each substation every "
                              "15 minutes.", "Waiting 9 days"),
                ("SRM-00004", "The system shall provide a monthly consumption report for each line.",
                 "Waiting 6 days"),
                ("SRM-00021", "Unacknowledged alarms shall be escalated to the control centre within "
                              "2 minutes.", "Waiting 6 days"),
                ("SRM-00030", "Reports shall be exportable to CSV and PDF.", "Waiting 3 days"),
            ]),
            ("button", ("Answer them in Smart Req", t("STB-2026", "/compliance?show=reminded&at=2026-12-01T14:32"))),
            ("muted", "Reply to this email to write to Thibaud directly."),
        ],
        footer=["Thibaud Breton sent this reminder from Smart Req at 14:32. Reminders are always sent "
                "by a person, at most once every 2 days on this tender.", SETTINGS_LINK],
    ),
    dict(
        slug="daily-summary-compliance", title="Daily summary — with Compliance", phase="After the pilot",
        klass="B — daily summary",
        when=SUMMARY_WHEN + " Grey “Still waiting” lines never send an email on their own.",
        reason="summary", tenders=["STB-2026", "RFP-2026-114"], sender=SMART_REQ, to=LOUIS,
        date=(2026, 12, 1, 8, 0),
        subject="STB-2026 — 4 new assignments and 2 more updates",
        preheader="Since Mon 08:00 · STB-2026, RFP-2026-114",
        blocks=[
            ("eyebrow", "Daily summary · Tue 1 Dec"),
            ("h1", "3 updates for you since Mon 08:00"),
            ("p", "Louis, here's what's new for you on 2 tenders."),
            ("group", {"title": STB, "context": "Contributor · SIG · submission Fri 11 Dec, 10 days left",
                       "rows": [
                           ("**4 new assignments** in SIG.", "Open them",
                            t("STB-2026", "/compliance?show=new-for-me")),
                           ("**3 of your answers** were reopened by Functional Specification v2.2: "
                            "the requirements changed.", "Answer them again",
                            t("STB-2026", "/compliance?show=reopened")),
                       ],
                       "waiting": [
                           ("2 of your assignments have been waiting more than 5 days.", "Open them",
                            t("STB-2026", "/compliance?show=waiting")),
                       ]}),
            ("group", {"title": RFP, "context": "Contributor · SIG",
                       "rows": [
                           ("The client answered your question on [[SRM-00031]] (Q-12).", "Read the answer",
                            t("RFP-2026-114", "/requirements/SRM-00031?tab=questions")),
                       ]}),
        ],
        footer=SUMMARY_FOOTER,
    ),
]
