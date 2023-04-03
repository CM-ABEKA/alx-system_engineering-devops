# installing a package with puppet

# ensuring that pip3 is installed
package { 'python3-pip':
  ensure => 'installed',
}

# installing flask version 2.1.0
exec { 'install flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => ['/usr/bin', '/usr/sbin'],
  unless  => '/usr/bin/test -f /usr/local/bin/flask',
  require => Package['python3-pip'],
}

# ensure flask command is available as a symlink
file { '/usr/local/bin/flask':
  ensure => 'link',
  target => '/usr/local/lib/python3.8/dist-packages/flask/bin/flask',
}
