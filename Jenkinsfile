pipeline {
  agent any

  environment {
    DOCKER_REGISTRY = "docker.io"
    DOCKER_REPO     = "vaishnavi873/flask-app"   // change if needed
    IMAGE_TAG       = "${env.BUILD_NUMBER}"
    FULL_TAG        = "${DOCKER_REPO}:${IMAGE_TAG}"
    LATEST_TAG      = "${DOCKER_REPO}:latest"
  }

  options {
    buildDiscarder(logRotator(numToKeepStr: '20'))
    timestamps()
  }

  stages {
    stage('Checkout') {
      steps { checkout scm }
    }

    stage('List workspace') {
      steps {
        script {
          if (isUnix()) { sh 'ls -la' } else { bat 'dir' }
        }
      }
    }

    stage('Build Docker image') {
      steps {
        script {
          if (isUnix()) {
            sh "docker build -t ${FULL_TAG} ."
            sh "docker tag ${FULL_TAG} ${LATEST_TAG}"
          } else {
            bat "docker build -t ${FULL_TAG} ."
            bat "docker tag ${FULL_TAG} ${LATEST_TAG}"
          }
        }
      }
    }

    stage('run tests') {
      steps {
        script {
          if (isUnix()) {
            sh "docker run --rm ${FULL_TAG} python -m unittest discover -s tests"
          } else {
            bat "docker run --rm ${FULL_TAG} python -m unittest discover -s tests"
          }
        }
      }
    }
  post {
    success { echo "Docker pushed: ${FULL_TAG} and ${LATEST_TAG}" }
    failure { echo "Pipeline failed — check console log" }
    always {
      script {
        if (isUnix()) { sh "docker images | head -n 50 || true" } else { bat "docker images | more" }
      }
    }
  }
}
