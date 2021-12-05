SHELL := /bin/bash
FILE := $(lastword $(MAKEFILE_LIST))
CWD := $(shell pwd)
FOLDER := $(shell basename ${CWD})

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

.PHONY: compile
compile:
	@echo -e "\n** COMPILING PROJECT"
	@${MAKE} -C backend/ build

.PHONY: test
test:
	@echo -e '\n** TESTING PROJECT'
	@python -m pytest tests/

.PHONY: pack
pack: archive.zip
	@echo -e '\n** ARCHIVING PROJECT'
	@zip -r archive.zip ../${FOLDER}

.PHONY: send
send: pack
	@echo -e '\n** SENDING PROJECT'

.PHONY: run
run:
	@echo -e '\n** RUNNING PROJECT'
	@python main.py
