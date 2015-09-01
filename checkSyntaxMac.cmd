del /F /Q %TEMP%\%~nx1.log
RunRegRS.vbs RSInit.exe checkSyntaxMac.mac %~nx1
chcp 1251 >nul
for /f "delims=" %%A in (%TEMP%\%~nx1.log) do >nul chcp 1251& echo.%%A