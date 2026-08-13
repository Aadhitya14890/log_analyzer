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

        stage('Push Docker Image') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-credentials',
                        usernameVariable: 'DOCKER_USERNAME',
                        passwordVariable: 'DOCKER_PASSWORD'
                    )
                ]) {
                    bat 'docker login -u "%DOCKER_USERNAME%" -p "%DOCKER_PASSWORD%"'
                    bat 'docker tag log-analyzer:%BUILD_NUMBER% %DOCKER_USERNAME%/log-analyzer:%BUILD_NUMBER%'
                    bat 'docker push %DOCKER_USERNAME%/log-analyzer:%BUILD_NUMBER%'
                }
            }
        }

        stage('Deploy Container') {
            steps {
                bat '''
                docker pull aadhitya14890/log-analyzer:%BUILD_NUMBER%

                docker stop log-analyzer-container 2>NUL || exit /B 0
                docker rm log-analyzer-container 2>NUL || exit /B 0

                docker run --name log-analyzer-container aadhitya14890/log-analyzer:%BUILD_NUMBER% python main.py application.log
                '''
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
            
        }
    }
}