#!/usr/bin/env python3
"""Smart Req notification emails: email-safe HTML, plain text and .eml samples.

    python3 proposals/notifications/emails/build_emails.py

For each email of content.py, writes next to this script <slug>.html (email-safe HTML),
<slug>.txt (the plain-text part, readable on its own) and <slug>.eml (multipart/alternative
with both parts and the real headers: double-click it to open it in Outlook or Apple Mail),
plus index.html, a viewer. Stdlib only, fictional data, not part of build_merge.py.
Rules: docs/current/NOTIFICATIONS.md, section 6.

Email HTML rules applied here: tables for layout (role="presentation"), every style inline,
a 600px column (an Outlook-only ghost table holds it where max-width is ignored), no image,
no web font, no tracking, a VML button for Outlook for Windows, a hidden preview line,
dark mode as progressive enhancement (prefers-color-scheme, Outlook.com [data-ogsc]/[data-ogsb]).
"""
import html
import json
import re
import sys
import textwrap
from datetime import datetime, timedelta, timezone
from email.message import EmailMessage
from email.utils import format_datetime, formataddr
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from content import EMAILS  # noqa: E402

PARIS = timezone(timedelta(hours=1))  # CET: every sample is dated in November or December
FONT = "'Segoe UI',-apple-system,BlinkMacSystemFont,Roboto,Helvetica,Arial,sans-serif"
MONO = "Consolas,'SF Mono',Menlo,'Courier New',monospace"
# Light colours: the prototype's light-theme tokens (--bg, --panel, --line, --text, --text-2,
# --text-3, --accent, --brand-red). Dark colours, in CSS below: its dark-theme tokens.
# LINK is the one colour of its own: the light --accent (navy) is too close to the text.
BG, CARD, LINE = "#F4F5FA", "#FFFFFF", "#E1E3EE"
TEXT, TEXT2, TEXT3 = "#1E3246", "#4A5A6E", "#637187"
ACCENT, LINK, RED = "#0B294A", "#2456C5", "#E4002B"
WRAP = 72  # plain-text line length

DARK_QUERY = "@media (prefers-color-scheme:dark)"  # index.html swaps it to preview dark mode
CSS = """
:root{color-scheme:light dark;supported-color-schemes:light dark}
body{margin:0;padding:0;width:100%!important;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%}
table,td{border-collapse:collapse;mso-table-lspace:0pt;mso-table-rspace:0pt}
a[x-apple-data-detectors]{color:inherit!important;text-decoration:none!important;font-size:inherit!important;font-family:inherit!important;font-weight:inherit!important;line-height:inherit!important}
@media only screen and (max-width:620px){
.sr-pad{padding-left:20px!important;padding-right:20px!important}
.sr-h1{font-size:20px!important;line-height:28px!important}
}
@media (prefers-color-scheme:dark){
.sr-bg{background-color:#071A30!important}
.sr-card{background-color:#0B294A!important;border-color:#1F3E5F!important}
.sr-text{color:#EEF1F8!important}
.sr-text2{color:#AAB6C6!important}
.sr-text3,.sr-text3 a{color:#8B9AAD!important}
.sr-line{border-color:#1F3E5F!important}
.sr-link{color:#8FB0FF!important}
.sr-id{color:#C9D6EA!important}
.sr-quote{background-color:#143556!important;border-color:#4C82FF!important}
.sr-btn{background-color:#4C82FF!important;border-color:#4C82FF!important;color:#071A30!important}
}
[data-ogsb] .sr-bg{background-color:#071A30!important}
[data-ogsb] .sr-card{background-color:#0B294A!important}
[data-ogsb] .sr-quote{background-color:#143556!important}
[data-ogsb] .sr-btn{background-color:#4C82FF!important}
[data-ogsc] .sr-text{color:#EEF1F8!important}
[data-ogsc] .sr-text2{color:#AAB6C6!important}
[data-ogsc] .sr-text3,[data-ogsc] .sr-text3 a{color:#8B9AAD!important}
[data-ogsc] .sr-link{color:#8FB0FF!important}
[data-ogsc] .sr-id{color:#C9D6EA!important}
[data-ogsc] .sr-btn{color:#071A30!important}
""".strip()
assert DARK_QUERY in CSS

HEAD = """<!DOCTYPE html>
<html lang="en" dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="x-apple-disable-message-reformatting">
<meta name="format-detection" content="telephone=no, date=no, address=no, email=no, url=no">
<meta name="color-scheme" content="light dark">
<meta name="supported-color-schemes" content="light dark">
<title>@@TITLE@@</title>
<!--[if mso]>
<noscript><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml></noscript>
<style>table,td,p,a,span,h1{font-family:'Segoe UI',Arial,sans-serif !important;}</style>
<![endif]-->
<style>
@@CSS@@
</style>
</head>
"""

# Keeps the start of the body out of the inbox preview line.
PREHEADER_FILL = "&#847;&zwnj;&nbsp;" * 60


# ----------------------------------------------------------------------------- helpers
def esc(s, attr=False):
    return html.escape(s, quote=attr)


def inline(s):
    """Content string -> HTML: **bold**, [[SRM-00042]] requirement ID."""
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r'<strong style="font-weight:600;">\1</strong>', s)
    return re.sub(r"\[\[(.+?)\]\]", lambda m: (
        f'<span class="sr-id" style="font-family:{MONO};font-size:13px;font-weight:600;'
        f'color:{ACCENT};white-space:nowrap;">{m.group(1)}</span>'), s)


def plain(s):
    return re.sub(r"\[\[(.+?)\]\]", r"\1", s.replace("**", ""))


def wrap(s, first="", rest=""):
    return textwrap.fill(plain(s), WRAP, initial_indent=first, subsequent_indent=rest,
                         break_long_words=False, break_on_hyphens=False)


def st(size, lh, color=TEXT, weight=None, m="0"):
    w = f"font-weight:{weight};" if weight else ""
    return (f"margin:{m};font-family:{FONT};font-size:{size}px;line-height:{lh}px;"
            f"color:{color};{w}mso-line-height-rule:exactly;")


def link(label, url, cls="sr-link", color=LINK):
    return (f'<a class="{cls}" href="{esc(url, True)}" style="color:{color};'
            f'text-decoration:underline;">{esc(label)}</a>')


def table(rows):
    return ('<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" '
            f'style="width:100%;">{rows}</table>')


def pad(inner, padding):
    return table(f'<tr><td style="padding:{padding};">{inner}</td></tr>')


def closing_line():
    return (f'<tr><td colspan="2" class="sr-line" style="border-top:1px solid {LINE};'
            'font-size:1px;line-height:1px;">&nbsp;</td></tr>')


# ------------------------------------------------------------------------------ blocks
# Each block returns (html, plain-text lines).
def b_eyebrow(s):
    return f'<p class="sr-text2" style="{st(13, 19, TEXT2, 600, "0 0 6px 0")}">{inline(s)}</p>', [plain(s), ""]


def b_h1(s):
    return (f'<h1 class="sr-text sr-h1" style="{st(22, 30, TEXT, 600, "0 0 14px 0")}">{inline(s)}</h1>',
            [wrap(s), ""])


def b_p(s):
    return f'<p class="sr-text" style="{st(15, 23, TEXT, None, "0 0 16px 0")}">{inline(s)}</p>', [wrap(s), ""]


def b_muted(s):
    return f'<p class="sr-text2" style="{st(14, 21, TEXT2, None, "0 0 14px 0")}">{inline(s)}</p>', [wrap(s), ""]


def b_quote(q):
    cell = (f'<td class="sr-quote" style="border-left:3px solid {ACCENT};background-color:{BG};'
            'padding:12px 16px;">'
            f'<p class="sr-text" style="{st(15, 23)}">{inline(q["text"])}</p>'
            f'<p class="sr-text2" style="{st(13, 19, TEXT2, None, "4px 0 0 0")}">{esc(q["by"])}</p></td>')
    lines = [wrap(q["text"], "> ", "> "), "> — " + q["by"], ""]
    return pad(table(f"<tr>{cell}</tr>"), "0 0 18px 0"), lines


def row_html(text, label, url, waiting=False):
    cls, color, lcls, lcolor = ("sr-text3", TEXT3, "sr-text3", TEXT3) if waiting else ("sr-text", TEXT, "sr-link", LINK)
    return ('<tr><td style="padding:12px 0 0 0;">'
            f'<p class="{cls}" style="{st(15, 22, color)}">{inline(text)}</p>'
            f'<p class="{cls}" style="{st(14, 20, color, None, "3px 0 0 0")}">{link(label, url, lcls, lcolor)}</p>'
            '</td></tr>')


def row_text(text, label, url):
    return [wrap(text, "* ", "  "), f"  {label}: {url}"]


def b_group(g):
    """One tender in a summary: title, context, new rows, then grey 'Still waiting' rows."""
    rows = (f'<tr><td class="sr-line" style="border-top:1px solid {LINE};padding:20px 0 0 0;">'
            f'<p class="sr-text" style="{st(16, 22, TEXT, 600)}">{inline(g["title"])}</p>'
            f'<p class="sr-text2" style="{st(13, 19, TEXT2, None, "2px 0 0 0")}">{inline(g["context"])}</p>'
            '</td></tr>')
    lines = [plain(g["title"]), plain(g["context"]), ""]
    for r in g["rows"]:
        rows += row_html(*r)
        lines += row_text(*r) + [""]
    if g.get("waiting"):
        rows += ('<tr><td style="padding:20px 0 0 0;">'
                 f'<p class="sr-text3" style="{st(13, 18, TEXT3, 600)}">Still waiting</p></td></tr>')
        lines.append("Still waiting")
        for r in g["waiting"]:
            rows += row_html(*r, waiting=True)
            lines += row_text(*r)
        lines.append("")
    return pad(table(rows), "0 0 22px 0"), lines


def b_rows(items):
    """Facts with a link each, between thin rules (processing emails)."""
    rows, lines = "", []
    for text, label, url in items:
        rows += (f'<tr><td colspan="2" class="sr-line" style="border-top:1px solid {LINE};padding:12px 0;">'
                 f'<p class="sr-text" style="{st(15, 22)}">{inline(text)}</p>'
                 f'<p style="{st(14, 20, LINK, None, "3px 0 0 0")}">{link(label, url)}</p></td></tr>')
        lines += row_text(text, label, url) + [""]
    return pad(table(rows + closing_line()), "0 0 18px 0"), lines


def b_reqs(reqs):
    """Requirements: ID, text, then a grey line (age, place)."""
    rows, lines = "", []
    for rid, text, meta in reqs:
        rows += (f'<tr><td class="sr-line sr-id" style="border-top:1px solid {LINE};padding:11px 14px 11px 0;'
                 f'vertical-align:top;white-space:nowrap;font-family:{MONO};font-size:13px;line-height:21px;'
                 f'font-weight:600;color:{ACCENT};">{esc(rid)}</td>'
                 f'<td class="sr-line" style="border-top:1px solid {LINE};padding:11px 0;vertical-align:top;">'
                 f'<p class="sr-text" style="{st(14, 21)}">{inline(text)}</p>'
                 f'<p class="sr-text2" style="{st(13, 19, TEXT2, None, "2px 0 0 0")}">{inline(meta)}</p></td></tr>')
        indent = " " * (len(rid) + 2)
        lines += [wrap(f"{rid}  {text}", "", indent), indent + plain(meta)]
    return pad(table(rows + closing_line()), "0 0 18px 0"), lines + [""]


def b_facts(facts):
    rows = "".join(
        f'<tr><td class="sr-text2" style="padding:3px 16px 3px 0;vertical-align:top;white-space:nowrap;'
        f'font-family:{FONT};font-size:13px;line-height:20px;color:{TEXT2};">{esc(k)}</td>'
        f'<td class="sr-text" style="padding:3px 0;vertical-align:top;width:100%;font-family:{FONT};'
        f'font-size:14px;line-height:20px;color:{TEXT};">{inline(v)}</td></tr>' for k, v in facts)
    width = max(len(k) for k, _ in facts) + 2
    return pad(table(rows), "0 0 18px 0"), [f"{k + ':':<{width}}{plain(v)}" for k, v in facts] + [""]


def b_button(b):
    """VML rounded rectangle for Outlook for Windows (Word engine), a padded link elsewhere."""
    label, url = b
    u = esc(url, True)
    width = max(160, (len(label) * 9 + 50) // 10 * 10)
    vml = ('<!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" '
           f'xmlns:w="urn:schemas-microsoft-com:office:word" href="{u}" '
           f'style="height:44px;v-text-anchor:middle;width:{width}px;" arcsize="14%" '
           f'strokecolor="{ACCENT}" fillcolor="{ACCENT}"><w:anchorlock/>'
           '<center style="color:#FFFFFF;font-family:\'Segoe UI\',Arial,sans-serif;font-size:15px;'
           f'font-weight:bold;">{esc(label)}</center></v:roundrect><![endif]-->')
    anchor = ('<!--[if !mso]><!-->'
              f'<a class="sr-btn" href="{u}" style="display:inline-block;background-color:{ACCENT};'
              f'border:1px solid {ACCENT};border-radius:6px;color:#FFFFFF;font-family:{FONT};font-size:15px;'
              'font-weight:600;line-height:20px;padding:12px 22px;text-decoration:none;'
              f'-webkit-text-size-adjust:none;">{esc(label)}</a><!--<![endif]-->')
    return pad(vml + anchor, "4px 0 20px 0"), [f"{label}: {url}", ""]


BLOCKS = dict(eyebrow=b_eyebrow, h1=b_h1, p=b_p, muted=b_muted, quote=b_quote, group=b_group,
              rows=b_rows, reqs=b_reqs, facts=b_facts, button=b_button)


def footer(items):
    out, lines = "", ["-- "]
    for it in items:
        if isinstance(it, tuple):
            label, url, after = it
            out += (f'<p class="sr-text3" style="{st(12, 18, TEXT3, None, "0 0 8px 0")}">'
                    f'{link(label, url, "sr-text3", TEXT3)}{esc(after)}</p>')
            lines.append(wrap(f"{label}{after}: {url}"))
        else:
            out += f'<p class="sr-text3" style="{st(12, 18, TEXT3, None, "0 0 8px 0")}">{inline(it)}</p>'
            lines.append(wrap(it))
    return out, lines


WORDMARK = ('<table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr>'
            f'<td class="sr-text" style="border-left:4px solid {RED};padding:0 0 0 8px;font-family:{FONT};'
            f'font-size:15px;line-height:20px;font-weight:700;color:{TEXT};mso-line-height-rule:exactly;">'
            'Smart Req</td></tr></table>')


# ------------------------------------------------------------------------------ build
def build(e):
    parts, text = [], ["Smart Req", ""]
    for kind, data in e["blocks"]:
        h, t = BLOCKS[kind](data)
        parts.append(h)
        text += t
    foot_html, foot_text = footer(e["footer"])
    subject = e["subject"]
    doc = (HEAD.replace("@@TITLE@@", esc(subject)).replace("@@CSS@@", CSS)
           + f'<body class="sr-bg" style="margin:0;padding:0;width:100%;background-color:{BG};">\n'
           + f'<div role="article" aria-roledescription="email" aria-label="{esc(subject, True)}" lang="en" '
           + f'dir="ltr" class="sr-bg" style="background-color:{BG};">\n'
           + '<div style="display:none;font-size:1px;line-height:1px;max-height:0;max-width:0;opacity:0;'
           + f'overflow:hidden;mso-hide:all;">{esc(e["preheader"])}{PREHEADER_FILL}</div>\n'
           + '<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" class="sr-bg" '
           + f'style="width:100%;background-color:{BG};">\n<tr><td align="center" style="padding:24px 12px 32px 12px;">\n'
           + '<!--[if mso]><table role="presentation" align="center" width="600" cellpadding="0" cellspacing="0" '
           + 'border="0"><tr><td><![endif]-->\n'
           + '<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" '
           + 'style="width:100%;max-width:600px;">\n'
           + f'<tr><td style="padding:0 2px 12px 2px;">{WORDMARK}</td></tr>\n'
           + f'<tr><td class="sr-card sr-pad" style="background-color:{CARD};border:1px solid {LINE};'
           + 'border-radius:8px;padding:28px 32px 12px 32px;">\n'
           + "\n".join(parts)
           + '\n</td></tr>\n'
           + f'<tr><td style="padding:16px 2px 0 2px;">{foot_html}</td></tr>\n'
           + '</table>\n<!--[if mso]></td></tr></table><![endif]-->\n</td></tr>\n</table>\n</div>\n</body>\n</html>\n')
    txt = re.sub(r"\n{3,}", "\n\n", "\n".join(text + foot_text)).strip() + "\n"
    return doc, txt


def eml(e, txt, doc):
    m = EmailMessage()
    m["From"] = formataddr(e["sender"])
    m["To"] = formataddr(e["to"])
    if e.get("reply_to"):
        m["Reply-To"] = formataddr(e["reply_to"])
    m["Subject"] = e["subject"]
    when = datetime(*e["date"], tzinfo=PARIS)
    m["Date"] = format_datetime(when)
    m["Message-ID"] = f"<{e['slug']}.{when:%Y%m%d%H%M}@smartreq.example>"
    m["Auto-Submitted"] = "auto-generated"      # RFC 3834: no auto-replies to this message
    m["X-Auto-Response-Suppress"] = "All"       # the same for Exchange and Outlook
    m["X-SmartReq-Reason"] = e["reason"]        # lets people sort Smart Req mail with a rule
    m["X-SmartReq-Tender"] = ", ".join(e["tenders"])
    m.set_content(txt)
    m.add_alternative(doc, subtype="html")
    return m.as_bytes()


def main():
    viewer = []
    for e in EMAILS:
        doc, txt = build(e)
        (HERE / f"{e['slug']}.html").write_text(doc, encoding="utf-8")
        (HERE / f"{e['slug']}.txt").write_text(txt, encoding="utf-8")
        (HERE / f"{e['slug']}.eml").write_bytes(eml(e, txt, doc))
        when = datetime(*e["date"], tzinfo=PARIS)
        sender = formataddr(e["sender"]) + (f" · reply to {e['reply_to'][0]}" if e.get("reply_to") else "")
        viewer.append(dict(slug=e["slug"], title=e["title"], phase=e["phase"], klass=e["klass"], when=e["when"],
                           sender=sender, to=formataddr(e["to"]), date=when.strftime("%a %d %b %Y, %H:%M"),
                           subject=e["subject"], preheader=e["preheader"], html=doc, text=txt,
                           kb=round(len(doc.encode("utf-8")) / 1024, 1)))
        print(f"{e['slug']:<30} {viewer[-1]['kb']:>5} KB  {e['subject']}")
    data = json.dumps(viewer, ensure_ascii=False).replace("<", "\\u003c")
    page = (HERE / "viewer.template.html").read_text(encoding="utf-8")
    (HERE / "index.html").write_text(page.replace("@@DATA@@", data).replace("@@DARK@@", DARK_QUERY),
                                     encoding="utf-8")


if __name__ == "__main__":
    main()
