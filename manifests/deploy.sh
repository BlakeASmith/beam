#!/bin/bash

function install-ingress-nginx {
    helm repo add nginx-stable https://helm.nginx.com/stable
    helm repo update
    sudo helm install my-release nginx-stable/nginx-ingress
}