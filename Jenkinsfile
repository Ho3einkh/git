pipeline {
    parameters {
        choice(name: 'VERSION', choices: ['v1.0', 'v1.1', 'v1.2', 'v1.3'], description: 'versions of package')
        booleanParam(name: 'executeTest', defaultValue: true, description: 'Test')
    }
    environment {
        // The MY_TOKEN environment variable will be assigned
        // the value of a temporary file.
        // minimum requirments for access token are
        // repo and read:org, make sure to give access to these privileges 
        MY_TOKEN = credentials('myToken1')
    }
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            when {
                expression {
                    params.executeTest == true
                }
            }
            steps {
                sh 'python3 test.py'
            }
        }
        stage('Deploy') {
            steps {
                echo "Deploying Version: ${params.VERSION}"
                // do Authentication
                sh("gh auth login --with-token < ${MY_TOKEN}")
                // Create Next Release
                sh("gh release create ${params.VERSION}")
            }
        }
    }
}

// def version(){
//     versions = sh(returnStdout: true, script: "git tag --sort version:refname | tail -1").trim()
//     return versions
// }