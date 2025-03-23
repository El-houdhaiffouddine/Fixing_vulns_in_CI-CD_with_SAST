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
                    //if(result !=0){
                     //   error('Security vulnerabilities has been reported ... !')
                    //}
                }
            
            }
        }

        stage('SCA with OWASP Dependency Check'){

             steps {

                 echo 'Software Composition Analysis ....'

                 dependencyCheck additionalArguments:  '--scan /var/lib/jenkins/workspace/DevSecOps/',
                                 format: 'html',
                                 odcInstallation: 'owasp-dependency-check'
                
             }     
                 

        }

    }

    post {

        always {

            
                 dependencyCheckPublisher pattern: 'dependency-check-report.html',
                                     failedTotalCritical: 1,
                                     failedTotalHigh: 1,
                                     failedTotalLow: 1, 
                                     stopBuild: true

        }

        failure {

            mail to: 'bensidi.elhoudhaiffouddine@esprit.tn',
                 from: 'Google Security',
                 subject: '[Urgent] Security Alert !',
                 mimeType: 'text/html',
              d Py  
                 body: 'Security vulnerabilities has been reported. Please look in the Jenkins Console for more informations. Thanks !'            


        }
    }


}