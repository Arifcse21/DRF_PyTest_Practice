pipeline {
  agent any

  stages {
//     stage('Install Requirements') {
//       steps {
// //         git 'https://github.com/your-repo-url.git'
//         sh 'pip install -r requirements.txt'
//       }
//     }
//
//     stage("Unit Test"){
//         steps {
//             sh 'pytest -sv'
//         }
//     }

//     stage('Database Migration') {
//       steps {
//         sh 'python3 manage.py makemigrations'
//         sh 'python3 manage.py migrate'
//       }
//     }

    stage('Docker Compose') {
      steps {
        sh 'docker-compose up -d --build --remove-orphans'
      }
    }
  }
}
