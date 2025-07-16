.PHONY: run setup activate

run:
	source venv/bin/activate && python voiceguard/app.py

setup:
	python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt

activate:
	source venv/bin/activate

