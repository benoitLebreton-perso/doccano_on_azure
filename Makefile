new-panai-retro:
	python src/retro_panai/create_project.py

get-retro-panai-answers:
	python src/retro_panai/get_answers.py

tests:
	python -m pytest tests

coverage:
	pytest --cov=src/ tests/
	