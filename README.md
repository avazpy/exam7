                                    1-variant
docker start
docker build -t exam7:latest .
docker run --name exam_container -p 8005:8005 exam7:latest
docker compose up --build
docker exec -it 56c python3 manage.py migrate
docker compose run exam_service python3 manage.py migrate
