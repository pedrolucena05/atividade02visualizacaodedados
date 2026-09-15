IMAGE_NAME=dashboard-streamlit
CONTAINER_NAME=dashboard-streamlit
PORT=8501

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run --rm \
		--name $(CONTAINER_NAME) \
		-p $(PORT):8501 \
		$(IMAGE_NAME)

show:
	cmd /c start http://localhost:$(PORT)

start: build run

stop:
	docker stop $(CONTAINER_NAME)

clean:
	docker rmi $(IMAGE_NAME)