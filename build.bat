@echo off
rem Build script to compile the executable

setlocal

rem Set the compiler and options
set COMPILER=g++
set OPTIONS=-o output_executable main.cpp

rem Compile the code
%COMPILER% %OPTIONS%

if %errorlevel% neq 0 (
    echo Build failed!
    exit /b 1
)

echo Build succeeded! Executable created: output_executable
endlocal