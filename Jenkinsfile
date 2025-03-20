pipeline {
    agent any
    
    environment {
            
            GITHUB_TOKEN= credentials('github_token')

    }

    stages {
        stage('Pre-commit'){
            steps {
                
                echo '####### Pre-commit stage ######\n'
                sh 'whoami'



            }

        }
    }


}