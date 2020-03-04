---
layout: post
---

# Linux command use cases | Linux命令行用例  

1.	Create a background session, run jobs and logs the output. Could be very useful when running Hadoop jobs:

```bash
screen -LS <screen_name> # Create a screen, give it a name and enable automatic loggings
cd dir # Change directory to where you want to run your job 
```
Ctrl+A and Ctrl+D to exit the screen. Let it run in the background. When you start a screen that way, it will create a screenlog.0 file. Note that you can’t scroll when you’re in a screen so you’ll need to exit and view the log file.  

You can re-enter the screen with *screen -r screen name* and can see a list of available screens with *screen -ls*  




