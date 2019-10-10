# this file is used to increase the OS limit of nginx open file count
file { 'resource title':
            path    => '/etc/default/nginx',
            mode    => '0644',
            owner   => 'root',
            group   => 'root',
            content => 'ULIMIT="-n 15000"\n',
            }
