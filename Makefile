test:
	docker-compose up -d
	pytest -v --disable-warnings || true
	docker-compose down