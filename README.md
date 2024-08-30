🚨 This repo is for the purpose of interviewing applicants for backend roles at Pantheon.

🚨 There are many issues to be found across the entire repo, and you should feel free to focus on any area that interests you.

🚨 Your interviewer will be available to help you with any questions you have.

🚨 Use any IDE or tools you are comfortable with, and feel free to use any libraries you want.

# Authentication Service

## Pre-requisites

- [Devbox](https://www.jetify.com/devbox)

## Quickstart

```
curl -fsSL https://get.jetify.com/devbox | bash
devbox shell
task init-local
task run-local
```

## Devbox

Devbox is a tool that helps you manage your development environment. It will install all the necessary dependencies and tools for you to develop on this project.

Once you have entered into a devbox shell, the following tools will be available:

- python 3.12
- [go-task](https://taskfile.dev)
- [poetry](https://python-poetry.org/)

Linting, formatting, and type checking tools are available as tasks:

```
task fmt
task lint
task type-check
```

These three commands can also be run in a single command `task preflight`.

## Tests

Tests can be run with the `task test` command.

## Running the service

The service can be run with the `task run-local` command.

