# Puppet manifest to change ssh config file.


file_line { 'Remove Password Auth':
	ensure 	=> 'present',
	path 	=> '/etc/ssh/ssh_config',
	line	=> '    PasswordAuthentication no',
}

file_line { 'Declare Identity File':
	ensure	=> 'present',
	path	=> '/etc/ssh/ssh_config',
	line	=> '	IdentityFile ~/.ssh/school',
}
