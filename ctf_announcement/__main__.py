import argparse
import dateutil.parser
import json
from urllib.parse import quote_plus
import feedparser


FEED_URL = 'https://ctftime.org/event/list/upcoming/rss/'
LINK_TEMPLATE = 'https://security.meta.stackexchange.com/questions/ask?title={title}&tags={tags}'
BODY_TEMPLATE = '''
Let's participate in the [{title}]({ctftime_url})!

- **Format:** {format}
- **Duration:** {hours}h
- **Start:** {start} <sup>[(Other timezone)](https://www.timeanddate.com/worldclock/fixedtime.html?msg={title_enc}&iso={start_iso})</sup>
- **Finish:** {stop} <sup>[(Other timezone)](https://www.timeanddate.com/worldclock/fixedtime.html?msg={title_enc}&iso={stop_iso})</sup>
- **Official URL:** [{official_url}]({official_url})
- **CTFtime URL:** [{ctftime_url}]({ctftime_url})
- **Rating weight:** {weight} <sup>[(?)](https://ctftime.org/faq/#weight)</sup>
- **Organizers:** {organizers}
- **Event series:** [{ctf_name}](https://ctftime.org/ctf/{ctf_id})

General info:

- We compete as team [secse](https://security.meta.stackexchange.com/q/1117/).
- We communicate over [Slack](http://sec-ctf.slack.com/). To get an invitation
  to the workspace you can contact any active team member. (We will need to
  know an email address to send the invitation to and a reference to your
  Security.SE profile.)
- For questions, join us in the [public chat room](https://chat.stackexchange.com/rooms/151/the-dmz).

Good luck everyone!
'''[1:-1]
TAGS = ['ctf', 'discussion']


class Event:

    def __init__(self, event):
        self._event = event
        self.id = int(event.ctftime_url.split('/')[-1])
        self.interval = tuple(dateutil.parser.parse(x) for x in (event.start_date, event.finish_date))
        self.hours = int((self.interval[1] - self.interval[0]).total_seconds() / 3600)

    def __getattr__(self, name):
        return getattr(self._event, name)

    def make_link(self):
        start_f, stop_f = (x.strftime('%a, %d %b %H:%M') for x in self.interval)
        title = '{title} | {start} — {stop} UTC ({hours}h)'.format(
            title=self.title,
            start=start_f,
            stop=stop_f,
            hours=self.hours,
        )
        return LINK_TEMPLATE.format(title=quote_plus(title), tags=','.join(TAGS))

    def make_organizers(self):
        return ', '.join('[{name}](https://ctftime.org/team/{id})'.format(**o) \
                         for o in json.loads(self.organizers))


    def make_body(self):
        start, stop = self.interval
        start_f, stop_f = (x.strftime('%a, %Y-%m-%d %H:%M UTC') for x in (start, stop))
        return BODY_TEMPLATE.format(
            title=self.title,
            title_enc=quote_plus(self.title),
            official_url=self.href,
            ctftime_url=self.link,
            format=self.format_text,
            weight=self.weight,
            organizers=self.make_organizers(),
            start=start_f,
            stop=stop_f,
            hours=self.hours,
            start_iso=self.start_date,
            stop_iso=self.finish_date,
            ctf_id=self.ctf_id,
            ctf_name=self.ctf_name,
        )


def find_event(key, events):
    try:
        return next(e for e in events if e.link == key)
    except StopIteration:
        pass
    if key.isnumeric():
        try:
            return next(e for e in events if e.id == int(key))
        except StopIteration:
            pass
    try:
        return next(e for e in events if key.lower() in e.title.lower())
    except StopIteration:
        raise NoMatchException('Error: No upcoming CTF matches "%s"!' % key)


class NoMatchException(Exception):
    pass


def heading(s):
    if not s:
        return 80 * '-'
    res = '-- %s ' % s
    res += (80 - len(res)) * '-'
    return res


def run(term, feed_url=FEED_URL):
    feed = feedparser.parse(feed_url)
    events = [Event(e) for e in feed.entries]
    yield '%d upcoming CTFs found.' % len(events)
    event = find_event(term, events)
    yield 'Here is the template for %s:\n' % event.title
    yield heading('URL')
    yield event.make_link() + '\n'
    yield heading('Body')
    yield event.make_body()
    yield heading('')


def main():
    parser = argparse.ArgumentParser(description='Secse CTF announcements')
    parser.add_argument('event', help='ID, link or part of CTF event title')
    parser.add_argument('-u', '--url', default=FEED_URL, help='URL to RSS feed')
    args = parser.parse_args()
    try:
        for output in run(args.event, args.url):
            print(output)
    except NoMatchException as e:
        exit(e)


if __name__ == '__main__':
    main()
