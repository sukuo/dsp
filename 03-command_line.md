# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

`cat <filename>` : shows the contents of the file <br />
`pwd` : shows the path of the directory you are currently in'<br />
`man <command>` : pulls up all information for a given command, best way to find information!<br />
`grep <text> <filename>` : outputs all instances of the text in the file<br />
`head -n <filename>` : outputs the top n lines of the file<br />
`tail -n <filename>` : outputs the bottom n lines of the file<br />
`touch <filename>` : creates a file<br />
`clear` : gives you a blank terminal window<br />
`rm -r <directory>/` : force removes a directory or file<br />
`mv <old_file> <new_file>` : renames the old file to the new file name<br />
`mv <file> <directory>` : moves the file to the selected directory<br />
`find <directory> "<filename>"` : finds all file with specified name in selected directory, can be used with * to find all files containing the "(filename)"<br />
"up arrow" : recalls last command executed, can be pressed multiple times to see past commands executed from latest to earliest<br />
`wc` : wordcount with options (-l : lines, -w : words, -c : byte size, -m : # of characters)<br />


---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

`ls` : lists all files and directories in the current directory not including ones starting with '.'<br />
`ls -a` : lists all files and directories including the ones starting with a '.'<br />
`ls -l` : lists files and directories in long format including information on permissions, owner, group, file size, date of last change, and its name<br />
`ls -lh` : lists files and directories in long format except it shows the size of the files all in bits (readable)<br />
`ls -lah` : lists all files (including those starting with a '.') and directories in long, human readable form<br />
`ls -t` : lists and sorts files and directories by most recently modified <br />
`ls -Glp` : lists files and directories in long format and highlights, places a '/' behind the directories<br />


---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

Five Favorite ls options:<br />
1)  -R<br />
2)  -1<br />
3)  -d<br />
4)  -p<br />
5)  -l<br />

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

`xargs` allows you to string together arguments and execute them on standard inputs such as:  ls, find, delete, touch etc...
For example - if you happen to create a bunch of text files in a given directory that were incorrectly named, you could pipe the find function to find the '*.txt' files into xargs and it will go through the files one by one and execute commands (either rename or delete) on them.

 

