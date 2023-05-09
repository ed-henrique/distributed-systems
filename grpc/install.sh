echo "Creating images..."

docker build -q -t client:eduardo_machado -f ./client/Dockerfile . > /dev/null &
docker build -q -t server:eduardo_machado -f ./server/Dockerfile . > /dev/null &
wait

echo "Images created:"
docker images | grep 'eduardo_machado'