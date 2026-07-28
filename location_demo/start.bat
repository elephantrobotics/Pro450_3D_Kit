@echo off

:Excute
cd /d "%~dp0\.."
start ..\RobotVisionSuite.exe -l unstacking_demo\demo.rvs -r
echo rvs demo running

:Protect
ping 127.0.0.1 -n 10 >nul
for /f "delims= " %%i in ('tasklist^|find /i "RobotVisionSuite.exe"') do (
 if /i "%%i"=="RobotVisionSuite.exe" goto Protect)

echo rvs demo restart
goto Excute