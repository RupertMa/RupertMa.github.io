---
layout: post
---

# Linux command use cases | Linux命令行用例  

#### 1.    Create a background session, run jobs and logs the output. Could be very useful when running Hadoop jobs:

```bash
screen -LS <screen_name> # Create a screen, give it a name and enable automatic loggings
cd dir # Change directory to where you want to run your job 
```
Ctrl+A and Ctrl+D to exit the screen. Let it run in the background. When you start a screen that way, it will create a screenlog.0 file. Note that you can’t scroll when you’re in a screen so you’ll need to exit and view the log file.  

You can re-enter the screen with `screen -r screen name` and can see a list of available screens with `screen -ls`  




#### 2. File Permissions for Unix-like operating systems

When you input `ls -l .` you will see something like 
```bash
drwxr-xr-x 2 root root     4096 Mar  5 16:09 post
-rw------- 1 root root  1792614 Mar  5 23:13 nohup.out
```
The first column shows the permission settings for a file or a directory.  
1. The 1st character could be -/d. "-" indicates regular file and d indicates directory.  
2. The 2nd to 4th characters indicates and **r**ead, **w**rite and e**x**ecute permissions for the file owner.  
3. The 5th to 7th characters indicates and **r**ead, **w**rite and e**x**ecute permissions for the group owner of the file.  
4. The 8th to 10th characters indicates and **r**ead, **w**rite and e**x**ecute permissions for all other users.  

The thrid column shows the the owner of the file, which is root in the example above. 

The forth column shows the the group owner of the file, which is root in the example above. Group owners are a group of related users.

*For other useful file permission commands, like `chmod`, `su`, `sudo`, `chown`,`chgrp`, please refer to [Permissions](http://linuxcommand.org/lc3_lts0090.php) *


#### 3. Schedule jobs using crontab command

To shedule jobs, `cd` to /var/spool/cron directory and input `crontab -e` to edit a cron file.  

Several examples of using crontab command below
```bash
# crontab -e
SHELL=/bin/bash
MAILTO=root@example.com
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin

# For details see man 4 crontabs

# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name  command to be executed

# This means appending the text to text.txt at 1:01 am everyday
01 01 * * * echo "this is a test file." >> test.txt

# This means appending the text to another_text.txt at 1:01 am every Friday
01 01 * * 5 echo "this is another test file." >> another_test.txt
``` 

#### 4. Get the min, max, count, sum of a column in a file

To perfom this simple calculation, you can use `awk` to do the job. One example is shown below.  

```bash
cat ./data/count.txt | awk '{if(min==""){min=max=$1}; 
                             if($1>max) {max=$1}; 
                             if($1<min) {min=$1}; 
                             total+=$1; count+=1} END {print total, count, max, min}'
```

