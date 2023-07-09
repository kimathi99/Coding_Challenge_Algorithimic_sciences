# Use the official NGINX image as the base image
FROM nginx:latest

# Set the working directory inside the container
WORKDIR /app

# Copy the NGINX configuration file to the container
COPY nginx.conf /etc/nginx/nginx.conf

# Copy the available_sites directory to the container
COPY available_sites /etc/nginx/available_sites

# Expose the port that NGINX will listen on
EXPOSE 80
EXPOSE 443

# Start NGINX with SSL certificate based on environment variable
CMD ["/bin/sh", "-c", "envsubst < /etc/nginx/nginx.conf > /etc/nginx/nginx.conf && nginx -g 'daemon off;'"]
