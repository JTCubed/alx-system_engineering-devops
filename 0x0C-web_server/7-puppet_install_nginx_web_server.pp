# Define the class for Nginx installation and configuration
class nginx {
  
  package { 'nginx':
    ensure => installed,
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => template('nginx/default.erb'),
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx'],
  }

  file { '/usr/share/nginx/html/index.html':
    ensure  => file,
    content => 'Hello World!',
    require => Package['nginx'],
    notify  => Service['nginx'],
  }
}

# Define the class for the redirection configuration
class redirect {
  file { '/etc/nginx/sites-available/redirect_me':
    ensure  => file,
    content => template('nginx/redirect_me.erb'),
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  file { '/etc/nginx/sites-enabled/redirect_me':
    ensure  => link,
    target  => '/etc/nginx/sites-available/redirect_me',
    require => File['/etc/nginx/sites-available/redirect_me'],
  }
}

# Include the classes in the main manifest
class { 'nginx': }
class { 'redirect': }
