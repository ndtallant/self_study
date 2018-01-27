# Opening a specific VirtualBox VM through terminal.

1. Go to the VM you want to open, right-click, and "create desktop shortcut".
![](/bs/bs_01.png)

2. Go to the shortcut, right-click, and select "properties".
![](/bs/bs_02.png)
![](/bs/bs_03.png)

3. Copy the "command" to your clipboard, feel free to delete the shortcut.
![](/bs/bs_04.png)

4. Open a file in your text editor with the name of your desired command (I used capp).
![](/bs/bs_05.png)

5. Make the top line of the file "#!/bin/bash", and the other line the copied command.
   The comment is not needed, feel free to delete it!
![](/bs/bs_06.png)

6. Save the file, and make it executable with "chmod +x *filename*".
![](/bs/bs_07.png)

7. Move the file to /usr/bin/, you may need root permission. 
![](/bs/bs_08.png)

8. Now type the name of your command (filename) in terminal, or as an executable. 
![](/bs/bs_09.png)

9. Enjoy not clicking two buttons to access your VM!
![](/bs/bs_10.png)