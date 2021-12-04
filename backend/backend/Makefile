SHELL := /bin/bash
FILE := $(lastword $(MAKEFILE_LIST))

isbuildEmpty = $(shell ls build/)

all:
	@echo "DUMMY"

.PHONY: help
help: 
	$(info Toolchain version: placeholder)
	$(info)
	$(info Targets: )
	$(info  * build         - Builds backend)
	$(info  * clean       	- Cleans backend project)
	@echo ""

.PHONY: clean
clean:
	@echo -e '\n** CLEANING PROJECT'
	@if [ -n "$(call isbuildEmpty)" ]; then \
		rm -rvf build/*; \
	fi
	@touch build/.gitkeep


.PHONY: build
build: clean
	@echo -e '\n** BUILDING PROJECT'
	cd build/ && cmake -DCMAKE_BUILD_TYPE=Release ..
	$(MAKE) -C build/
	$(MAKE) -C build/ install
