pipeline {
    agent {
        docker {
            image 'neharaj08/nginx-log-analyzer:latest'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/Neharaj08/nginx-log-analyzer.git'
            }
        }

        stage('Run Analyzer') {
            steps {
                sh './nginx-log-analyzer.sh'
            }
        }
    }
}
