pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo "Would run: docker build -t hello-devops-python:${BUILD_NUMBER} ."
            }
        }

        stage('Test') {
            steps {
                echo "Would run: docker run --rm hello-devops-python:${BUILD_NUMBER} pytest or unit tests"
            }
        }

        stage('Deploy') {
            steps {
                echo "Would run: docker run -d -p 5001:5000 --name hello-app-${BUILD_NUMBER} hello-devops-python:${BUILD_NUMBER}"
            }
        }
    }

    post {
        always {
            echo "Would run: docker stop/rm hello-app-${BUILD_NUMBER}"
        }
    }
}
