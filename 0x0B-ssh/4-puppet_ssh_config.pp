# automate changes to ssh_config using puppet
file_line { 'pass?':
    ensure  => present,
    path    => '/etc/ssh/ssh_config',
    line    => 'PasswordAuthentication no',
    match   => '^#?\s*PasswordAuthentication\syes'
    replace => true,
}
file_line { 'pub_key':
    ensure             => present,
    path               => '/etc/ssh/ssh_config',
    line               => 'IdentifyFile ~/.ssh/holberton',
    match              => '^#?\s*IdentifyFile ~/.ssh/holberton',
    append_on_no_match => true,
}
