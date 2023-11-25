# Stage 1: Clone the repository and build the application
FROM node:18

# Set the working directory inside the container
WORKDIR /app

# Install Git
RUN apt-get update && \
    apt-get install -y git npm 

# Clone the public repository
RUN git clone https://github.com/DuckAI-hackthon/duckMicroservice-hercai.git

WORKDIR /app/duckMicroservice-hercai

# Install project dependencies
RUN yarn

# Copy the rest of the application code to the working directory
COPY . .

# Expose port 3000
EXPOSE 3000

# Command to run the application
CMD ["yarn", "dev"]