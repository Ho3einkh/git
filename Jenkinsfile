pipeline {
    environment { 
        CC = sh(script: 'git tag --sort version:refname')
    }
    parameters {
        choice(name: 'VERSION', choices: ['0.1'], description: 'versions of package')
        booleanParam(name: 'executeTest', defaultValue: true, description: 'Test')
    }
    agent any

    stages {
        stage('Build') {
            steps {
                echo "Building.. ${CC}"
                // GIT_COMMIT_EMAIL = sh (
                //         script: 'git tag --sort version:refname',
                //         returnStdout: true
                //     ).trim()
                // echo "Git committer email: ${GIT_COMMIT_EMAIL}"
                // sh(script: 'git tag --sort version:refname')
                // def output = sh returnStdout: true, script: 'git tag --sort version:refname'
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