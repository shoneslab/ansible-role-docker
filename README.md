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
docker_ce_package_name: docker-ce

docker_ce_debian_version: 18.03.1~ce-0~ubuntu
docker_ce_debian_gpg_key_url: "https://download.docker.com/linux/ubuntu/gpg"
docker_ce_debian_apt_repo_url:
  - "deb [arch=amd64] https://download.docker.com/linux/{{ ansible_distribution|lower }} {{ ansible_lsb.codename }} stable"

docker_ce_redhat_version: 18.03.1.ce-1.el7.centos
docker_ce_redhat_yum_repo_url: https://download.docker.com/linux/centos/7/$basearch/stable
docker_ce_redhat_gpg_key_url: https://download.docker.com/linux/centos/gpg
```

Following values are for Docker Community Edition (CS)
```
docker_cs_package_name: 'docker-engine'

docker_cs_redhat_version: 1.13.1.cs9-1.el7.centos
docker_cs_redhat_rpm_key: https://sks-keyservers.net/pks/lookup?op=get&search=0xee6d536cf7dc86e2d7d56f59a178ac6c6238f52e
dockee_cs_redhat_yum_repo_url: https://packages.docker.com/1.13/yum/repo/main/centos/7

docker_cs_debian_version: 1.13.1~cs9-0~ubuntu-xenial
docker_cs_debian_rpm_key: "https://sks-keyservers.net/pks/lookup?op=get&search=0xee6d536cf7dc86e2d7d56f59a178ac6c6238f52e"
docker_cs_debian_apt_repo_url: "deb https://packages.docker.com/1.13/apt/repo ubuntu-{{ ansible_distribution_release }} main"
```

Following section enables Community Edition (ce) for this role. To Enable CE Edition, Change the below values

```
docker_version: ce
docker_apt_validate_certs: no
docker_enable_experimental_features: true
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
