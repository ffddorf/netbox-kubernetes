from ansible_utils.plugins.filter.ipaddr import _ipaddr

JINJA2_FILTERS = {
    'ipaddr': _ipaddr,
}
