pipeline {
  agent {
    docker {
      image 'docker:latest'
      args '-v /var/run/docker.sock:/var/run/docker.sock'
    }
  }
  stages {
    stage('Run Docker commands') {
      steps {
        sh 'docker pull neharaj08/nginx-log-analyzer:latest'
        sh 'docker inspect neharaj08/nginx-log-analyzer:latest'
      }
    }
  }
}
