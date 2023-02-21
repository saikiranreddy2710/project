pipeline {
    agent any
    
    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t my-image1 .'
            }
        }
        
        stage('Run Docker Container') {
            steps {
                sh 'docker run -p 8880:80 my-image1'
            }
        }
    }
}
