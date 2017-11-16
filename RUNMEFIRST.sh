echo "To install Linus you need root privileges." 
read -r -p "Are you sure you want to give those privileges? [y/N] " response
if [[ "$response" =~ ([yY][eE][sS]|[yY])+$ ]]
then
    read -r -p "Do you already have the "su" password set? [y/N] " response
	if [[ "$response" =~ ([yY][eE][sS]|[yY])+$ ]]
	then
    	echo "Please execute the command 'su' and run install.sh to install Linus."
	else
    	sudo passwd
    	echo "Please execute the command 'su' and run install.sh to install Linus."
	fi
else
    echo "Can't install Linus if you don't give the permission :c"
fi
