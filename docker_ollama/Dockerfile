# https://hub.docker.com/_/python
FROM ollama/ollama

COPY ./download_model.sh .

# Install production dependencies.
#RUN ["/bin/bash", "-c", "echo Hello, World."]
RUN chmod +x download_model.sh
RUN ./download_model.sh

#to shell into the container
#runthe the image
#docker build -t myollama .
#docker run -p 11434:11434 -d myollama 
#docker ps

#docker exec -it <container-id-or-name> bash

#remove the container
#docker rm 


