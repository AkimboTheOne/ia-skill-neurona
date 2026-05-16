SHELL := /bin/bash

PLUGIN_DIR := $(abspath $(dir $(lastword $(MAKEFILE_LIST))))
REPO_ROOT := $(abspath $(PLUGIN_DIR)/../..)
APP_DIR := $(PLUGIN_DIR)
IMAGE ?= mem-api:local
PORT ?= 8000

.PHONY: help install setup env build up down logs smoke test

help:
	@printf '%s\n' "Targets:" \
		"  setup   - initialize a local .env file from .env.example if missing" \
		"  install - alias for setup; kept for product-style onboarding" \
		"  env     - print the effective plugin environment" \
		"  build   - build the container image" \
		"  up      - run the service with docker compose" \
		"  down    - stop the service" \
		"  logs    - follow service logs" \
		"  smoke   - run a basic health/config smoke test" \
		"  test    - run the plugin test suite"

setup:
	@bash "$(PLUGIN_DIR)/scripts/setup.sh"

install: setup

env:
	@bash "$(PLUGIN_DIR)/scripts/env.sh"

build:
	@bash "$(PLUGIN_DIR)/scripts/build.sh"

up:
	@bash "$(PLUGIN_DIR)/scripts/up.sh"

down:
	@bash "$(PLUGIN_DIR)/scripts/down.sh"

logs:
	@bash "$(PLUGIN_DIR)/scripts/logs.sh"

smoke:
	@bash "$(PLUGIN_DIR)/scripts/smoke.sh"

test:
	@bash "$(PLUGIN_DIR)/scripts/test.sh"
