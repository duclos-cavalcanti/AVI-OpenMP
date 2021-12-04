SHELL := /bin/bash
FILE := $(lastword $(MAKEFILE_LIST))

.PHONY: all
all:


.PHONY: help
help: 
	$(info Toolchain version: placeholder)
	$(info)
	$(info Targets: )
	$(info  * run           - Runs Python frontend)
	$(info  * build         - Builds backend)
	$(info  * clean       	- Cleans project)
	@echo ""

.PHONY: clean
clean:
	@echo -e '\n** CLEANING PROJECT'
	@rm -rf __pycache__
	@${MAKE} -C backend/ clean

.PHONY: build
build:
	@echo -e "\n** BUILDING PROJECT"
	@${MAKE} -C backend/ build

.PHONY: test
test:
	@echo -e '\n** TESTING PROJECT'
	@python -m pytest tests/

.PHONY: run
run:
	@echo -e '\n** RUNNING PROJECT'
	@python main.py
