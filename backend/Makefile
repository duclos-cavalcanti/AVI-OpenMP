SHELL := /bin/bash
FILE := $(lastword $(MAKEFILE_LIST))

.PHONY: all
all:

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
	@echo -e '\n** CLEANING INTERFACE'
	@rm -rf include lib __pycache__
	@rm -f *.cpp
	@rm -f *.so
	@rm -f *.o
	@${MAKE} -C cpp_backend/ clean


.PHONY: build
build: clean
	@echo -e '\n** COMPILING INTERFACE'
	@${MAKE} -C cpp_backend/ build
	@echo -e '\n** compiling cpp-py interface...'
	python3 compile.py
