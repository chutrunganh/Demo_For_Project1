node {
    stage('SCM') {
        git branch: 'main', credentialsId: '25102004', url: 'https://github.com/chutrunganh/Demo_For_Project1.git'
    }
    stage('SonarQube Analysis') {
            def scannerHome = tool 'SonarQube Scanner';
            withSonarQubeEnv() {
                sh "${scannerHome}/bin/sonar-scanner -Dsonar.host.url=http://localhost:9000/ -Dsonar.java.binaries=. -Dsonar.projectKey=Demo_For_Project1 -Dsonar.login=sqa_c4975010fa662a570789ca41db89d06b0cba640a"
        }
    }
}

