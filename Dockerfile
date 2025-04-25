- name: Build Docker image
  uses: docker/build-push-action@v5
  with:
    context: .
    file: ./Dockerfile  # ya no es necesario poner docker/Dockerfile
    push: true
    tags: ghcr.io/japipe05/jave_smart_yml:main
