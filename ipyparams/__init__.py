# vim: expandtab tabstop=4 shiftwidth=4

from collections import defaultdict
from os.path import basename
from time import sleep
from urllib.parse import urlparse, parse_qs

_ipython_support = True

try:
    from IPython import get_ipython
    from IPython.display import display, Javascript
except ImportError:
    print('This package only works within Jupyter/IPython accessed from a browser.')
    _ipython_support = False

raw_url = ''
params = defaultdict(lambda: None)
raw_params = defaultdict(lambda: None)
notebook_name = ''

def update_params(url):
    global raw_url
    global params
    global raw_params
    global notebook_name

    raw_url = url
    parsed = urlparse(url)
    notebook_name = basename(parsed.path)
    _raw_params = parse_qs(parsed.query)

    for k, v in _raw_params.items():
        params[k] = v[0]

    raw_params = _raw_params

def target_func(comm, open_msg):
    # comm is the kernel Comm instance
    # open_msg is the comm_open message

    # register handler for later messages
    @comm.on_msg
    def _recv(msg):
        # data is in msg['content']['data']
        comm.send({'echo': msg['content']['data']})

        for k, v in msg['content']['data'].items():
            if k == 'ipyparams_browser_url':
                update_params(v)

    # send data to the front end on creation
    comm.send({'init': 1})

if _ipython_support:
    # register the comm target on the kernel side (back end)
    get_ipython().kernel.comm_manager.register_target('url_querystring_target', target_func)
    sleep(0.2)

    # register the comm target on the browser side (front end)
    display(Javascript('''
console.log('Starting front end url_querystring_target comm target');
const comm = Jupyter.notebook.kernel.comm_manager.new_comm('url_querystring_target', {'init': 1});
comm.send({'ipyparams_browser_url': window.location.href});
console.log('Sent window.location.href on url_querystring_target comm target');

comm.on_msg(function(msg) {
    console.log(msg.content.data);
});
'''))
