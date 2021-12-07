SHELL := /bin/bash
FILE := $(lastword $(MAKEFILE_LIST))

isbuildEmpty = $(shell ls build/)

.PHONY: all
all:

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
	@echo -e '\n** CLEANING BACKEND'
	@if [ -n "$(call isbuildEmpty)" ]; then \
		rm -rf build/*; \
	fi
	@touch build/.gitkeep

.PHONY: build
build: clean
	@echo -e '\n** COMPILING BACKEND'
	cd build/ && cmake -DCMAKE_BUILD_TYPE=Release ..
	@echo -e '\n** compiling backend...'
	@$(MAKE) -C build/
	@echo -e '\n**  installing library...'
	@$(MAKE) -C build/ install
