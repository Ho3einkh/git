pipeline {
    parameters {
        choice(name: 'VERSION', choices: ['1.0', '1.1', '1.2'], description: 'versions of package')
        booleanParam(name: 'executeTest', defaultValue: true, description: 'Test')
    }
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh("git tag --sort version:refname | tail -1")
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
                echo 'Deploying....'
                // sh "gh release create ${params.VERSION}"
                echo "Deploying Version: ${params.VERSION}"
            }
        }
    }
}

// def version(){
//     versions = sh(returnStdout: true, script: "git tag --sort version:refname | tail -1").trim()
//     return versions
// }