import requests
import functools


def fetch_file(url):
    # Make request to file location
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    return r.content


def compose(*funcs):
    return functools.reduce(lambda f, g: lambda x: f(g(x)), funcs, lambda x: x)
