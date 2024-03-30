# pinned to specific release
ARG NETBOX_VERSION=v3.7.1
FROM docker.io/netboxcommunity/netbox:${NETBOX_VERSION} AS base

COPY plugin_requirements.txt /opt/netbox/
RUN /opt/netbox/venv/bin/pip install --no-warn-script-location -r /opt/netbox/plugin_requirements.txt

COPY plugins.py /etc/netbox/config/plugins.py
RUN SECRET_KEY="dummydummydummydummydummydummydummydummydummydummy" /opt/netbox/venv/bin/python /opt/netbox/netbox/manage.py collectstatic --no-input
