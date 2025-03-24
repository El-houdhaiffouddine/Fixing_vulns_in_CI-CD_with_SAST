pipeline {
    agent any
    
    environment {
            
            GITHUB_TOKEN= credentials('github_token')
            SEMGREP_APP_TOKEN = credentials('SEMGREP_APP_TOKEN')

    }

    stages {
        stage('Scan for secret with Talisman and Trufflehog'){
            steps {
                
                echo '####### Pre-commit stage ######\n'
                echo 'Cheking for secrets ...\n'
                script {

                 def result = sh(script:'trufflehog github --repo=https://github.com/El-houdhaiffouddine/Python_with_Flask.git --results=verified,unknown --token=${GITHUB_TOKEN}',returnStatus:true)
                
                 if(result != 0){

                    error('Security vulnerabilities has been reported ... !')
                 }
                 
                }


            }

        }

        stage('SAST with bandit'){
            steps {
                echo '###### Static Analysis with Bandit #######\n'

                script {
                def result = sh(script:'/home/user1/flask/bin/bandit -r /var/lib/jenkins/workspace/DevSecOps/', returnStatus:true)
                    if(result !=0){
                       error('Security vulnerabilities has been reported ... !')
                    }
                }
            
            }
        }

        stage('SAST with semgrep') {

            steps {

                script {
                    def result = sh(script: '/home/user1/flask/semgrep ci',returnStatus=true)
                    if(result != 0){
                        error('Security issues has been reported by Semgrep !')
                    }
                }
            }
        }

       // stage('SCA with OWASP Dependency Check'){

         //    steps {

           //      echo 'Software Composition Analysis ....'

                 //dependencyCheck additionalArguments:  '--scan /var/lib/jenkins/workspace/DevSecOps/ --format xml',
                   //              odcInstallation: 'owasp-dependency-check'
                
             //}     
                 

       // }

        stage('Building a Docker container') {

            steps {

                echo 'Building the docker image ...'

                script {

                 def result = sh(script: 'docker build -t flask-app:1.0.0 /var/lib/jenkins/workspace/DevSecOps/', returnStatus:true)
                
                 if(result !=0){

                    error('Security issues has been reported !')
                 }

                }
            }
        }

        stage('Scan Docker image with trivy'){

            steps {

                echo 'Scanning the docker image for security issues ...'
                script {
                def result = sh(script:'trivy image --security-checks vuln,config flask-app:1.0.0',returnStatus:true)
                
                if(result!=0){
                    error('Security issues has been reported ... !')
                }

                }
            }
        }


        stage('DAST with OWASP ZAP'){

            steps {

                echo 'Scanning dynamically the Flask APp for security issues ...'
                script {

                    def result = 
                }
            }
        }

    }

    post {

        always {
                 
                 echo 'Dependency Check Publisher'
               //  dependencyCheckPublisher pattern: 'dependency-check-report.xml',
                 //                    failedTotalCritical: 1,
                   //                  failedTotalHigh: 1,
                     //                failedTotalLow: 1, 
                       //              stopBuild: true

        }

        failure {

            mail to: 'bensidi.elhoudhaiffouddine@esprit.tn',
                 from: 'Google Security',
                 subject: '[Urgent] Security Alert !',
                 mimeType: 'text/html', 
                 body: 'Security vulnerabilities has been reported. Please look in the Jenkins Console for more informations. Thanks !'            


        }
    }


}