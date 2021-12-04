SHELL := /bin/bash
FILE := $(lastword $(MAKEFILE_LIST))

all:
	@echo "DUMMY"

.PHONY: help
help: 
	$(info Toolchain version: placeholder)
	$(info)
	$(info Targets: )
	$(info  * build         - Builds)
	$(info  * clean       	- Cleans project)
	@echo ""

.PHONY: clean
clean:
	@echo -e '\n** CLEANING PROJECT'
	@rm -vrf include lib __pycache__
	@rm -vf *.cpp
	@rm -vf *.so
	@rm -vf *.o


.PHONY: build
build:
	${MAKE} -C backend/ build
