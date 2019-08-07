# automate changes to ssh_config using puppet
file_line { 'pass?':
    ensure  => present,
    path    => '/etc/ssh/ssh_config',
    line    => 'PasswordAuthentication no',
    match   => '^#?.*PasswordAuthentication yes'
    replace => true,
}
file_line { 'pub_key':
    ensure             => present,
    path               => '/etc/ssh/ssh_config',
    line               => 'IdentifyFile ~/.ssh/holberton',
    match              => '^#?.*IdentifyFile ~/.ssh/holberton',
    append_on_no_match => true,
}
