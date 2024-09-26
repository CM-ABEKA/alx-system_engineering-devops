# Kill the process 'killmenow'
exec { 'kill-killmenow':
  command  => 'pkill killmenow',
  path     => '/usr/bin:/bin',
  onlyif   => 'pgrep killmenow',
}
