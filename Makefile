clean:
	@find . -name "*.pyc" -delete
	@find . -name "*.swp" -delete
	@find . -name "__pycache__" -delete

lint:
	@pycodestyle .

test: clean lint
	pytest --cov=src tests/
