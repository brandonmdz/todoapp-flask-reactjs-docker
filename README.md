# todoapp-flask-reactjs-docker

This is a Dockerized simple TO-DO list application developed with Flask/Python (Backend) and ReactJS (Frontend) with Dockerfiles provided for both components. Credit goes to the original creator of the app . Please note that in the frontend's `.env` file, you need to specify the host IP where you plan to run it.

## Requirements

- Docker and Docker Compose must be installed on your system.

## Usage

- 1: Clone the repository to your local machine:

   ```
   $ git clone https://github.com/brandonmdz/todoapp-flask-reactjs-docker.git
   $ cd todoapp-flask-reactjs-docker
   ```

- 2: Configure the frontend's .env file:

Open the .env file located in the frontend folder and set the host IP where you plan to run the application:
   ```
    VITE_API_URL=http://your-ip-here:5000
   ```
- 3: Start the application:
  
```
$ docker-compose up -d
   ```

This will build the images and run the containers for both the frontend and backend.

- 4: Access the application:

Open your web browser and go to http://your-host-ip:5173 to use the application.

## Credits
This application is based on the original work by [Remy349](https://github.com/Remy349 "Remy349"). You can find the original project [here](https://github.com/Remy349/todo-app-flask-reactjs "here").
