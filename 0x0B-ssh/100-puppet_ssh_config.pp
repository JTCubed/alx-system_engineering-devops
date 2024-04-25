# Define SSH client configuration file content
$file_content = @(EOT)
Host 34.227.91.196
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
EOT

# Ensure SSH client configuration file exists and has the correct content
file { '/etc/ssh/ssh_config':
    ensure  => present,
    content => $file_content,
    mode    => '0644', # Set permissions to 0644
    owner   => 'root',
    group   => 'root',
}
