# simplest-keylogger
this keylogger is only for educational purposes or self monitoring.

At the moment it only works on Windows.

to install it in any windows pc you need to place the folder named "llave" like this E:\llave (E: being your USB) and run "armador", this will change regedit to open the
keylogger in startup, it will be placed in C:\Users\Public\Documents\Proyectos and armador will execute the keylogger.

the keylogger will create a txt file named "proximos_proyectos" and store any keystrokes in it.

for manual install:
make a folder named "proyectos" in C:\Users\Public\Documents\ and store the keylogger in the folder, run the keylogger and do the next steps
windows+r:
regedit 
(Equipo\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run)
in this folder make a string value named php and modify it to the path "C:\Users\Public\Documents\Proyectos"