pipeline {
    parameters {
        choice(name: 'VERSION', choices: ['v1.0', 'v1.1', 'v1.2', 'v1.3'], description: 'versions of package')
        booleanParam(name: 'executeTest', defaultValue: true, description: 'Test')
    }
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh('gh --version')
                // GIT_COMMIT_EMAIL = sh (
                //         script: 'git tag --sort version:refname',
                //         returnStdout: true
                //     ).trim()
                // echo "Git committer email: ${GIT_COMMIT_EMAIL}"
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
                withCredentials([file(credentialsId: 'myToken1', variable: 'TOKEN')]) {
                    sh("gh auth login --with-token < $TOKEN")
                    sh("gh release create ${params.VERSION}")
                }
            }
        }
    }
}

// def version(){
//     versions = sh(returnStdout: true, script: "git tag --sort version:refname | tail -1").trim()
//     return versions
// }