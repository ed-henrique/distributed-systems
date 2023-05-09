echo "Removing images and containers that use them..."

image_tag='eduardo_machado'

if docker ps -a | grep "${image_tag}" > /dev/null; then
  docker ps -a | grep "${image_tag}" | awk '{print $1}' | xargs docker rm -f > /dev/null
  echo "Containers using image ${image_tag} have been removed."
else
  echo "No containers using image ${image_tag} were found."
fi

if docker images | grep "${image_tag}" > /dev/null; then
  docker image rm "client:${image_tag}" "server:${image_tag}" > /dev/null
  echo "Images with the tag ${image_tag} have been removed."
else
  echo "No images using the tag ${image_tag} were found."
fi

echo "Images and containers removed!"