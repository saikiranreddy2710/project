pipeline {
    agent any
    
    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t my-image .'
            }
        }
        
        stage('Run Docker Container') {
            steps {
                sh 'docker run -p 8081:80 my-image'
            }
        }
    }
}
