PLUGINS = ["netbox_secrets", "netbox_bgp"]

PLUGINS_CONFIG = {
    'netbox_bgp': {
        'top_level_menu': True,
    },
    'netbox_secrets': {
        'display_default': 'right_page',
    },
}
