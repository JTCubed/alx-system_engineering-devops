# Define SSH client configuration file content
$file_content = @(EOT)
Host your_server_ip
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
EOT

# Ensure SSH client configuration file exists and has the correct content
file { '/home/your_username/.ssh/config': # Update the path and username accordingly
    ensure  => present,
    content => $file_content,
    mode    => '0600', # Set permissions to 0600
    owner   => 'your_username', # Update the username accordingly
    group   => 'your_username', # Update the group accordingly
}
