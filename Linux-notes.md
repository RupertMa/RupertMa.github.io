---
layout: post
---

# Linux command use cases | Linux命令行用例  

#### 1.	Create a background session, run jobs and logs the output. Could be very useful when running Hadoop jobs:

```bash
screen -LS <screen_name> # Create a screen, give it a name and enable automatic loggings
cd dir # Change directory to where you want to run your job 
```
Ctrl+A and Ctrl+D to exit the screen. Let it run in the background. When you start a screen that way, it will create a screenlog.0 file. Note that you can’t scroll when you’re in a screen so you’ll need to exit and view the log file.  

You can re-enter the screen with *screen -r screen name* and can see a list of available screens with *screen -ls*  




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
