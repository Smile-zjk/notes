#!/bin/bash
# Processing options & parameters with getopts
#
echo
while getopts :ab:cd opt

do
	case "$opt" in
		a) echo "Found the -a option, OPTARG=[$OPTARG] OPTIND=[$OPTIND]" ;;
		b) echo "Found the -b option, OPTARG=[$OPTARG] OPTIND=[$OPTIND]" ;;
		c) echo "Found the -c option, OPTARG=[$OPTARG] OPTIND=[$OPTIND]" ;;
		d) echo "Found the -d option, OPTARG=[$OPTARG] OPTIND=[$OPTIND]" ;;
		*) echo "Unknown option: $opt" ;;
	esac
done
#
echo  $[ $OPTIND -1 ]
shift $[ $OPTIND -1 ]
#
echo
count=1
for param in "$@"
do
	echo "Parameter $count: $param"
	count=$[ $count + 1 ]
done
