#!/bin/bash
# 
#
#
read -s -p "Enter your password: " pass
echo
echo "Is your password really $pass?"

read -n1 -p "Do you want to continue [Y/N]?" answer
case $answer in 
	Y | y)  echo
		echo "fine, continue on...";;
	N | n)  echo
		echo OK, goodbye
		exit;;
esac
echo "This is the end of the script"
