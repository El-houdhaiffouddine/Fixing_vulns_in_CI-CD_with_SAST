pipeline {
    agent any
    
    environment {
            
            GITHUB_TOKEN= credentials('github_token')
            SEMGREP_APP_TOKEN = credentials('SEMGREP_APP_TOKEN')

    }

    stages {
        stage('Scan for secret with Talisman and Trufflehog'){
            steps {
                
                echo '***** Scan for secrets with Trufflehog *****\n'
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
                echo '***** Static Analysis with Bandit *****\n'

                script {
                def result = sh(script:'/home/user1/flask/bin/bandit -r /var/lib/jenkins/workspace/DevSecOps/', returnStatus:true)
                    if(result !=0){
                       error('Security vulnerabilities has been reported ... !')
                    }
                }
            
            }
        }

        //stage('SAST with semgrep') {

          //  steps {

            //    echo 'Static Analysis with Semgrep'

                 
              //  sh ''' docker pull semgrep/semgrep && \
                  //     docker run --rm -v "${PWD}:/src" -e SEMGREP_APP_TOKEN=${SEMGREP_APP_TOKEN} \
                    //   --workdir ${PWD} semgrep/semgrep semgrep ci'''
                //}
            //}

       // stage('SCA with OWASP Dependency Check'){

         //    steps {

           //      echo 'Software Composition Analysis ....'

                 //dependencyCheck additionalArguments:  '--scan /var/lib/jenkins/workspace/DevSecOps/ --format xml',
                   //              odcInstallation: 'owasp-dependency-check'
                
             //}     
                 

       // }

        stage('Building a Docker container') {

            steps {

                echo '***** Building the docker image with Docker *****'

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

                echo '***** Scanning the docker image for security issues with Trivy *****'
                script {
                def result = sh(script:'trivy image --security-checks vuln,config flask-app:1.0.0',returnStatus:true)
                
                if(result!=0){
                    error('Security issues has been reported ... !')
                }

                }
            }
        }

        stage('Deployment with Docker Compose') {

            steps {

                echo '***** Deployment of the Flask App with Docker Compose *****'
                sh 'docker compose up -d'
            }
        }


        stage('DAST with OWASP ZAP'){

            steps {

                echo '***** Scanning dynamically the Flask APP for security issues with ZAP *****'

                script {

                    def result = sh(script: '/home/user1/Downloads/ZAP_2.16.1/zap.sh -cmd -port 8085 -quickurl http://192.168.1.2:8081/ -quickout /var/lib/jenkins/workspace/DevSecOps/report.html',returnStatus:true)

                    if (result != 0){

                        error('OWASP ZAP has reported a security issues ... !')
                    }
                }
                
            }
        }

    }

    post {

       // always {
                 
         //        echo 'Dependency Check Publisher'
               //  dependencyCheckPublisher pattern: 'dependency-check-report.xml',
                 //                    failedTotalCritical: 1,
                   //                  failedTotalHigh: 1,
                     //                failedTotalLow: 1, 
                       //              stopBuild: true

       // }

        failure {

            mail to: 'bensidi.elhoudhaiffouddine@esprit.tn',
                 from: 'Google Security',
                 subject: '[Urgent] Security Alert !',
                 mimeType: 'text/html', 
                 body: 'Security vulnerabilities has been reported. Please look in the Jenkins Console for more informations. Thanks !'            


        }
    }


}