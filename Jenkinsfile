pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    // Build the Docker image
                    def dockerImage = docker.build('my-fastapi-app', '-f Dockerfile .')
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    // Run the Docker container
                    docker.image('my-fastapi-app').withRun('-p 8088:80') {
                        echo 'The FastAPI application is now running on http://localhost:8088'
                    }
                }
            }
        }
    }
}
