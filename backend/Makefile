
.PHONY: run shell fmck fm help

.DEFAULT_GOAL := help

run: ## Run server
	uvicorn src.main:app --reload --host 0.0.0.0

migrate: ## Migrate
	python -m src.migrate

seed: ## Seed
	python -m src.seed

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
