import os
import shutil
from pytest import fixture
from ctf_announcement.__main__ import run


@fixture
def feed_path():
    return os.path.dirname(os.path.abspath(__file__)) + '/feed.rss'


@fixture
def local_run(feed_path):
    def inner(term):
        return '\n'.join(run(term, feed_path))
    return inner
