#GLOBAL_PYTHON = $(shell py -3.9 -c 'import sys; print(sys.executable)')
#LOCAL_PYTHON = eval{poetry env info --path}
#LOCAL_PRE_COMMIT = .\\.venv\\Lib\\site-packages\\pre_commit
PYTHON_VERSION = '3.11'

setup: venv install

venv:
	@echo "Install python with pyenv, define as local and creatte the virtual envirionment..."
	pyenv install --skip-existing ${PYTHON_VERSION}
	pyenv local ${PYTHON_VERSION}  # Activate Python 3.11 for the current project
	poetry env use ${PYTHON_VERSION}

install:
	@echo $LOCAL_PYTHON
	@echo "Installing dependencies..."
	poetry install --no-root --sync

test:
	@echo "Running tests..."
	poetry run pytest

coverage:
	@echo "Creating coverage report..."
	poetry run pytest --cov=coding_challenges --cov-report=html --cov-report=term-missing

clean:
	@echo "Cleaning up..."
	if exist poetry.lock ( del poetry.lock /q /s )