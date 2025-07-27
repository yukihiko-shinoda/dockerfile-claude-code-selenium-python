variable "DOCKER_TAG" {
}
target "claude-code-selenium-python" {
  tags = [
    "futureys/claude-code-selenium-python:latest",
    "futureys/claude-code-selenium-python:${DOCKER_TAG}",
  ]
}