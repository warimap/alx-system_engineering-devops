# This Puppet manifest ensures the /var/www/html directory exists with the correct permissions
file { '/var/www/html':
  ensure  => directory,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
}

# Restart Apache to apply the changes
service { 'apache2':
  ensure => running,
  enable => true,
  require => File['/var/www/html'],
}

