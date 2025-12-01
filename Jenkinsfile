#!/usr/bin/env groovy
/**
 * Jenkinsfile for Bazel Calculator Project
 * 
 * This pipeline:
 * 1. Checks out the repository
 * 2. Verifies dependencies (Python, Bazel)
 * 3. Executes the Python build executor
 * 4. Reports build status
 */

pipeline {
    agent any
    
    options {
        timeout(time: 1, unit: 'HOURS')
        timestamps()
        buildDiscarder(logRotator(numToKeepStr: '10'))
    }
    
    stages {
        stage('Checkout') {
            steps {
                script {
                    echo "📋 Checking out repository..."
                    checkout scm
                }
            }
        }
        
        stage('Environment Check') {
            steps {
                script {
                    echo "🔍 Checking build environment..."
                    sh '''
                        echo "Current Directory: $(pwd)"
                        echo "Python Version: $(python3 --version)"
                        echo "Bazel Version: $(bazel --version)"
                        echo "Repository Contents:"
                        ls -la
                    '''
                }
            }
        }
        
        stage('Build') {
            steps {
                script {
                    echo "🔨 Starting Bazel build..."
                    sh '''
                        echo "================================"
                        echo "BAZEL BUILD EXECUTOR"
                        echo "================================"
                        python3 build_executor.py
                        echo "================================"
                        echo "Build completed successfully"
                        echo "================================"
                    '''
                }
            }
        }
    }
    
    post {
        success {
            script {
                echo "✅ Pipeline completed successfully"
            }
        }
        failure {
            script {
                echo "❌ Pipeline failed"
            }
        }
        always {
            script {
                echo "Pipeline execution finished"
            }
        }
    }
}
