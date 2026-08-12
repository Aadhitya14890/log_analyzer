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

        stage('Generate Report') {
            steps {
                bat 'python main.py application.log'
            }
        }
    }
    
    post {
        always {
            junit 'test-results.xml'
        }
    }
}