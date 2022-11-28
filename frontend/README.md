# Tief-gang-list Frontend

These are the frontend technologies we're using:

- [Npm](https://www.npmjs.com/) for package management.
- [Typescript](https://www.typescriptlang.org/) as a language.
- [Parcel](https://parceljs.org/) to bundle the frontend.
- [React](https://reactjs.org/) as a frontend framework.

Dev tools:

- [eslint](https://eslint.org/) A Typescript/Javascript linter.
- [tsc](https://www.typescriptlang.org/docs/handbook/compiler-options.html) the typescript compiler to check if we have valid typescript.
- [openapi-typescript-codegen](https://www.npmjs.com/package/openapi-typescript-codegen) A code generator, which generates the api interaction code for us from the FastAPI Swagger definition.

## Workflows

- `just setup` to install dependencies.
- `just run` to start a local webserver that hosts the frontend.
- `just lint` Check for any lintint errors. Also executed in our CI.
- `just format` Try to auto-format stuff.
- `just build-api` Build the typescript code to interact with our backend. Needs a running backend instance.
