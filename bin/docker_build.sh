if [ -f  ../Dockerfile ] 
then
   docker build -f ../Dockerfile -t treehouse ..
elif [ -f  ./Dockerfile ] 
then
   docker build -f ./Dockerfile -t treehouse ..
else
   echo "No docker file to build. Check directory structure"
fi
