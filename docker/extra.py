import sys
sys.path.append('/etc/netbox/config/modules')

from ansible_collections.ansible.utils.plugins.plugin_utils.base.ipaddr_utils import ipaddr
from slugify import slugify, SLUG_OK

def slugify_filter(input, **kwargs):
  if "extra_chars" in kwargs:
    kwargs["ok"] = SLUG_OK+kwargs["extra_chars"]
    del kwargs["extra_chars"]
  return slugify(input, **kwargs)

JINJA2_FILTERS = {
    'ipaddr': ipaddr,
    'slugify': slugify_filter,
}
