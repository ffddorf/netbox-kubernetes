from ansible_collections.ansible.utils.plugins.plugin_utils.base.ipaddr_utils import ipaddr

JINJA2_FILTERS = {
    'ipaddr': ipaddr,
}
