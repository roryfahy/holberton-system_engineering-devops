# manifest the death of a puppet
exec { 'not resource title':
  command => '/usr/bin/pkill killmenow'
}
