SHELL := /bin/bash
FILE := $(lastword $(MAKEFILE_LIST))

all:
	@echo "DUMMY"

.PHONY: help
help: 
	$(info Toolchain version: placeholder)
	$(info)
	$(info Targets: )
	$(info  * run           - Runs Python frontend)
	$(info  * clean       	- Cleans project)
	@echo ""

.PHONY: clean
clean:
	@echo -e '\n** CLEANING PROJECT'
	@rm -vrf __pycache__
	@${MAKE} -C backend/ clean


.PHONY: run
run:
	python main.py
