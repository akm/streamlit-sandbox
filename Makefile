.PHONY: default
default: up dev

.PHONY: dev
dev:
	streamlit run my_first_app.py

.PHONY: up
up:
	docker-compose up -d

.PHONY: down
down:
	docker-compose down
