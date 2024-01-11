#.EXPORT_ALL_VARIABLES:
#.PHONY: venv install pre-commit clean
#
#GLOBAL_PYTHON = $(shell py -3.9 -c 'import sys; print(sys.executable)')
#LOCAL_PYTHON = eval{poetry env info --path}
#LOCAL_PRE_COMMIT = .\\.venv\\Lib\\site-packages\\pre_commit
PYTHON_VERSION = '3.11'

#setup: venv install pre-commit

venv:
	@echo "Install python with pyenv, define as local and creatte the virtual envirionment"
	pyenv install --skip-existing ${PYTHON_VERSION}
	pyenv local ${PYTHON_VERSION}  # Activate Python 3.11 for the current project
	poetry env use ${PYTHON_VERSION}

install:
	@echo $LOCAL_PYTHON
	@echo "Installing dependencies..."
	poetry install --no-root --sync

#pre-commit: #${LOCAL_PYTHON} ${LOCAL_PRE_COMMIT}
#	@echo "Setting up pre-commit..."
#	.\\.venv\\Scripts\\pre-commit install
#	.\\.venv\\Scripts\\pre-commit autoupdate

#clean:
#	if exist .\\.git\\hooks ( rmdir .\\.git\\hooks /q /s )
#	if exist .\\.venv\\ ( rmdir .\\.venv /q /s )
#	if exist poetry.lock ( del poetry.lock /q /s )