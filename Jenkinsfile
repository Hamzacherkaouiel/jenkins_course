pipeline {

    agent { 
        node {
            label 'docker-test'
            }
      }
      triggers {
                  pollSCM('*/1 * * * *')
              }

    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                cd myapp
                python3 -m venv venv
                source venv/bin/activate
                pip3 install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                cd myapp
                source venv/bin/activate
                python3 hello.py
                python3 hello.py --name=hamza
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}