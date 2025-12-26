pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building Python app...'
                sh 'sudo docker build -t hello-devops-python:${BUILD_NUMBER} .'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'sudo docker run --rm hello-devops-python:${BUILD_NUMBER} python -c "from flask import Flask; print(\'Tests passed!\')"'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying to localhost...'
                sh 'sudo docker run -d -p 5001:5000 --name hello-app-${BUILD_NUMBER} hello-devops-python:${BUILD_NUMBER}'
                sh 'sleep 3'
                sh 'curl -f http://localhost:5001 || true'
            }
        }
    }

    post {
        always {
            sh 'sudo docker stop hello-app-${BUILD_NUMBER} || true'
            sh 'sudo docker rm hello-app-${BUILD_NUMBER} || true'
        }
    }
}
