ppp=`docker ps -a | grep "treehouse" | cut -c 1-10` 
echo $ppp
docker stop $ppp | xargs docker rm
docker rmi  treehouse:latest
./docker_build.sh
./docker_run.sh
docker ps -a | grep treehouse
