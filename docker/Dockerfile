# pinned to specific release
ARG NETBOX_VERSION
FROM docker.io/netboxcommunity/netbox:${NETBOX_VERSION} AS base

FROM --platform=$BUILDPLATFORM docker.io/netboxcommunity/netbox:${NETBOX_VERSION} AS build

# Patch NGINX Unit config
RUN apt-get update || true && apt-get install -yq jq
RUN jq -r '.settings.http.max_body_size = 52428800' /etc/unit/nginx-unit.json \
  > /etc/unit/nginx-unit-edit.json && \
  mv /etc/unit/nginx-unit-edit.json /etc/unit/nginx-unit.json

# Install packages for collectstatic
COPY plugin_requirements.txt extra_requirements.txt /opt/netbox/
RUN /usr/local/bin/uv pip install \
  -r /opt/netbox/plugin_requirements.txt \
  -r /opt/netbox/extra_requirements.txt

COPY plugins.py extra.py /etc/netbox/config/
RUN SECRET_KEY="dummydummydummydummydummydummydummydummydummydummy" /opt/netbox/venv/bin/python /opt/netbox/netbox/manage.py collectstatic --no-input

FROM docker.io/netboxcommunity/netbox:${NETBOX_VERSION} AS prod

# Copy modified files
COPY --from=build /etc/unit /etc/unit
COPY --from=build /opt/netbox/netbox/static /opt/netbox/netbox/static

# Install plugins for prod
COPY plugin_requirements.txt extra_requirements.txt /opt/netbox/
RUN /usr/local/bin/uv pip install \
  -r /opt/netbox/plugin_requirements.txt \
  -r /opt/netbox/extra_requirements.txt
