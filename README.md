# Netbox on Kubernetes

Setup Netbox on a single-node Kubernetes Cluster using Kustomize

## Install

```sh
kubectl apply -k .
```

## Applying changes

### Kubernetes Manifests

Run `kubectl apply -k .` to apply any changes to the Kubernetes Manifests.

### Upgrades

When changing the Netbox version or plugins, a new image needs to be built. Make a commit to have the CI build and push the image.

Afterwards, update `netbox/kustomization.yaml` to use the newly built image, by specifying `<netbox-version>-<short git hash>`.

Then apply the change, by running `kubectl apply -k .`
