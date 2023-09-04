# creating a custom HTTP header response
package { 'nginx':
    ensure => installed,
    before => Service['nginx'],
}

service { 'nginx':
    ensure     => running,
    enable     => true,
    subscribe  => File['/etc/nginx/sites-available/default'],
}

file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => template('nginx/default.erb'),
    require => Package['nginx'],
}