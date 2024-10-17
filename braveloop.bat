@echo off
:loop
start brave
timeout /t 2 /nobreak >nul
goto loop
