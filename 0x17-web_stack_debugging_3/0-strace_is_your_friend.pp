# Fix Error in file extension in wp-settings ".phpp"

exec { 'fixWpSettigsTypo' :
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin:/bin'
}
