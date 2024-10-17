@echo off
:loop
start chrome
timeout /t 2 /nobreak >nul
goto loop
