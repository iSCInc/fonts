#!/bin/sh

# Config
basePath="iscinc/fonts/"

# Script to clone any missing extensions and updates the others
ssh -p 29418 gerrit.wikimedia.org gerrit ls-projects | grep "^${basePath}" | sed "s,${basePath},," | while read PROJECT
do
	echo "[${PROJECT}]:"
	# Clone projects that don't exist here...
	if [ ! -d "${PROJECT}" ]; then
		git submodule add "https://git.inc.isc/gerrit/r/p/${basePath}${PROJECT}.git" "${PROJECT}"
		echo "\tbranch = ." >> .gitmodules
	fi
done
