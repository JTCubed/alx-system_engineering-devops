# Define the class for Nginx installation and configuration
class nginx {

  package { 'nginx':
    ensure => installed,
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => '
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /usr/share/nginx/html;
    index index.html index.htm;

    server_name _;

    location / {
        try_files $uri $uri/ =404;
    }

    error_page 404 /404.html;
    location = /404.html {
        root /usr/share/nginx/html;
        internal;
    }
}',
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
    content => '
server {
    listen 80;
    server_name _;

    location /redirect_me {
        return 301 https://www.youtube.com/;
    }
}',
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
