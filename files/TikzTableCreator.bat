@echo off
title TikzTable Creator
setlocal EnableDelayedExpansion
color 09

cls

::---------------------------------------------------------------------------------
::Setting up the functions section, and spacing.

set /p nbfunctions=How many functions ? 
echo.
set local=1
set parenthesis=);
set functions[0]="0$x$", "/1");
:while
	if %local% leq %nbfunctions% (
		set /p tempfunction=Function %local% ? 
		set rawfunctions[%local%]=!tempfunction!
		set /p tempspacing=Spacing ? 
		set functions[%local%]="!local!$!tempfunction!$", "/!tempspacing!"!parenthesis!
		set /a local += 1
		goto while
	)


cls
::Makes txt file containing each function in raw text.
(for /L %%f in (1,1,!nbfunctions!) do (
	echo !rawfunctions[%%f]!
)) > rawfunctions.txt

python MakeURL.py > url.txt
::Makes txt file containing urls for Wolfram|Alpha API and opens the funtions' data pages.
for /F "delims=" %%i in (url.txt) do set urlval=!urlval! %%i
::Creates urlval variable containing urls.

::In case of a glitch :
::MakeURL.py will open the Wolfram|Alpha pages for each function.
::This checks for root validity, assuring there is no glitch.
echo Checking internet connection...
Ping www.google.com -n 1 -w 1000
cls
if errorlevel 1 (
	set internet=Notconnectedtointernet
	echo Not connected to internet.
	ping localhost -n 2 >nul
	goto notwolfram
) else (
	set internet=Connectedtointernet
)
ping localhost -n 1 >nul


set /p wolframbool=Wolfram, y or n ? 

::Making user input minimal is best
if %wolframbool% == y (
	python GetRoots.py > roots.txt
	start roots.txt
)
::------------------------------------------------------

:notwolfram

(for /L %%i in (0,1,!nbfunctions!) do (
   echo functions.put(!functions[%%i]!
)) > functions.txt
::Creates tikz functions text.


if %errorlevel% == 0 (
	color 0a
	echo Successful. Output sent to functions.txt.
) else (
	color 0c
	echo.
	echo [7;31mUnsuccessful.[0m
	echo [91mPress a key to exit.[0m
	pause>null
	exit
)
ping localhost -n 2 >nul

cls

if %internet% == Notconnectedtointernet (
	goto manualsections
) else if %wolframbool% neq y (
	goto manualsections
)


set /p autosectionsbool=Automatic sections fill, y or n ? 
if %autosectionsbool% == y (
	goto autosections
)


::--------------------------------------------------------------------------------
::Setting up the numbers section
:manualsections
color 09
set /p nbsections=How many sections ? 
set /a nbsections -= 1

set local=0


:whiletwo
if %local% leq %nbsections% (
		set /p tempsection=New section, infinity is double backslash infty : 
		set sections[%local%]=!tempsection!
		set /a local += 1
		goto whiletwo
	)

cls
(for /L %%i in (0,1,!nbsections!) do (
   echo "$!sections[%%i]!$"
)) > sections.csv

python MakeSections.py > sections.txt
::Creates tikz text for sections.

if %errorlevel% == 0 (
	color 0a
	echo Successful. Output sent to sections.txt.
) else (
	color 0c
	echo.
	echo [7;31mUnsuccessful.[0m
	echo [91mPress a key to exit.[0m
	pause>null
	exit
)
ping localhost -n 2 >nul

cls

goto skip

::SET UP GOTO TO SKIP IN CASE OF AUTOMATIC SECTIONS FILL-IN
::SET UP VARIABLES
:autosections

set local=0

set /p left_infty=Negative infty, y or n ? 
set /p right_infty=Positive infty, y or n ? 

if %left_infty% == y (
	set sections[!local!]=-\\infty
	set /a local += 1
)

for /F "delims=" %%i in (roots.txt) do (
	echo %%i
	set sections[!local!]=%%i
	set /a local += 1
)

if %right_infty% == y (
	set sections[!local!]=+\\infty
	set /a local += 1
)

set /a local -= 1

(for /L %%i in (0,1,!local!) do (
   echo "$!sections[%%i]!$"
)) > sections.csv
python MakeSections.py > sections.txt
::Creates tikz text for sections, with the automated values.

set /a nbsections = local

:skip
::--------------------------------------------------------------------------
::Setting up the signs and variations section
color 09
set local=0
set local2=0
set /a othernbfunctions = nbfunctions-1
set /a linvaluescount = 2*nbsections + 1

:whilethree
set count[0]=0
if %local% lss %nbfunctions% (
	set /p valtyp=Value type, LIN or VAR ? 
	if !valtyp! == lin (
		set valtyp=LIN
		echo You need to write %linvaluescount% values.
	) else if !valtyp! == var (
		set valtyp=VAR
	)
	set tempvalue=0
	set tempvallist[!local2!]=!valtyp!
	:whiletemp1
	if !tempvalue! neq stop (
		set /a local2 += 1
		set /p tempvalue=New value, stop to stop, s for space : 
		if !tempvalue! neq stop (
			set tempvallist[!local2!]=!tempvalue!
		)
		goto whiletemp1
	)
	set /a local += 1
	set /a count[%local%]=local2-1
	goto whilethree
)
cls
::Manually input values.

if exist values\ (
	rmdir /s /q values
	mkdir values
) else (
	mkdir values
)


cd values

for /L %%c in (1,1,%local%) do (
	(for /L %%i in (0,1, !count[%%c]!) do (
		if !tempvallist[%%i]! == s (
			echo.
		) else (
			echo !tempvallist[%%i]!
		)
	)) > values%%c.csv
)
(echo %local% > length.txt)

cd ..\
python MakeValues.py > values.txt

cls
if %errorlevel% == 0 (
	color 0a
	echo Successful. Output sent to values.txt.
) else (
	color 0c
	echo.
	echo [7;31mUnsuccessful.[0m
	echo [91mPress a key to exit.[0m
	pause>null
	exit
)
ping localhost -n 2 >nul

cls



::----------------------------------------
::Global rescaling, custom spacing
color 09

set /p globresc=Global Rescaling, write a number or no : 
set /p customspace=Custom Space, write a number or no : 

(
	if %globresc% == no (
		echo .
	) else (
		echo %globresc%
	)
	if %customspace% == no (
		echo .
	) else (
		echo %customspace%
	)
	echo .
	if %customspace% == no (
		echo false
	) else (
		echo true
	)
) > rescaling_info.csv

python MakeRescaling.py > rescaling.txt

cls
if %errorlevel% == 0 (
	color 0a
	echo Successful. Output sent to rescaling.txt.
) else (
	color 0c
	echo.
	echo [7;31mUnsuccessful.[0m
	echo [91mPress a key to exit.[0m
	pause>null
	exit
)
ping localhost -n 2 >nul

python MakeJava.py > Main.java

cls
if %errorlevel% == 0 (
	color 0a
	echo Code creation successful. Java file created. Creating tikzpicture code...
) else (
	color 0c
	echo.
	echo [7;31mUnsuccessful.[0m
	echo [91mPress a key to exit.[0m
	pause>null
	exit
)
ping localhost -n 2 >nul
javac Main.java
cls
python MakeLog.py > log.txt
del rawfunctions.txt
del url.txt
del functions.txt
del sections.txt
del values.txt
del rescaling.txt
del roots.txt
del rescaling_info.csv
del sections.csv
rmdir /s /q values

java Main > ..\tikztable.txt

if %errorlevel% == 0 (
	echo Tikzpicture code sent to tikztable.txt.
	echo.
	echo Hit any key to exit.
	pause>null
) else (
	color 0c
	echo.
	echo [7;31mUnsuccessful.[0m
	echo [91mPress a key to exit.[0m
	pause>null
	exit
)

exit
