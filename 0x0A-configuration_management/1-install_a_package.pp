# ensure pip3 is installed

package { 'python3-pip':
  ensure => 'installed',
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  notify   => Exec['success_log'],
}

exec { 'success_log':
  command   => '/bin/echo Notice: /Stage[main]/Main/Package[flask]/ensure: created',
  path      => '/bin',
  onlyif    => 'which flask',
  logoutput => true,
  subscribe => Package['flask'],
}

