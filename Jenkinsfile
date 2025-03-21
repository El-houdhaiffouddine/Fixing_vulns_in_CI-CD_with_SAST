pipeline {
    agent any
    
    environment {
            
            GITHUB_TOKEN= credentials('github_token')

    }

    stages {
        stage('Pre-commit'){
            steps {
                
                echo '####### Pre-commit stage ######\n'
                echo 'Cheking for secrets ...\n'
                sh 'trufflehog github --repo=https://github.com/El-houdhaiffouddine/Python_with_Flask.git --results=verified,unknown --token=${GITHUB_TOKEN}'
                


            }

        }

        stage('SAST with bandit'){
            steps {
                echo '###### Static Analysis with Bandit #######\n'

                script {
                    def result = sh(script:'/home/user1/flask/bin/bandit -r /var/lib/jenkins/workspace/DevSecOps/',returnStatus:true)
                    
                }
            
            }
        }

        stage('SCA with OWASP Dependency Check'){

             steps {
                 echo 'Software Composition Analysis ....'
             }     
                 

        }

        stage('Email'){

            steps {
                 
                 emailext replyTo: 'bensidi.elhoudhaiffouddine@esprit.tn',
                          subject: '[Urgent] Security Alert !',
                          body: 'A secuity issues has been reported. Please look in your Jenkins Console.',
                          mimeType: 'text/html'


            }
        }
    }

    post {

        failure {

            echo 'Test'            


        }
    }


}