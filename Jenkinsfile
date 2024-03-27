node {
    stage('SCM') {
        git branch: 'main', credentialsId: '25102004', url: 'https://github.com/chutrunganh/Demo_For_Project1.git'
    }
    stage('SonarQube Analysis') {
            def scannerHome = tool 'SonarQube Scanner';
            withSonarQubeEnv() {
                sh "${scannerHome}/bin/sonar-scanner -Dsonar.host.url=http://sonar:9000/ -Dsonar.java.binaries=. -Dsonar.projectKey=Demo_For_Project1 -Dsonar.login=sqa_997f560e37bd8883338eb27016f266f2385a5eae"
        }
    }
}

