# sync
Back-end Script to sync File Servers 
the execution should be as follows:

--
# /usr/bin/env python sunc.py [Source-Directory]
--

the script test source and destination equality 
regarding their size and in case of unequality 
the rsync starts synchronising two servers.
this script is supposed to check rsync process
on every execution so that if you execute it twice 
on the same directory it will give you 0 1 2

0 signifies that the servers are not in sync and starts rsync
--
1 signifies that servers are in complete sync
--
2 signifies that the rsync is being executed 
--

