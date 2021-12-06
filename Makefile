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
pack: clean
	@echo -e '\n** ARCHIVING PROJECT'
	@rm -f archive.zip
	@zip -r archive.zip ../${FOLDER}
	@zip -d archive.zip *.git/* *.git

.PHONY: send
send:
	@echo -e '\n** SENDING PROJECT'
	@scp archive.zip ga74ped@hpc05.clients.eikon.tum.de:~/Documents

.PHONY: get
get:
	@echo -e '\n** GETTING PLOT FROM SERVER'
	@rm -f plot_server.png
	@scp ga74ped@hpc05.clients.eikon.tum.de:~/Documents/${FOLDER}/plot.png ./plot_server.png

.PHONY: run
run:
	@echo -e '\n** RUNNING PROJECT'
	@python main.py
