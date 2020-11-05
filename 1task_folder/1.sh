#!/bin/bash

IFS='/' read -r -a array <<< "Paris/France/Europe"

echo "${array[0]}"
