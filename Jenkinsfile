// Scripted 문법으로 작성
node {
    // 변수 선언
    def app

    // scm에서 소스코드 체크아웃 받음
    // jenkins pipeline 설정 시 구성한 git repository를 '/var/lib/jenkins/workspace/{job name}' 위치로 Clone 함
    stage('Clone repository') {
        checkout scm
    }

    // Dockerfile과 애플리케이션 코드를 통해 컨테이너화된 이미지를 '{aws ecr url}/{aws ecr repository name}'이라는 이름으로 이미지 빌드
    // 아래의 Push image 단계에서 이미지 태그 설정
    stage('Build image') {
       app = docker.build("234311324580.dkr.ecr.ap-northeast-2.amazonaws.com/ecr")
    }

    // 사용자 정의 Docker Registry를 사용하려면 withRegistry() 사용 필요
    // ecr:ap-northeast-2:ecr-credentials은 jenkins에 등록한 AWS Credential 이름
    // BUILD_NUMBER는 Jenkins의 기본 환경 변수로 현재 Jenkins의 빌드 번호를 의미, push() 안에 있는 Jenkins 빌드 번호로 이미지 태그가 지정된 후 ecr로 push
    stage('Push image') {
        docker.withRegistry('https://234311324580.dkr.ecr.ap-northeast-2.amazonaws.com/ecr', 'ecr:ap-northeast-2:ecr-credentials') {
            app.push("${env.BUILD_NUMBER}")
        }
    }
    
    stage('Trigger ManifestUpdate') {
                // Jenkins 작업 콘솔에 출력되는 메시지
                echo "triggering updatemanifestjob"
        
                // 새로운 Jenkins Job을 트리거 하는 명령어
                // 현재 Job이 끝나면 'updatemanifest'라는 job을 트리거하고, env.BUILD_NUMBER 파라미터를 DOCKERTAG'이라는 이름으로 전달
                build job: 'updatemanifest', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER)]
    }
}
