@echo off
start cmd /k "cd /d %cd% && doskey ls=dir /P $*  && doskey cd=cd /D $* "
 



