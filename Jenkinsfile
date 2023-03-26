pipeline {
  agent any

  stages {
    stage('Build') {
      steps {
//         git 'https://github.com/your-repo-url.git'
        sh 'pip install -r requirements.txt'
      }
    }

    stage('Database Migration') {
      steps {
        sh 'python manage.py makemigrations'
        sh 'python manage.py migrate'
      }
    }

    stage('Docker Compose') {
      steps {
        sh 'docker-compose up -d'
      }
    }
  }
}
