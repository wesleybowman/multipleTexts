multipleTexts

    multipleTexts allows the user to send multiple text messages of the same string.
    Copyright (C) 2013 Wesley A. Bowman

    This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

=============

Send multiple texts of the same string through Gmail

This program allows the user to send multiple text messages of the same string through Gmail. 

The first time the program is run, it will ask the user for a username and password.
It will then create a file named username.txt, and every subsequent run of the program it will use this
file to log into your gmail account. 

There needs a be a providers.txt in the same folder as the program, and an example text file is included in the
repository. This allows the user to input an name for the service provider instead of having to 
find the email address of the service provider every time the program is run. 

Once prompted for the number, provider, count, and message, just hit enter after inputting the information for each 
text box. Once the final text box has text and then the enter key has been hit, the program will start sending the 
text messages, and once it is done will close the GUI.
