
.PHONY: help format

.DEFAULT_GOAL := help

shell: ## Spawns a shell within the virtualenv
	python -m pipenv shell

fmck: ## Format check
	black --check .;\
	flake8;\
	isort --check .;\
	mypy .

fm: ## Format
	black .; isort .

help: ## Show help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
