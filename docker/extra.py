import sys
sys.path.append('/etc/netbox/config/modules')

from ansible_collections.ansible.utils.plugins.plugin_utils.base.ipaddr_utils import ipaddr
from slugify import slugify

JINJA2_FILTERS = {
    'ipaddr': ipaddr,
    'slugify': slugify,
}
