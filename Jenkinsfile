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

        stage('Test Docker') {
            steps {
                bat 'whoami'
                bat 'docker --version'
                bat 'docker info'
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
            archiveArtifacts artifacts: 'report.html, report.csv', allowEmptyArchive: true
        }
    }
}