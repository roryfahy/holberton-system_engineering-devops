# manifest to replace a line in file with '.php' instead of '.phpp'
exec { 'not resource title':
          command => '/bin/sed -i "s|class-wp-locale.phpp|class-wp-locale.php|g" /var/www/html/wp-settings.php'
        }
