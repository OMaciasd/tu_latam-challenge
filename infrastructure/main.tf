resource "docker_image" "rabbitmq" {
  name = "rabbitmq:management"
}

resource "docker_container" "rabbitmq" {
  name  = "rabbitmq"
  image = docker_image.rabbitmq.name

  ports {
    internal = 5672
    external = 5672
  }

  ports {
    internal = 15672
    external = 15672
  }

  env = [
    "RABBITMQ_DEFAULT_USER=user",
    "RABBITMQ_DEFAULT_PASS=password"
  ]
}

resource "docker_image" "postgres" {
  name = "postgres:latest"
}

resource "docker_container" "postgres" {
  name  = "postgres"
  image = docker_image.postgres.name

  ports {
    internal = 5432
    external = 5432
  }

  env = [
    "POSTGRES_USER=myuser",
    "POSTGRES_PASSWORD=mypassword",
    "POSTGRES_DB=mydatabase"
  ]
}

resource "docker_image" "api" {
  name = "flask-api"
  build {
    context = "${path.root}/src"
    tag     = ["flask-api:latest"]
    label = {
      author : "omaciasd"
    }
  }
  triggers = {
    dir_sha1 = sha1(join("", [for f in fileset(path.module, "src/*") : filesha1(f)]))
  }
}

resource "docker_container" "api" {
  name  = "flask-api"
  image = docker_image.api.name

  ports {
    internal = 50010
    external = 50010
  }

  depends_on = [docker_container.postgres]
}
