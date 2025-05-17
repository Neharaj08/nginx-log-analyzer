pipeline {
    agent {
        docker {
            image 'docker:latest'  // docker CLI official image
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    stages {
        stage('Pull and Run Image') {
            steps {
                sh 'docker pull neharaj08/nginx-log-analyzer:latest'
                sh 'docker run --rm neharaj08/nginx-log-analyzer:latest'
            }
        }
    }
}
