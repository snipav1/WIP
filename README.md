# WIP
quick script that checks the ip address location


Setup:

    sudo pip install -r requirements.txt


Usage:

    - Run ip.py script by setting ISP provider. ie: at&t, comcast
	python3 ip.py -p "at&t"
      
Optional:

Very useful if a bash alias is created
    
Modify .bashrc file with something like these Examples:
    
    alias wip='python3 /<path>/ip.py -p "at&t"'

