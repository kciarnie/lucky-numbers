SHELL:=/bin/bash
ENV = dev
OUTPUT = $(shell which brew)
ACTIVATE = $(shell source $(ENV)/bin/activate)

.PHONY: help clean local
.SILENT: help
help:
	echo "Make"
	echo "----------------------------------------------------------"
	echo "make clean:	Cleans the directory"
	echo "make local:	Sets up a local instance"
	echo "make setup: 	Makes sure we setup python 3 and a venv"
	echo "make test:	runs the pytests"
	echo "----------------------------------------------------------"

clean:
	-$(RM) -rf dist
	-$(RM) -rf build
	-$(RM) -rf $(ENV)
	-$(RM) -f .env
	-$(RM) -rf lucky-numbers.egg-info

.ONESHELL:
local:
	./scripts/local.sh $(ENV)

homebrew:
	./scripts/homebrew.sh
	
setup:
	make homebrew
	brew install python3

	# Setup the virtual environment
	pip3 install virtualenv

test:
	pytest