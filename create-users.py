#!/usr/bin/python3

# INET4031
# Leandro Escobar
# Data Created: 2025-10-27
# Date Last Modified: 2025-10-27

#Important Moduels:
import os # used to run systems commands to create users,set passwords,and add groups
import re    # used for regular expression matching to detect commented lines
import sys # Used to read input from standard input (stdin)


def main():
    # Porcess each line froom the input file
    for line in sys.stdin:

        # Check if the line starts with # comment using regex
        match = re.match("^#",line)

        # splits the line into field uisng ':' as the delimiter
        fields = line.strip().split(':')

        # Skip this line if it is acomment that starts with a # or if it does not have exactly 5 fields,
        # Ensuring that only valid, properly formatted user data is processed
        if match or len(fields) != 5:
            continue

        # Extract user inoframtion from the fields
        username = fields[0] # The username for the new account
        password = fields[1] # The password for the new account
        gecos = "%s %s,,," % (fields[3],fields[2])

        # Splits the group field inot a list of groups
        groups = fields[4].split(',')

        # Build the system command to create the user account
        print("==> Creating account for %s..." % (username))
        # Build the command to set the users password
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username) 

        os.system(cmd) # Execute the command to create the user

        # Inform the user that the password is being set
        print("==> Setting the password for %s..." % (username))
        # Build the commadn to set the user's password
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        os.system(cmd) # Execute the command to set the password

        for group in groups:
            if group != '-': # skip if no groups are listed 
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print cmd
                os.system(cmd) # Execute the command to add the user to the group

if __name__ == '__main__':
    main()
