import sys
from unittest import mock
import pytest
from ctf_announcement.__main__ import main, run, NoMatchException


def test_main(capsys, feed_path):
    with mock.patch.object(sys, 'argv', ['ctf_announcement', '-u', feed_path, '686']):
        main()
    out, err = capsys.readouterr()
    assert 'Insomni' in out


def test_event_by_title(local_run):
    out = local_run('hitc')
    assert 'HITCON' in out


def test_event_by_id(local_run):
    out = local_run('686')
    assert 'Insomni' in out


def test_event_by_url(local_run):
    out = local_run('https://ctftime.org/event/685')
    assert 'SECCON' in out


def test_event_not_found(local_run):
    with pytest.raises(NoMatchException) as e:
        out = local_run('12341234')
