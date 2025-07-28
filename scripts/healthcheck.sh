#!/bin/bash
# Verifica se o serviço Flask está a responder

curl -i http://localhost:5000/health
