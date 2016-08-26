@echo off
mkdir "%COMPUTERNAME%"
break>%COMPUTERNAME%/infocollect.txt
echo ========Melt Down This Computer===========>>%COMPUTERNAME%/infocollect.txt
echo ==========================================>>%COMPUTERNAME%/infocollect.txt
echo ====== Thing cant get pass=====>>%COMPUTERNAME%/infocollect.txt
echo ===============================>>%COMPUTERNAME%/infocollect.txt
echo Factory:     >>%COMPUTERNAME%/infocollect.txt
echo Department:  >>%COMPUTERNAME%/infocollect.txt
echo WAN IP Address:  >>%COMPUTERNAME%/infocollect.txt
echo WAN MAC Address: >>%COMPUTERNAME%/infocollect.txt
echo User:            >>%COMPUTERNAME%/infocollect.txt
echo Hardware SN:     >>%COMPUTERNAME%/infocollect.txt
echo Office Version:  >>%COMPUTERNAME%/infocollect.txt
echo Office No.:      >>%COMPUTERNAME%/infocollect.txt
echo Anti Virus software:     >>%COMPUTERNAME%/infocollect.txt
echo Anti Virus software No.:  >>%COMPUTERNAME%/infocollect.txt
echo Antivirus software expired date:  >>%COMPUTERNAME%/infocollect.txt
echo ========Thing we can get it free =========>>%COMPUTERNAME%/infocollect.txt
echo ==========================================>>%COMPUTERNAME%/infocollect.txt
echo Checking your system info. Please wait...
systeminfo | findstr /c:"Host Name" /c:"OS Name" /c:"OS Version" /c:"System Manufacturer" /c:"System Model" /c:"System Type" /c:"Processor" /c:"Physical Memory" /c:"Original Install Date">>%COMPUTERNAME%/infocollect.txt
ipconfig/all | findstr Address>>%COMPUTERNAME%/infocollect.txt
echo Service Tag:>>%COMPUTERNAME%/infocollect.txt
wmic bios get serialnumber>>%COMPUTERNAME%/infocollect.txt
echo \n>>%COMPUTERNAME%/infocollect.txt
setlocal enabledelayedexpansion

  WMIC LOGICALDISK where drivetype=3 get caption,size,FreeSpace>%~n0.tmp
@set tong=0
  for /f "tokens=1-3 skip=1" %%a in ('type "%~n0.tmp"') do call :displayinfo %%a %%b %%c

exit /b

:displayinfo
  set drive=%1
  set free=%2
  set total=%3
  set /a tong =%tong% + %total%	
  call :convertbytes total
  call :convertbytes free
  echo Tong: %tong%>>%COMPUTERNAME%/infocollect.txt
  echo %drive% Total: %total%. Free: %free%>>%COMPUTERNAME%/infocollect.txt
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
