pipeline {
    agent any
 
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/your-username/weather-aggregator.git'
            }
        }
 
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
 
        stage('Run Tests') {
            steps {
                sh 'pytest --maxfail=1 --disable-warnings -q'
            }
        }
 
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t weather-aggregator .'
            }
        }
 
        stage('Deploy') {
            steps {
                sh 'docker run -d -p 8000:8000 weather-aggregator'
            }
        }
    }
}