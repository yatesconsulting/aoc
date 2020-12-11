@echo off
rem fix this every so often
for /f "delims=" %%a in (../sessioncookie.txt) DO ( 
  set session=%%a
)

rem set year from current directory name
for %%I in (.) do set /a year=%%~nxI

rem setting defday from command line || today+1 and prompt user

IF "%~1"=="" goto setfromuser:
set /a day=%1%
goto setfromuserskip

:setfromuser
SET /A defday = 100%date:~7,2% %% 100 + 1
set /p day=Year=%year%; Please enter day [%defday%] || set /a day=%defday%

:setfromuserskip
set baseloc=\Users\15759\OneDrive - Roswell Independent School District\Documents\GitHub\aoc
echo curl -b "session=%session%" -o "%baseloc%\%year%\%day%.txt" "https://adventofcode.com/%year%/day/%day%/input"
curl -b "session=%session%" -o "%baseloc%\%year%\%day%.txt" "https://adventofcode.com/%year%/day/%day%/input"

pause
