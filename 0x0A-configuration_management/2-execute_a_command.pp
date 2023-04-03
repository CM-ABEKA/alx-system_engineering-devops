# this manifest kills a process named killmenow

exec { 'kill process':
  command => '/bin/pkill killmenow',
  path    => ['/bin', '/usr/bin', '/usr/sbin'],
  onlyif  => 'pgrep killmenow',
}
