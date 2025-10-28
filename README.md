# INET 4031 Add User Script

## Description
This Python script automates the creation of multiple user accounts and group assignments on an Ubuntu Linux system. 
It reads user information from an input file (`create-users.input`) and executes the necessary system commands to create accounts, set passwords, and assign users to groups.

## Instructions

### Setup
1. Clone this repository to your Ubuntu VM:
   ```bash
   git clone https://github.com/escob138/inet_4031_adduser_script.git
   cd inet_4031_adduser_script
##
 Make the scripts executable:
chmod +x create-users.py

## To test the script without making any system changes:
./create-users.py < create-users.input

## This will print the commands that would be executed, allowing you to verify the input file and script logic safely.

## To actually create the users and assign passwords/groups:
sudo ./create-users.py < create-users.input

## This requires root privileges. After running, you can verify user creation:
grep user0 /etc/passwd
grep user0 /etc/group

#### **Optional Notes**
```markdown
## Notes
- The input file uses colon-separated fields in the format:  
  `username:password:lastname:firstname:groups`
- Groups are comma-separated; use `-` if no group is assigned.
- Always perform a dry run first to prevent mistakes.
