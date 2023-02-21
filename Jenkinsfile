pipeline {
    agent {
        docker {
            image 'my-image:latest'
            args '-p 8081:80'
            platform 'linux/amd64'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'echo "Build step"'
            }
        }
        stage('Test') {
            steps {
                sh 'echo "Test step"'
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo "Deploy step"'
            }
        }
    }
}
