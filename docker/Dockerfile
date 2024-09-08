# pinned to specific release
ARG NETBOX_VERSION
FROM docker.io/netboxcommunity/netbox:${NETBOX_VERSION} AS base

# Patch NGINX Unit config
RUN apt-get update || true && apt-get install -yq jq
RUN jq -r '.settings.http.max_body_size = 52428800' /etc/unit/nginx-unit.json \
  > /etc/unit/nginx-unit-edit.json && \
  mv /etc/unit/nginx-unit-edit.json /etc/unit/nginx-unit.json

COPY plugin_requirements.txt extra_requirements.txt /opt/netbox/
RUN /opt/netbox/venv/bin/pip install --no-warn-script-location -r /opt/netbox/plugin_requirements.txt && \
  /opt/netbox/venv/bin/pip install --no-warn-script-location -r /opt/netbox/extra_requirements.txt

# Add ansible.utils collection to use ipaddr filter
RUN mkdir -p /etc/netbox/config/modules/ansible_collections/ansible && \
  curl --fail -L https://github.com/ansible-collections/ansible.utils/archive/main.tar.gz | tar -xz -C . && \
  mv ansible.utils-main /etc/netbox/config/modules/ansible_collections/ansible/utils
ENV ANSIBLE_HOME=/tmp/.ansible

COPY plugins.py extra.py /etc/netbox/config/
RUN SECRET_KEY="dummydummydummydummydummydummydummydummydummydummy" /opt/netbox/venv/bin/python /opt/netbox/netbox/manage.py collectstatic --no-input
