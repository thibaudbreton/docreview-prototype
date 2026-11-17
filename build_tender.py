#!/usr/bin/env python3
"""build_tender.py — write tenders.js: generated demo tenders for the Allocation screen.

One tender today: RFP-2026-152 "Northern Corridor Resignalling — ETCS L2", a
standalone SIG tender on the Mainline Wayside product, at the size of one real
document set (about 250 blocks). RFP-2026-114 shows every state on twelve
requirements written by hand; this one shows the same screen at working volume,
with the whole chain filled in: class, ABS, PBS, one to three roles (OBS) and
the person in charge of each.

Every word of it is fictional. ABS / PBS / OBS values are read from keys.js
(build_keys.py), never typed here: an id that is not flagged for the product
stops the script.

What the script decides, from a fixed seed so the tender is the same on every
run: who is in charge of each role, the model's confidence on each field, and
the states a working tender always holds — a few requirements with no role
yet, a few proposals the model is unsure of, a few roles with nobody on them.

Usage:
    python3 build_tender.py        # writes tenders.js
    python3 build_merge.py         # inlines it into the app
"""
import json
import random
import sys
from pathlib import Path

KEYS_FILE = "keys.js"
OUT = "tenders.js"
PRODUCT_KEY = "mainline-wayside"
SEED = 152

TENDER_ID = "rfp152"
ID_PREFIX = "NC"

# How many requirements start in each state. Kept together so the mix is one
# decision, not something scattered through the code below.
N_NO_ROLE = 15         # no role (OBS) derived: Incomplete
N_NO_CHAIN = 5         # ...of which nothing derived at all (no ABS, no PBS either)
N_LOW_TYPE = 5         # type proposed with low confidence
N_LOW_CLASS = 5        # class proposed with low confidence
N_LOW_CHAIN = 10       # one of ABS / PBS / OBS under the 75 % threshold
N_NOBODY_SINGLE = 12   # one role, nobody in charge
N_NOBODY_MULTI = 8     # several roles, one of them with nobody in charge
N_LOW_TYPE_INFO = 4    # information blocks whose type the model is unsure of

DOCS = [
    {"id": "d1", "name": "Tender specification — signalling and train control", "file": "NC_signalling_main.pdf",
     "versions": [{"v": "v1.0", "date": "Sep 14, 2026", "note": "Invitation to tender"}]},
    {"id": "d2", "name": "Technical annex — delivery, assurance and services", "file": "NC_annex_delivery.pdf",
     "versions": [{"v": "v1.0", "date": "Sep 14, 2026", "note": "Invitation to tender"}]},
]

# The tender's people: all on SIG (DEC-102 — a person belongs to one sub-system).
# Ids "dirN" are the Allocation screen's own directory entries, so a person
# found through "Search a person…" and a person listed here are one and the same.
PALETTE = ["#6e7bf2", "#3fb27f", "#e0a43c", "#a06ef2", "#e5544b", "#3fa9b2", "#c46bd6", "#5c9ee0"]
PEOPLE = [
    ("dir3", "Marc Dubois", "SIG · Train control"),
    ("dir5", "Thomas Weber", "SIG · Interlocking"),
    ("dir6", "Léa Girard", "SIG · Control centre"),
    ("dir7", "Omar Saidi", "SIG · Control centre"),
    ("dir8", "Anaïs Petit", "SIG · Telecoms and networks"),
    ("dir9", "Hugo Bernard", "SIG · Power supply"),
    ("dir11", "Nicolas Roux", "SIG · Installation"),
    ("dir13", "Youssef Amrani", "SIG · Installation"),
    ("dir10", "Ines Kaya", "SIG · V&V and commissioning"),
    ("dir12", "Camille Fontaine", "SIG · V&V and commissioning"),
    ("dir4", "Fatima Zahra", "SIG · Safety and RAM"),
    ("dir14", "Elodie Simon", "SIG · Safety and RAM"),
    ("dir15", "Pierre Lefevre", "SIG · Cybersecurity"),
    ("dir16", "Sara Nasri", "SIG · Project office"),
    ("dir19", "Julien Marchal", "SIG · Project office"),
]
# Who can be put in charge of which role. "m_sig" and "sup" are the two SIG
# contributors every tender of the prototype already has.
ROLE_PEOPLE = {}
for roles, people in [
    (["obs13", "obs14", "obs15", "obs30"], ["m_sig", "dir3"]),
    (["obs22", "obs23", "obs24", "obs25"], ["sup", "dir5"]),
    (["obs17", "obs20", "obs21", "obs27"], ["dir6", "dir7"]),
    (["obs18", "obs19"], ["dir8"]),
    (["obs35"], ["dir9"]),
    (["obs45", "obs46", "obs47"], ["dir11", "dir13"]),
    (["obs37", "obs38", "obs39"], ["dir10", "dir12"]),
    (["obs42", "obs43", "obs44", "obs51", "obs52"], ["dir4", "dir14"]),
    (["obs53", "obs54", "obs55"], ["dir15"]),
    (["obs1", "obs2", "obs4", "obs5", "obs6", "obs7", "obs8", "obs9", "obs10", "obs11",
      "obs40", "obs58", "obs60", "obs62", "obs64", "obs66"], ["dir16", "dir19"]),
]:
    for r in roles:
        ROLE_PEOPLE[r] = people


def ctx(**kw):
    """Defaults for the requirements that follow: abs, pbs, obs, cls."""
    return ("ctx", kw)


def H(text):
    return ("h", text)


def I(text):
    return ("i", text)


def R(text, **kw):
    """A requirement. Overrides: abs, pbs, obs, cls; also=[roles] adds further roles."""
    return ("r", text, kw)


SECTIONS = [
    # ------------------------------------------------------------------ document 1
    ("d1", "1", "Scope and general provisions", [
        I("This specification defines the requirements applicable to the resignalling of the Northern Corridor with ETCS Level 2, from Arden Junction to Dunmere, including the approach to the Eastfield depot."),
        I("The line is 86 km long and comprises fourteen stations, three junctions and twenty-two level crossings. It remains in commercial service throughout the works."),
        I("Onboard equipment is procured under a separate contract and is outside the scope of this specification, except for the track-to-train interfaces defined in section 2."),
        H("1.1 Definitions and applicable documents"),
        I("In this document, the Supplier designates the tenderer once the contract is awarded, and the Infrastructure Manager designates the owner and operator of the line."),
        I("Where a standard is cited without a date, the edition in force on the date of the invitation to tender applies."),
        I("Requirements are identified individually. Explanatory paragraphs carry no contractual obligation."),
        H("1.2 Project organisation"),
        ctx(abs="project-management", pbs="2", obs="obs1", cls="nontech"),
        I("The Infrastructure Manager is represented by a project director, assisted by a technical authority for signalling and a technical authority for telecommunications."),
        R("The Supplier SHALL appoint a single project manager, empowered to commit the Supplier, for the whole duration of the contract."),
        R("The Supplier SHALL submit a detailed project schedule within 30 days of contract award and SHALL update it every month.", obs="obs8"),
        R("All project documentation SHALL be delivered in English through the Infrastructure Manager's document management platform, with a unique reference and a revision index.", obs="obs6"),
        R("The Supplier SHALL maintain a configuration baseline of all delivered hardware and software items and SHALL submit every change to it for approval before implementation.", obs="obs4"),
        R("The Supplier SHALL maintain full traceability between the requirements of this specification, the design documents and the test evidence.", obs="obs10", also=["obs37"]),
        R("A project risk register SHALL be maintained by the Supplier and reviewed jointly with the Infrastructure Manager at least once a month.", obs="obs9"),
        R("Any deviation from this specification SHALL be submitted as a formal concession request, with its technical justification and its impact on cost and schedule.", obs="obs5"),
        R("The Supplier SHALL provide a monthly progress report including earned value, the forecast at completion and the status of milestone payments.", obs="obs2"),
    ]),
    ("d1", "2", "Train control", [
        I("Train control is provided by ETCS Level 2 over the whole corridor. The existing automatic warning system is decommissioned section by section as ETCS enters service."),
        H("2.1 Radio block centre"),
        ctx(abs="design", pbs="2.2.1", obs="obs15", cls="tech"),
        I("The radio block centre (RBC) supervises all trains running under ETCS Level 2. Two RBCs are foreseen, located at Arden and at Carrow."),
        R("The RBC SHALL issue movement authorities to every ETCS Level 2 train within its area of control, based on the route status reported by the interlockings."),
        R("Each RBC SHALL manage at least 60 trains simultaneously, with a movement authority update time not exceeding 1.5 seconds.", also=["obs37"]),
        R("Handover of a train between the two RBCs SHALL be performed without any reduction of speed and without driver intervention."),
        R("The RBC SHALL apply temporary speed restrictions entered by the signaller within 10 seconds of their confirmation."),
        R("Loss of communication between an RBC and an interlocking SHALL result in the withdrawal of the movement authorities concerned, and SHALL be alarmed at the control centre."),
        R("The RBC SHALL be built on a redundant architecture such that no single failure interrupts the supervision of trains.", obs="obs30", also=["obs51"]),
        R("The RBC SHALL record all messages exchanged with trains and interlockings and SHALL retain them for at least 30 days.", also=["obs17"]),
        H("2.2 Balises"),
        ctx(abs="design", pbs="x1", obs="obs15", cls="tech"),
        I("Fixed balises provide position references to trains. Their layout is defined by the Supplier on the basis of the track layout drawings supplied in annex."),
        R("Balise groups SHALL be installed so that the position confidence interval of a train never exceeds 5 metres on plain line.", also=["obs47"]),
        R("Each balise SHALL be readable at any train speed up to 200 km/h."),
        R("Balises SHALL remain operational when covered by snow, ballast dust or standing water up to the top of the rail."),
        R("Balise telegrams SHALL be generated from the approved signalling data and SHALL be traceable to it."),
        R("Each balise SHALL carry a permanent identification label readable from the cess.", obs="obs14"),
        H("2.3 Operating modes and degraded operation"),
        ctx(abs="design", pbs="2.2", obs="obs13", cls="tech"),
        I("Degraded operation covers the situations in which radio communication, an RBC or an interlocking is partially unavailable."),
        R("Trains SHALL remain able to run under line-side signals at reduced speed when radio coverage is unavailable on a section."),
        R("The transition from ETCS Level 2 to the fallback level SHALL be announced to the driver at least 15 seconds before the transition point."),
        R("The system SHALL support mixed operation of fitted and unfitted trains throughout the migration period.", also=["obs38", "obs46"]),
        R("A possession taken for maintenance SHALL be protected by the system against the entry of any train, whatever its level of equipment."),
        H("2.4 Cubicles and cabling"),
        ctx(abs="design", pbs="2.2.3", obs="obs14", cls="tech"),
        R("ATC cubicles SHALL be front-access, with a protection rating of at least IP54 in technical rooms."),
        R("All ATC cables SHALL be halogen-free and flame-retardant in accordance with EN 50264."),
        R("Every cable and connector SHALL be labelled at both ends with the reference used in the as-built drawings."),
    ]),
    ("d1", "3", "Interlocking", [
        I("Seven electronic interlockings replace the existing relay installations. Their areas of control are given in annex."),
        H("3.1 Interlocking sub-system"),
        ctx(abs="design", pbs="2.1.1", obs="obs22", cls="tech"),
        I("The interlockings are of a type already approved for use on a main line network. The application of each one is specific to its site."),
        R("Each interlocking SHALL prevent the simultaneous setting of conflicting routes."),
        R("A route SHALL be released only once the train has been proved clear of the last track section of the route."),
        R("Route setting SHALL be completed within 3 seconds of the request under nominal conditions.", also=["obs37"]),
        R("The interlocking SHALL reach a safe state on loss of power supply and SHALL restart without manual reconfiguration.", obs="obs25"),
        R("The interlocking SHALL achieve safety integrity level 4 in accordance with EN 50129.", obs="obs25", also=["obs44"]),
        R("The application data of each interlocking SHALL be produced from the approved scheme plans and control tables."),
        R("Each interlocking SHALL provide a local control panel allowing operation when the link to the control centre is lost.", obs="obs25"),
        H("3.2 Point machines"),
        ctx(abs="design", pbs="2.1.2", obs="obs25", cls="tech"),
        I("One hundred and eighteen sets of points are renewed with new point machines. Clamp locks are retained on the high-speed turnouts at Arden Junction."),
        R("Point machines SHALL throw and lock a set of points within 6 seconds."),
        R("Detection of point position SHALL be continuous and SHALL be lost if the switch rail moves by more than 3 mm from the locked position."),
        R("Point machines SHALL be trailable without damage at speeds up to 40 km/h."),
        R("Point heating SHALL be controlled automatically according to rail temperature and precipitation."),
        R("Each point machine SHALL be replaceable in less than 45 minutes by a team of two.", also=["obs64"]),
        H("3.3 Signals"),
        ctx(abs="design", pbs="2.1.4", obs="obs25", cls="tech"),
        I("Line-side signals are retained at junctions and at station entries as a fallback for unfitted trains."),
        R("Signals SHALL use LED light units with a sighting distance of at least 400 metres in daylight."),
        R("Failure of a signal lamp SHALL be detected and SHALL result in the display of a more restrictive aspect."),
        R("Signal posts SHALL be designed to be lowered for maintenance without possession of the adjacent track.", obs="obs22"),
        R("Each signal SHALL carry a retro-reflective identification plate."),
        H("3.4 Level crossings"),
        ctx(abs="design", pbs="2.1.3", obs="obs22", cls="tech"),
        I("Twenty-two level crossings are fitted with automatic half barriers. Six of them are equipped with obstacle detection."),
        R("A level crossing SHALL close only on the approach of a train, with a warning time of at least 27 seconds before the train arrives."),
        R("Loss of the link between an interlocking and a level crossing SHALL result in the crossing remaining closed to road traffic."),
        R("Obstacle detection SHALL cover the whole crossing surface and SHALL hold the protecting signal at danger while an obstacle is present.", also=["obs42"]),
        R("A barrier failure SHALL be reported to the control centre within 2 seconds."),
        R("Each level crossing SHALL operate for at least 8 hours on its own battery supply.", also=["obs35"]),
        H("3.5 Cubicles and cabling"),
        ctx(abs="design", pbs="2.1.6", obs="obs14", cls="tech"),
        R("Interlocking cubicles SHALL be designed with 20 % spare capacity in input and output modules."),
        R("Trackside cables SHALL be protected against rodents and SHALL be laid in the cable routes defined in annex."),
        R("Cable terminations SHALL be accessible without removing adjacent equipment."),
    ]),
    ("d1", "4", "Train detection", [
        I("Train detection relies on axle counters on plain line and in stations. Track circuits are retained in the two tunnels."),
        H("4.1 Axle counters"),
        ctx(abs="design", pbs="x4", obs="obs25", cls="tech"),
        R("Axle counter sections SHALL detect all rail vehicles with a wheel diameter of 330 mm or more."),
        R("An axle counter section SHALL be reset only under a procedure requiring the cooperation of the signaller and the maintainer."),
        R("The availability of each axle counter section SHALL be at least 99.99 %.", also=["obs51"]),
        R("Axle counter heads SHALL be immune to the eddy current brakes of the rolling stock operated on the line.", also=["obs52"]),
        H("4.2 Track circuits"),
        ctx(abs="design", pbs="x3", obs="obs25", cls="tech"),
        I("The tunnels at Belmont and Carrow are 2.1 km and 3.4 km long. Rail breaks there cannot be found by visual inspection alone."),
        R("Track circuits SHALL be of the jointless audio-frequency type and compatible with the traction return current."),
        R("A broken rail SHALL be detected by the track circuits within the tunnels."),
        R("Track circuit receivers SHALL be housed in the technical rooms and not at the trackside."),
        H("4.3 Hot axle box detection"),
        ctx(abs="design", pbs="x5", obs="obs30", cls="tech"),
        R("Hot axle box detectors SHALL be installed at intervals not exceeding 40 km."),
        R("A hot axle box alarm SHALL be transmitted to the control centre and to the train concerned within 5 seconds.", also=["obs17"]),
        R("Detectors SHALL measure bearing temperature with an accuracy of 3 °C at speeds up to 200 km/h."),
    ]),
    ("d1", "5", "Supervision and control centre", [
        I("The corridor is operated from a single control centre at Carrow, with a backup centre at Arden."),
        H("5.1 Traffic management"),
        ctx(abs="design", pbs="2.6.1", obs="obs27", cls="tech"),
        I("Six signaller positions and two supervisor positions are foreseen at Carrow. The backup centre has four positions."),
        R("The traffic management system SHALL display the position and identity of every train with a refresh period not exceeding 1 second."),
        R("Automatic route setting SHALL follow the timetable and SHALL be overridable by the signaller at any time."),
        R("The system SHALL detect timetable conflicts at least 10 minutes ahead and SHALL propose a resolution to the signaller.", obs="obs21"),
        R("Switchover from the main to the backup control centre SHALL be completed in less than 60 seconds without loss of train describer data.", obs="obs17", also=["obs18", "obs37"]),
        R("Each signaller workstation SHALL control the whole corridor, subject to the access rights of the operator.", obs="obs20"),
        R("All operator commands SHALL be logged with the operator identity and a time stamp accurate to 100 milliseconds.", also=["obs55"]),
        R("The system SHALL replay any period of the last 12 months of operation on request."),
        H("5.2 SCADA"),
        ctx(abs="design", pbs="2.6.2", obs="obs17", cls="tech"),
        R("The SCADA SHALL monitor the status of all signalling power supplies, technical rooms and telecom nodes."),
        R("Alarms SHALL be classified in three priority levels and SHALL be acknowledged individually."),
        R("The SCADA SHALL exchange data with the power supply control system using IEC 60870-5-104."),
        H("5.3 Data platform"),
        ctx(abs="design", pbs="2.6.4", obs="obs20", cls="tech"),
        I("The Infrastructure Manager operates its own asset management system, which consumes the diagnostic data produced by the signalling system."),
        R("Diagnostic data from all signalling sub-systems SHALL be stored for at least 5 years on the data platform."),
        R("The data platform SHALL expose a documented interface allowing the Infrastructure Manager to extract raw data without the Supplier's assistance.", also=["obs54"]),
        R("Storage capacity SHALL be sized for a 30 % growth in the volume of data over the service life."),
        H("5.4 Security management"),
        ctx(abs="design", pbs="2.6.3", obs="obs19", cls="tech"),
        R("Access to technical rooms SHALL be controlled by badge readers reporting to the security management system."),
        R("Video surveillance SHALL cover the entrance of every technical room and every level crossing."),
    ]),
    ("d1", "6", "Telecommunications and networks", [
        I("Train-to-ground communication uses the railway mobile radio network, which is renewed under this contract."),
        H("6.1 Radio"),
        ctx(abs="design", pbs="4.2.2", obs="obs19", cls="tech"),
        I("Thirty-one base station sites exist today. Their reuse is permitted where the coverage study confirms it."),
        R("Radio coverage SHALL be continuous along the whole corridor, including the tunnels and the depot approach."),
        R("The radio network SHALL have no single point of failure between two consecutive base stations."),
        R("The end-to-end transfer delay of an ETCS message SHALL not exceed 500 milliseconds for 99 % of messages.", also=["obs15"]),
        R("Voice communication between drivers and signallers SHALL have priority over all other voice calls.", pbs="4.2.1"),
        R("Radio masts SHALL be designed for a wind speed of 160 km/h.", pbs="4.2.1", also=["obs47"]),
        H("6.2 Networks"),
        ctx(abs="design", pbs="4.3.3", obs="obs18", cls="tech"),
        R("The backbone network SHALL be built as a ring so that a single fibre cut does not interrupt any service."),
        R("Network reconfiguration after a failure SHALL be completed within 50 milliseconds."),
        R("Signalling traffic SHALL be segregated from all other traffic on the wayside network.", pbs="4.3.2", also=["obs54"]),
        R("Network equipment SHALL be synchronised to a common time reference with an accuracy better than 1 millisecond."),
        R("Each wayside network node SHALL provide at least 25 % of spare ports.", pbs="4.3.2"),
    ]),
    ("d1", "7", "Power supply and technical rooms", [
        I("Signalling equipment is supplied from the Infrastructure Manager's medium-voltage network through dedicated transformers."),
        H("7.1 Signalling power supply"),
        ctx(abs="design", pbs="7.1", obs="obs35", cls="tech"),
        R("Each technical room SHALL be equipped with an uninterruptible power supply providing 4 hours of autonomy at full load.", also=["obs51"]),
        R("Changeover between the two incoming supplies SHALL be automatic and SHALL not disturb the equipment supplied."),
        R("The power supply SHALL be sized with a 30 % margin on the calculated load."),
        R("Battery condition SHALL be monitored continuously and reported to the SCADA."),
        H("7.2 Technical rooms"),
        ctx(abs="design", pbs="5.3", obs="obs14", cls="tech"),
        I("Nineteen technical rooms are built or refurbished. Their civil works are part of a separate lot, coordinated by the Infrastructure Manager."),
        R("The temperature of technical rooms SHALL be maintained between 15 °C and 28 °C by redundant air-conditioning units."),
        R("Fire detection SHALL be installed in every technical room and SHALL report to the building management system.", pbs="5.2"),
        R("Technical rooms SHALL be laid out so that any cubicle can be replaced without dismantling the building envelope."),
    ]),
    # ------------------------------------------------------------------ document 2
    ("d2", "8", "Installation and site works", [
        I("Works are carried out under traffic, during night possessions of 5 hours and four weekend blockades per year."),
        H("8.1 Site organisation"),
        ctx(abs="installation", pbs="2", obs="obs46", cls="nontech"),
        I("The possession calendar for the first two years is given in annex. Later years are agreed annually."),
        R("The Supplier SHALL submit a possession plan at least 12 weeks before each period of works."),
        R("The line SHALL be handed back to operation at the end of each possession with all safety systems in service.", also=["obs44", "obs38"]),
        R("The Supplier SHALL appoint a site manager present on site during every shift."),
        R("All staff working on or near the track SHALL hold the Infrastructure Manager's track safety certification.", obs="obs45"),
        R("Site installations SHALL be removed and the land reinstated within 3 months of completion of the works."),
        H("8.2 Cable routes and civil works"),
        ctx(abs="installation", pbs="x8", obs="obs45", cls="nontech"),
        I("About 140 km of cable route are concerned, of which 60 km are new."),
        R("Cable routes SHALL be installed with 30 % spare capacity.", obs="obs47"),
        R("Under-track crossings SHALL be made by directional drilling, without opening the track bed."),
        R("Foundations for signals and location cases SHALL be designed for the ground conditions given in the geotechnical report.", pbs="8", obs="obs47"),
        R("Cables SHALL be pulled with tension monitoring and the records SHALL be kept in the installation file."),
        R("As-built drawings SHALL be delivered within 30 days of the completion of each section.", obs="obs47", also=["obs6"]),
        R("The existing cable routes SHALL be reused wherever their condition allows, after a joint survey."),
        H("8.3 Removal of existing equipment"),
        ctx(abs="installation", pbs="2", obs="obs46", cls="nontech"),
        R("Redundant signalling equipment SHALL be removed within 6 months of commissioning of the new system."),
        R("Recovered equipment designated by the Infrastructure Manager SHALL be delivered to the Eastfield depot."),
        R("Removed materials SHALL be disposed of through approved channels, with traceability of hazardous waste.", obs="obs45"),
    ]),
    ("d2", "9", "Verification, validation, testing and commissioning", [
        I("Verification and validation follow the life cycle of EN 50126. The test strategy is submitted for approval with the preliminary design."),
        H("9.1 Verification and validation"),
        ctx(abs="verification-and-validation", pbs="2", obs="obs37", cls="nontech"),
        R("The Supplier SHALL deliver a verification and validation plan covering every requirement of this specification."),
        R("Each requirement SHALL be verified by test, analysis, inspection or demonstration, the method being agreed beforehand."),
        R("Factory acceptance tests SHALL be witnessed by the Infrastructure Manager, with 4 weeks' notice."),
        R("A system integration laboratory representative of the corridor SHALL be available from the detailed design phase until the end of the warranty period.", pbs="6.3.5", also=["obs14"]),
        R("Interlocking application data SHALL be validated on a simulator before any site test.", pbs="6.3.5", also=["obs22"]),
        R("Regression tests SHALL be performed after every software change, and their extent SHALL be justified."),
        H("9.2 Testing and commissioning"),
        ctx(abs="test-and-commissioning", pbs="2", obs="obs38", cls="nontech"),
        I("The corridor is commissioned in five sections, from south to north. The staging plan is given in annex."),
        R("Site acceptance tests SHALL be carried out on each section before it is put into service.", obs="obs39"),
        R("Commissioning of a section SHALL be reversible until the end of the first weekend of operation."),
        R("The Supplier SHALL provide the test trains, drivers and pilots required for dynamic tests.", also=["obs46"]),
        R("A trial running period of 4 weeks without passengers SHALL precede the entry into service of ETCS Level 2."),
        R("Every test SHALL be recorded in a test report signed by both parties within 5 working days.", obs="obs39"),
        R("Open points remaining at commissioning SHALL be classified and closed within the periods agreed for each class.", obs="obs39"),
        R("The Supplier SHALL keep a commissioning team on call 24 hours a day during the first 8 weeks of operation."),
    ]),
    ("d2", "10", "Safety, reliability and electromagnetic compatibility", [
        I("The safety demonstration is built on the generic approvals of the products and on the specific application safety case of the corridor."),
        H("10.1 Safety"),
        ctx(abs="safety", pbs="2", obs="obs44", cls="tech"),
        R("The Supplier SHALL deliver a safety case demonstrating SIL 4 for all train protection functions."),
        R("A hazard log SHALL be opened at the start of the project and maintained until the end of the warranty period.", obs="obs42"),
        R("The Supplier SHALL appoint an independent safety assessor accredited to ISO/IEC 17020.", obs="obs43", also=["obs40"]),
        R("Safety-related application conditions exported to the operator and to the maintainer SHALL be listed in a dedicated document.", obs="obs42"),
        R("Every modification of safety-related software SHALL be subject to an impact analysis approved by the safety assurance manager."),
        R("The tolerable hazard rate of each safety function SHALL be allocated to sub-systems and demonstrated.", obs="obs42"),
        H("10.2 Reliability, availability and maintainability"),
        ctx(abs="ram", pbs="2", obs="obs51", cls="tech"),
        I("Reliability targets are expressed for the signalling system as a whole. Their allocation to sub-systems is the Supplier's responsibility."),
        R("The availability of the signalling system SHALL be at least 99.95 %, measured over each calendar year."),
        R("Signalling failures SHALL not cause more than 300 minutes of cumulated train delay per year."),
        R("The mean time to restore service after a failure SHALL not exceed 60 minutes, travel time included.", also=["obs64"]),
        R("A reliability demonstration SHALL be conducted over the first 24 months of operation."),
        R("The Supplier SHALL deliver a failure mode, effects and criticality analysis for every line-replaceable unit."),
        H("10.3 Electromagnetic compatibility"),
        ctx(abs="emc", pbs="2", obs="obs52", cls="tech"),
        R("Signalling equipment SHALL comply with EN 50121-4 for emission and immunity."),
        R("The Supplier SHALL demonstrate compatibility between train detection and every type of rolling stock authorised on the line."),
        R("An EMC management plan SHALL be submitted with the preliminary design."),
        R("Earthing and bonding SHALL comply with EN 50122-1."),
    ]),
    ("d2", "11", "Cybersecurity", [
        I("The signalling system is classified as critical infrastructure. Cybersecurity is addressed over the whole life cycle in accordance with IEC 62443."),
        H("11.1 Protection"),
        ctx(abs="cybersecurity", pbs="12.2", obs="obs54", cls="tech"),
        R("The system SHALL achieve security level 3 of IEC 62443-3-3 for the zones hosting safety functions."),
        R("All remote access SHALL go through a single secured gateway with multi-factor authentication.", also=["obs18"]),
        R("Removable media ports SHALL be disabled by default on all operational equipment.", obs="obs55"),
        R("User accounts SHALL be personal, and every privileged action SHALL be traceable to an individual.", obs="obs55"),
        R("Network zones SHALL be separated by firewalls configured on a deny-by-default basis.", pbs="4.4"),
        H("11.2 Management"),
        ctx(abs="cybersecurity", pbs="12.2", obs="obs53", cls="nontech"),
        I("The Infrastructure Manager's security operations centre monitors the system once in service. The Supplier provides the interfaces it needs."),
        R("Security patches SHALL be qualified and made available within 90 days of their publication by the original vendor."),
        R("The Supplier SHALL deliver a cybersecurity risk assessment and SHALL update it at each major release."),
        R("Security events SHALL be collected centrally and retained for at least 12 months.", pbs="12.1", obs="obs55"),
        R("A penetration test SHALL be carried out by an independent body before the entry into service.", also=["obs37"]),
    ]),
    ("d2", "12", "Quality, environment and sourcing", [
        H("12.1 Quality"),
        ctx(abs="quality", pbs="2", obs="obs40", cls="nontech"),
        I("The quality requirements apply to the Supplier and to every subcontractor contributing to the design, manufacture or installation of safety-related equipment."),
        R("The Supplier SHALL operate a quality management system certified to ISO 9001 and ISO 22163."),
        R("A project quality plan SHALL be submitted within 60 days of contract award."),
        R("Non-conformities SHALL be recorded, analysed and closed, with a monthly status sent to the Infrastructure Manager."),
        R("The Infrastructure Manager SHALL be entitled to audit the Supplier and its subcontractors with 10 days' notice."),
        H("12.2 Environment"),
        ctx(abs="eco-design", pbs="2", obs="obs58", cls="nontech"),
        R("The Supplier SHALL provide a life cycle assessment of the main equipment in accordance with ISO 14040."),
        R("Equipment SHALL be free of the substances listed in the restricted substances annex."),
        R("At least 90 % of the mass of delivered equipment SHALL be recoverable at end of life."),
        H("12.3 Sourcing"),
        ctx(abs="sourcing", pbs="2", obs="obs60", cls="nontech"),
        R("The Supplier SHALL declare all subcontractors performing more than 5 % of the contract value."),
        R("Components subject to obsolescence SHALL be identified, with a monitoring and last-buy process."),
        R("The origin of safety-related components SHALL be traceable to the manufacturing batch."),
    ]),
    ("d2", "13", "Maintenance, warranty and services", [
        I("First-line maintenance is performed by the Infrastructure Manager's staff, trained by the Supplier. The Supplier provides second-line and third-line support."),
        H("13.1 Maintenance"),
        ctx(abs="warranty", pbs="6.3.1", obs="obs64", cls="nontech"),
        R("The diagnostic and maintenance system SHALL locate any failure to the line-replaceable unit.", also=["obs20"]),
        R("Preventive maintenance SHALL not require more than 2 possessions per year and per section."),
        R("The Supplier SHALL deliver maintenance manuals for every equipment type, in English, 3 months before commissioning."),
        R("Special tools and test benches required for maintenance SHALL be delivered with the first section.", pbs="6.3.6"),
        R("The Supplier SHALL train 40 maintainers and 60 signallers before the entry into service.", obs="obs62", also=["obs38"]),
        R("Spare parts for 2 years of operation SHALL be delivered before commissioning, on the basis of a justified list.", pbs="6.3.6"),
        H("13.2 Warranty and support"),
        ctx(abs="warranty", pbs="2", obs="obs66", cls="nontech"),
        I("The warranty applies section by section. Its conditions are set out in the contract; this section states the technical obligations that go with it."),
        R("The warranty period SHALL be 36 months from the commissioning of each section."),
        R("During the warranty period, a failed unit SHALL be repaired or replaced within 15 calendar days."),
        R("The Supplier SHALL guarantee the availability of spare parts and support for 25 years.", obs="obs62"),
        R("A hotline staffed by qualified engineers SHALL be available 24 hours a day during the warranty period."),
        R("Software support SHALL include corrective releases at no charge during the warranty period."),
        R("The Supplier SHALL hand over to the Infrastructure Manager all the data and tools needed to modify the application data.", obs="obs62"),
    ]),
]


def load_keys():
    src = Path(KEYS_FILE).read_text(encoding="utf-8")
    keys = json.loads(src[src.index("{"):src.rindex("}") + 1])
    on_product = lambda e: PRODUCT_KEY in (e.get("products") or [])
    return (
        {a["id"]: a for a in keys["abs"] if on_product(a)},
        {p["id"]: p for p in keys["pbs"] if on_product(p)},
        {o["id"]: o for o in keys["obs"] if on_product(o)},
    )


def pbs_label(e):
    # same reading as the Allocation screen's PBS_LABEL: id-less rows ("x…") show their name alone
    return ("" if e["id"].startswith("x") else e["id"] + " · ") + e["name"]


def main():
    ABS, PBS, OBS = load_keys()
    rng = random.Random(SEED)
    known_people = {"m_sig", "sup"} | {p[0] for p in PEOPLE}

    def need(table, key, what):
        if key not in table:
            sys.exit(f"build_tender.py: {what} '{key}' is not in the {PRODUCT_KEY} key — fix the content or rebuild keys.js")
        return table[key]

    # ---- 1. walk the content: ids in document order, one scheme for every kind of block
    seq = 0
    def next_id():
        nonlocal seq
        seq += 1
        return f"{ID_PREFIX}-{seq:04d}"

    sections, reqs, infos = [], [], []
    for n, (doc, num, title, items) in enumerate(SECTIONS, 1):
        sec = {"id": f"s{n}", "docId": doc, "num": num, "title": title, "hid": next_id(), "blocks": []}
        cur = {}
        for it in items:
            kind = it[0]
            if kind == "ctx":
                cur = dict(it[1])
            elif kind == "h":
                sec["blocks"].append({"id": next_id(), "kind": "heading", "level": 2, "text": it[1]})
            elif kind == "i":
                b = {"id": next_id(), "kind": "text", "text": it[1]}
                sec["blocks"].append(b); infos.append(b)
            else:
                kw = {**cur, **it[2]}
                roles = [kw["obs"]] + list(kw.get("also", []))
                a, p = need(ABS, kw["abs"], "ABS"), need(PBS, kw["pbs"], "PBS")
                for r in roles:
                    need(OBS, r, "role")
                    if r not in ROLE_PEOPLE:
                        sys.exit(f"build_tender.py: nobody is listed for role '{r}' in ROLE_PEOPLE")
                b = {"id": next_id(), "kind": "requirement", "text": it[1]}
                sec["blocks"].append(b)
                reqs.append({"b": b, "cls": kw["cls"], "abs": a, "pbs": p, "roles": roles})
        sections.append(sec)

    # ---- 2. the starting states
    singles = [r for r in reqs if len(r["roles"]) == 1]
    multis = [r for r in reqs if len(r["roles"]) > 1]
    no_role = rng.sample(singles, N_NO_ROLE)
    no_chain = set(id(r) for r in rng.sample(no_role, N_NO_CHAIN))
    rest = [r for r in reqs if r not in no_role]
    low = rng.sample(rest, N_LOW_TYPE + N_LOW_CLASS + N_LOW_CHAIN)
    low_type, low_class = low[:N_LOW_TYPE], low[N_LOW_TYPE:N_LOW_TYPE + N_LOW_CLASS]
    low_chain = {id(r): rng.choice(["abs", "pbs", "obs"]) for r in low[N_LOW_TYPE + N_LOW_CLASS:]}
    nobody_single = rng.sample([r for r in singles if r not in no_role], N_NOBODY_SINGLE)
    nobody_multi = {id(r): rng.randrange(len(r["roles"])) for r in rng.sample(multis, N_NOBODY_MULTI)}

    level = lambda: "medium" if rng.random() < 0.25 else "high"
    sure = lambda lo: rng.randint(lo, 98)       # a derivation the model stands by
    unsure = lambda: rng.randint(52, 74)        # under the 75 % threshold: To review

    for r in reqs:
        b = r["b"]
        weak = low_chain.get(id(r))
        conf = {k: (unsure() if weak == k else sure(lo)) for k, lo in (("abs", 80), ("pbs", 78), ("obs", 76))}
        people = [rng.choice(ROLE_PEOPLE[role]) for role in r["roles"]]
        for p in people:
            assert p in known_people, p
        if r in nobody_single:
            people = [None]
        if id(r) in nobody_multi:
            people[nobody_multi[id(r)]] = None
        obs = [{"v": OBS[role]["title"], "id": role, "c": conf["obs"] if i == 0 else sure(76)} for i, role in enumerate(r["roles"])]
        b.update({
            "branchStatus": "proposed",
            "tech": r["cls"], "techAI": r in low_class,
            "perim": ["sig"], "perimAI": False,
            "abs": {"v": r["abs"]["label"], "id": r["abs"]["id"], "c": conf["abs"]},
            "pbs": {"v": pbs_label(r["pbs"]), "id": r["pbs"]["id"], "c": conf["pbs"]},
            "obs": obs[0], "manager": people[0],
            "domain": r["abs"]["label"],            # what the table's ABS cell reads
            "status": "suggested", "comments": 0,
            "charLevel": {"type": level(), "class": level()},
        })
        if r in low_type:
            b["typeAI"] = True
        if r in no_role:
            b.update({"obs": None, "manager": None})
            if id(r) in no_chain:
                b.update({"abs": None, "pbs": None, "domain": ""})
        if len(obs) > 1:
            # one sub-system, several roles: each role is an allocation with its own person (DEC-060)
            b["branches"] = [{
                "typology": "sig", "label": "SIG", "manager": people[0], "branchStatus": "proposed", "compliance": "pending",
                "abs": b["abs"], "pbs": b["pbs"], "obs": obs[0],
                "teams": [{"team": None, "manager": people[i], "branchStatus": "proposed", "compliance": "pending", "obs": o}
                          for i, o in enumerate(obs)],
            }]
        # key order: text last, as in the hand-written tenders
        b["text"] = b.pop("text")

    low_info = set(id(b) for b in rng.sample(infos, N_LOW_TYPE_INFO))
    for b in infos:
        b["charLevel"] = {"type": level()}
        if id(b) in low_info:
            b["typeAI"] = True
        b["text"] = b.pop("text")

    people_out = [{"id": pid, "name": name, "role": role, "system": "sig",
                   "init": "".join(w[0] for w in name.split())[:2].upper(),
                   "color": PALETTE[int(pid[3:]) % len(PALETTE)]} for pid, name, role in PEOPLE]

    tender = {"docs": DOCS, "people": people_out, "sections": sections}
    payload = json.dumps({TENDER_ID: tender}, ensure_ascii=False, separators=(",", ":"))
    Path(OUT).write_text(
        "/* tenders.js — generated by build_tender.py. Fictional content. Do not edit by hand. */\n"
        f"window.SRM_TENDERS = {payload};\n", encoding="utf-8")

    n_head = sum(1 for s in sections for b in s["blocks"] if b["kind"] == "heading") + len(sections)
    slots = sum(len(r["roles"]) for r in reqs if r not in no_role)
    print(f"Wrote {OUT}: {seq} blocks — {len(reqs)} requirements, {len(infos)} information, {n_head} headings.")
    print(f"  {len(multis)} requirements with several roles · {slots} roles in all · "
          f"{N_NOBODY_SINGLE + N_NOBODY_MULTI} with nobody in charge")
    print(f"  {N_NO_ROLE} with no role (Incomplete) · {len(low)} with a low-confidence proposal (To review)")


if __name__ == "__main__":
    main()
