#!/bin/bash
cd /Users/zmiguel/Projetos/voiceguard
source venv/bin/activate
export FLASK_APP=app.py
export FLASK_ENV=development
export ENV_FILE=.env
python app.py
