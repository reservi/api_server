MAKEFILE_DIR_PATH := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))


help:
	@echo "Makefile for reservi project."
	@echo "Available commands:"
	@echo ">> clean - deletes all build and test-related directories except virtual environment."
	@echo ">> venv-clean - deletes virtual environment if exists"
	@echo ">> venv-create - creates virtual environment if does not exists"
	@echo ">> install - installs application on virtual environment"
	@echo ">> test - runs the unit tests on virtual environment"
	@echo ">> lint - runs pylint check"
	@echo ">> black-lint - auto-formats the code with black on src/ and tests/ "

clean:
	@echo "Cleaning the repo..."
	@if [[ -d $(MAKEFILE_DIR_PATH)htmlcov ]]; then\
		rm -r $(MAKEFILE_DIR_PATH)htmlcov;\
		echo ">> Removed $(MAKEFILE_DIR_PATH)htmlcov";\
	fi
	@if [[ -e $(MAKEFILE_DIR_PATH).coverage ]]; then\
		rm -r $(MAKEFILE_DIR_PATH).coverage;\
		echo ">> Removed $(MAKEFILE_DIR_PATH).coverage";\
	fi
	@if [[ -d $(MAKEFILE_DIR_PATH)build ]]; then\
		rm -r $(MAKEFILE_DIR_PATH)build;\
		echo ">> Removed $(MAKEFILE_DIR_PATH)build";\
	fi
	@if [[ -d $(MAKEFILE_DIR_PATH)dist ]]; then\
		rm -r $(MAKEFILE_DIR_PATH)dist;\
		echo ">> Removed $(MAKEFILE_DIR_PATH)dist";\
	fi
	@if [[ -d $(MAKEFILE_DIR_PATH)reservi.egg-info ]]; then\
		rm -r $(MAKEFILE_DIR_PATH)reservi.egg-info;\
		echo ">> Removed $(MAKEFILE_DIR_PATH)reservi.egg-info";\
	fi

venv-clean:
	@echo "Deleting virtual environment if exists..."
	@if [[ -d $(MAKEFILE_DIR_PATH).venv ]]; then\
		rm -r $(MAKEFILE_DIR_PATH).venv;\
		echo ">> Removed $(MAKEFILE_DIR_PATH).venv";\
	else\
		echo "!ERR: No virtualenv detected on $(MAKEFILE_DIR_PATH).";\
	fi

venv-create:
	@echo "Creating virtual environment if does not exists..."
	@if [[ ! -d $(MAKEFILE_DIR_PATH).venv ]]; then\
		./setupenv_and_install.sh\
		echo ">> Virtualenv $(MAKEFILE_DIR_PATH).venv created.";\
	else\
		echo "!ERR: Virtualenv $(MAKEFILE_DIR_PATH).venv already exists.";\
	fi

install:
	@echo "Installing application on virtual environment..."
	@if [[ -d $(MAKEFILE_DIR_PATH).venv ]]; then\
		$(MAKEFILE_DIR_PATH).venv/bin/python setup.py install;\
	else\
		echo "!ERR: No virtualenv detected on $(MAKEFILE_DIR_PATH).";\
	fi

develop:
	@echo "Switching to develop mode on virtual environment..."
	@if [[ -d $(MAKEFILE_DIR_PATH).venv ]]; then\
		$(MAKEFILE_DIR_PATH).venv/bin/python setup.py develop;\
	else\
		echo "!ERR: No virtualenv detected on $(MAKEFILE_DIR_PATH).";\
	fi

test:
	@echo "Running unit tests..."
	@if [[ -d $(MAKEFILE_DIR_PATH).venv ]]; then\
		$(MAKEFILE_DIR_PATH).venv/bin/coverage run -m unittest -vvv;\
	else\
		echo "!ERR: No virtualenv detected on $(MAKEFILE_DIR_PATH).";\
	fi

run:
	@echo "Running --no-exec version..."
	@if [[ -d $(MAKEFILE_DIR_PATH).venv ]]; then\
		$(MAKEFILE_DIR_PATH).venv/bin/reservi --no_exec;\
	else\
		echo "!ERR: No virtualenv detected on $(MAKEFILE_DIR_PATH).";\
	fi

raport:
	@echo "Display coverage report..."
	@if [[ -d $(MAKEFILE_DIR_PATH).venv ]]; then\
		$(MAKEFILE_DIR_PATH).venv/bin/coverage report --fail-under=80 --omit '*venv*,*tests*';\
	else\
		echo "!ERR: No virtualenv detected on $(MAKEFILE_DIR_PATH).";\
	fi

html:
	@echo "Display coverage report..."
	@if [[ -d $(MAKEFILE_DIR_PATH).venv ]]; then\
		$(MAKEFILE_DIR_PATH).venv/bin/coverage html --omit '*venv*,*tests*';\
	else\
		echo "!ERR: No virtualenv detected on $(MAKEFILE_DIR_PATH).";\
	fi

lint:
	@echo "Running linter on /reservi ..."
	@if [[ -d $(MAKEFILE_DIR_PATH).venv ]]; then\
		$(MAKEFILE_DIR_PATH).venv/bin/pylint --fail-under=8.0 src;\
	else\
		echo "!ERR: No virtualenv detected on $(MAKEFILE_DIR_PATH).";\
	fi

black-lint:
	@echo "Running Black auto-lint ..."
	@if [[ -d $(MAKEFILE_DIR_PATH).venv ]]; then\
		$(MAKEFILE_DIR_PATH).venv/bin/black -t py38 src/ tests/;\
	else\
		echo "!ERR: No virtualenv detected on $(MAKEFILE_DIR_PATH).";\
	fi
