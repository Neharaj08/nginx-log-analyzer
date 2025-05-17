pipeline {
    agent any

    stages {
        stage('Pull and Run Image') {
            steps {
                sh 'docker pull neharaj08/nginx-log-analyzer:latest'
                sh 'docker run --rm neharaj08/nginx-log-analyzer:latest'
            }
        }
    }
}
