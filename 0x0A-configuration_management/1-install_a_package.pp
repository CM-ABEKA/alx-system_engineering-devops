# Ensuring that pip3 is installed
package { 'python3-pip':
  ensure => 'installed',
}

# Installing required dependencies for Flask
package { ['python3-setuptools', 'python3-wheel']:
  ensure  => 'installed',
  require => Package['python3-pip'],
}

# Installing Flask version 2.1.0
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => [Package['python3-pip'], Package['python3-setuptools'], Package['python3-wheel']],
  notify   => Exec['flask_install_success'],
}

# Ensure flask command is available as a symlink
file { '/usr/local/bin/flask':
  ensure => 'link',
  target => '/usr/local/lib/python3.8/dist-packages/flask/bin/flask',
}

# Executed after Flask installation is successful
exec { 'flask_install_success':
  command   => 'echo "Notice: /Stage[main]/Main/Package[flask]/ensure: created"',
  path      => ['/usr/bin', '/usr/sbin'],
  onlyif    => 'which flask',
  logoutput => true,
  unless    => 'test -f /usr/local/bin/flask',
}
