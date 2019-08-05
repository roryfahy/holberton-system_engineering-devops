# create holberton resource inthe /tmp dir
file { 'resource title':
    path    => '/tmp/holberton',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet',
}
