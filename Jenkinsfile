pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/Neharaj08/nginx-log-analyzer.git'
            }
        }

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
