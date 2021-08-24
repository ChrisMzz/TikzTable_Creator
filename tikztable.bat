@echo off
color 0c
cd files
javac Main.java
if %errorlevel% == 0 (
	color 0a
	java Main > ..\tikztable.txt
	echo Successful. Output sent to tikztable.txt.
) else (
	echo.
	echo [7;31mUnsuccessful.[0m
	echo [91mPress a key to exit.[0m
)
pause>null
