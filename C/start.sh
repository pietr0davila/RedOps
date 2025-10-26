#!/bin/bash

usage="Usage: ./start.sh <scriptDirectory> <filename (without extension)> <output file (without extension)>"
dir=${1:-./}
filename=${2:-"main"}   
outFile=${3:?$usage}
args=("${@:4}")
g++ -Wall "$dir"/"$filename".c -o "$dir"/"$outFile" && "$dir"/"$outFile" "${args[@]}"

