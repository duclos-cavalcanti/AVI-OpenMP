SHELL := /bin/bash
FILE := $(lastword $(MAKEFILE_LIST))
PWD := $(shell pwd)
FOLDER := $(shell basename ${PWD})

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
	@echo -e '** CLEANING PROJECT'
	@rm -rf __pycache__
	@rm -rf backend/__pycache__
	@rm -f backend/*.cpp
	@rm -f backend/*.so
	@rm -f backend/*.o
	@rm -rf backend/lib
	@rm -rf backend/include
	@rm -rf backend/backend/build/*

.PHONY: build
build:
	@echo -e "\n** BUILDING PROJECT"
	@cd backend/backend/build && cmake -DCMAKE_BUILD_TYPE=Release ..
	@${MAKE} -C backend/backend/build/
	@${MAKE} -C backend/backend/build/ install
	@cd backend && python3 compile.py

.PHONY: test
test:
	@echo -e '\n** TESTING PROJECT'
	@python3 -m pytest -v tests/

.PHONY: run
run:
	@echo -e '\n** RUNNING PROJECT'
	@python3 main.py

.PHONY: img
img:
	@echo -e '\n** Viewing Plot'
	@sxiv plot.png
