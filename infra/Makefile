APP_NAME=infra
SERVICE=web

build:
	docker compose down
	docker system prune --all --volumes --force
	docker compose build --no-cache

run:
	docker compose run --rm $(SERVICE) python3 /app/test_magic.py

shell:
	docker compose run --rm $(SERVICE) bash

check-libmagic:
	docker compose run --rm $(SERVICE) bash -lc \
	"apt-get update >/dev/null && apt-get install -y libmagic-dev file >/dev/null && \
	find /usr -name 'libmagic.so*'"

uname:
	docker compose run --rm $(SERVICE) uname -m

clean:
	docker compose down
	docker system prune --all --volumes --force
