run:
	docker build . -t lab_mini_server
	docker run -p 8000:8000 --name lab_mini_server lab_mini_server
	##########################

stop:
	docker stop lab_mini_server
	docker rm lab_mini_server
	##########################

it:
	docker exec -it lab_mini_server /bin/sh
	##########################

clean:
	docker rmi lab_mini_server
	##########################