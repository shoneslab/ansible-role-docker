docker
======
[![Build Status](https://travis-ci.org/shoneslab/ansible-role-docker.svg?branch=master)](https://travis-ci.org/shoneslab/ansible-role-docker)


This ansible role installs Docker community edition(ce), commercially supported edition(cs) and enterprise edition(ee) on ubuntu hosts.

Requirements
------------

This role requires Ansible 2.0 or higher and platform requirements are listed in the metadata file.

Role Variables
--------------

The Following pre-requisites are needed prior to the installation.
```
docker_prereq_packages:
  - apt-transport-https
  - ca-certificates
  - curl
  - software-properties-common
```

The following dependencies are for Ubuntu trusty
```
docker_prereq_packages_trusty:
  - linux-image-extra-{{ansible_kernel}}
  - linux-image-extra-virtual
```

Following values are for Docker Community Edition (CE)
```
docker_ce_version: 17.03.0~ce-0~ubuntu-xenial

docker_ce_gpg_key_url: "https://download.docker.com/linux/ubuntu/gpg"

docker_ce_apt_repo_url:
  - "deb [arch=amd64] https://download.docker.com/linux/{{ ansible_distribution|lower }} {{ ansible_lsb.codename }} stable"

docker_ce_package_name: docker-ce
```

Following values are for Docker Enterprise Edition (EE)
```
docker_ee_version: 17.03.0~ee-0~ubuntu-xenial

docker_ee_gpg_key_url: "https://<docker-ee-url>/gpg"

docker_ee_apt_repo_url:
  - "deb [arch=amd64] https://<docker-ee-url>/linux/{{ ansible_distribution|lower }} {{ ansible_lsb.codename }} stable-17.03"

docker_ee_package_name: docker-ee
```

Following section enables Community Edition (ce) for this role. To Enable Enterprise Edition, Change the below values

```
If docker_version omits the version value, it will install the latest one
docker_version: "{{ docker_ce_version }}"
docker_gpg_key_url: "{{ docker_ce_gpg_key_url }}"
docker_apt_repo_url: "{{ docker_ce_apt_repo_url }}"
docker_package_name: "{{ docker_ce_package_name }}"
```

docker_enable_experimental_features: false

Example Playbook
----------------

    - hosts: all
      roles:
         - { role: docker }

Testing         
-------
pre-requisites:
vagrant and virtual box

```
pip install molecule
pip install python-vagrant

molecule test
```
License
-------

BSD, MIT

Author Information
------------------

Shone Jacob
