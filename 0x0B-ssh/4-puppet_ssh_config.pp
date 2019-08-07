# automate changes to ssh_config using puppet
file_line { 'password':
    ensure   => present,
    line     => 'PasswordAuthentication no',
    match    => '^.?.*PasswordAuthentication yes$',
    replace  => true,
    path     => '/etc/ssh/ssh_config',
    multiple => false,
}

file_line { 'identity':
    ensure             => present,
    line               => 'IdentityFile ~/.ssh/holberton',
    match              => '^.*IdentityFile ~/.ssh/holberton$',
    path               => '/etc/ssh/ssh_config',
    multiple           => false,
    append_on_no_match => true,
}