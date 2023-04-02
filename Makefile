run-test:
	python -m unittest

run:
	uvicorn src.catalog.api:app --reload
