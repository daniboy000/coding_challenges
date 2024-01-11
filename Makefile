PYTHON_VERSION = '3.11'

setup: venv install

.PHONY: venv
venv:
	@echo "Install python with pyenv, define as local and creatte the virtual envirionment..."
	pyenv install --skip-existing ${PYTHON_VERSION}
	pyenv local ${PYTHON_VERSION}  # Activate Python 3.11 for the current project
	poetry env use ${PYTHON_VERSION}

install:
	@echo $LOCAL_PYTHON
	@echo "Installing dependencies..."
	poetry install --no-root --sync

.PHONY: tests
tests:
	@echo "Running tests..."
	poetry run pytest

coverage:
	@echo "Creating coverage report..."
	poetry run pytest --cov=coding_challenges --cov-report=html --cov-report=term-missing

clean:
	@echo "Cleaning up..."
	if exist poetry.lock ( del poetry.lock /q /s )