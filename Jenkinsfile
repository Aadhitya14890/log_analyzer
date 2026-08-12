pipeline {

    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest --junitxml=test-results.xml'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t log-analyzer:%BUILD_NUMBER% .'
            }
        }

        stage('Verify Docker Image') {
            steps {
                bat 'docker images log-analyzer'
            }
        }

        stage('Docker Tests') {
            steps {
                bat 'docker run --rm log-analyzer:%BUILD_NUMBER% python -m pytest'
            }
        }

        stage('Run Application') {
            steps {
                bat 'docker run --rm log-analyzer:%BUILD_NUMBER% python main.py application.log'
            }
        }
    }
    
    post {
        always {
            junit 'test-results.xml'
            bat 'docker image prune -f'
        }
    }
}