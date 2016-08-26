@echo off
  setlocal enabledelayedexpansion

  WMIC LOGICALDISK where drivetype=3 get caption,size,FreeSpace>%~n0.tmp

  for /f "tokens=1-3 skip=1" %%a in ('type "%~n0.tmp"') do call :displayinfo %%a %%b %%c
exit /b


:displayinfo
  set drive=%1
  set free=%2
  set total=%3

  call :convertbytes total
  call :convertbytes free

  echo %drive% Total: %total%. Free: %free%>>file.txt
goto :eof


:convertbytes
  set str=!%1!
  set "sign="
  set bytes=0
  set fraction=0
  
  :loop
    set fraction=%bytes:~0,1%
    set bytes=%str:~-3%
    set str=%str:~0,-3%
    if "%sign%"=="GB" set sign=TB
    if "%sign%"=="MB" set sign=GB
    if "%sign%"=="KB" set sign=MB
    if "%sign%"=="B" set sign=KB
    if not defined sign set sign=B
  if defined str goto loop
  set %1=%bytes%.%fraction% %sign%
goto :eof
pause