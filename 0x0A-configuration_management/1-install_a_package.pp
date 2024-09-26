# Ensure pip3 is installed and manage Python packages with pip3
package { 'python3-pip':
  ensure => installed,
}

# Install a specific version of Flask (2.1.0) using pip3
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}

