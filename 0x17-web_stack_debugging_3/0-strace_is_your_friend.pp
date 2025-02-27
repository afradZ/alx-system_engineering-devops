exec { 'install_php':
  command => '/usr/bin/apt update && /usr/bin/apt install php libapache2-mod-php -y',
  path    => ['/usr/bin', '/usr/sbin'],
  onlyif  => 'test ! -f /usr/bin/php',
}

exec { 'restart_apache':
  command => '/bin/systemctl restart apache2',
  path    => ['/bin', '/usr/bin', '/sbin', '/usr/sbin'],
  subscribe => Exec['install_php'],
}

