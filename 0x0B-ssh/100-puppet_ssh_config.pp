#!/usr/bin/env bash
# Puppet manifest to change ssh config file.

file { 'etc/ssh/ssh_config':
	ensure => present,
	content => "
		#SSH client configuration
		host*
		IdentityFile ~/.ssh/school
		PasswordAuthentication no
		",
}
