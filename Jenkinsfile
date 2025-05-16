pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('nginx-log-analyzer')
                }
            }
        }

        stage('Run Analyzer') {
            steps {
                script {
                    docker.image('nginx-log-analyzer').run('--rm')
                }
            }
        }
    }
}
