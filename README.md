# SecSE CTF Announcement Tool

[![Build Status](https://travis-ci.org/secse-ctf/announcement-tool.svg?branch=master)](https://travis-ci.org/secse-ctf/announcement-tool)
[![codecov](https://codecov.io/gh/secse-ctf/announcement-tool/branch/master/graph/badge.svg)](https://codecov.io/gh/secse-ctf/announcement-tool)
[![Python Versions](https://img.shields.io/pypi/pyversions/ctf-announcement.svg)](https://pypi.python.org/pypi/ctf-announcement)

This is a simple commandline tool to quickly generate SecSE CTF announcements as markdown posts for usage on meta.

## Installation

    $ pip install ctf-announcement --upgrade

## Usage

Call `ctf-announcement` with either the ID, the link or a substring of the title of an upcoming CTF. The tool will parse upcoming CTFs from CTFtime, and output a link to create the meta post and the markdown post body, e.g.:

```
$ ctf-announcement hitc

29 upcoming CTFs found.
Here is the template for HITCON CTF 2018:

-- URL -------------------------------------------------------------------------
https://security.meta.stackexchange.com/questions/ask?title=HITCON+CTF+2018+%7C+Sat%2C+20+Oct+02%3A00+%E2%80%94+Mon%2C+22+Oct+02%3A00+UTC+%2848h%29&tags=ctf,discussion

-- Body ------------------------------------------------------------------------
Let's participate in the [HITCON CTF 2018](https://ctftime.org/event/669)!

- **Format:** Jeopardy
- **Duration:** 48h
- **Start:** Sat, 2018-10-20 02:00 UTC <sup>[(See other timezones)](https://www.timeanddate.com/worldclock/fixedtime.html?msg=HITCON+CTF+2018&iso=20181020T020000&ah=48)</sup>
- **Finish:** Mon, 2018-10-22 02:00 UTC
- **Official URL:** [https://ctf.hitcon.org/](https://ctf.hitcon.org/)
- **CTFtime URL:** [https://ctftime.org/event/669](https://ctftime.org/event/669)
- **Rating weight:** 98.32 <sup>[(?)](https://ctftime.org/faq/#weight)</sup>
- **Organizers:** [217](https://ctftime.org/team/5160), [HITCON](https://ctftime.org/team/8299)
- **Event series:** [HITCON CTF](https://ctftime.org/ctf/79)

General info:

- We compete as team [secse](https://security.meta.stackexchange.com/q/1117/).
- We communicate over [Slack](http://sec-ctf.slack.com/). To get an invitation
  to the workspace you can contact any active team member. (We will need to
  know an email address to send the invitation to and a reference to your
  Security.SE profile.)
- For questions, join us in the [public chat room](https://chat.stackexchange.com/rooms/151/the-dmz).

Good luck everyone!
--------------------------------------------------------------------------------
```
