# Self Study

This repo is full of half finished thoughts and scratch notes.


## Opening a specific VirtualBox VM through terminal.

1. Go to the VM you want to open, right-click, and "create desktop shortcut".
![](./vm-from-cmd/bs_01.png)
![](./vm-from-cmd/bs_02.png)

2. Go to the shortcut, right-click, and select "properties".
![](./vm-from-cmd/bs_03.png)

3. Copy the "command" to your clipboard, feel free to delete the shortcut.
![](./vm-from-cmd/bs_04.png)

4. Open a file in your text editor with the name of your desired command (I used capp).
![](./vm-from-cmd/bs_05.png)

5. Make the top line of the file "#!/bin/bash", and the other line the copied command.
   The comment is not needed, feel free to delete it!
![](./vm-from-cmd/bs_06.png)

6. Save the file, and make it executable with "chmod +x *filename*".
![](./vm-from-cmd/bs_07.png)

7. Move the file to /usr/bin/, you may need root permission. 
![](./vm-from-cmd/bs_08.png)

8. Now type the name of your command (filename) in terminal, or as an executable. 
![](./vm-from-cmd/bs_09.png)

9. Enjoy not clicking two buttons to access your VM!
![](./vm-from-cmd/bs_10.png)
