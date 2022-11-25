pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/Chinthan23/primality-testing.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x primality.py"
                sh "./primality.py"
            }
        }
        stage('Test Set') {
            steps {
                sh "chmod u+x unittest1.py"
                sh "./unittest1.py"
            }
        }
        // stage('Test Set') {
        //     steps {
        //         sh "chmod u+x unittest2.py"
        //         sh "./unittest2.py"
        //     }
        // }
    } 
}