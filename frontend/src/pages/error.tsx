import { useRouteError } from "react-router-dom";

// The type bindings for `useRouteError` are `unknown`.
// We create our own Typescript bindings to please the compiler.
interface ErrorInterface {
  statusText: string;
  message: string;
}

function ErrorPage() {
    const error = useRouteError() as ErrorInterface;
    console.error(error);

    return (
        <div id="error-page">
            <h1>Oops!</h1>
            <p>Sorry, an unexpected error has occurred.</p>
            <p>Please contact either Merle or Arne :))</p>
            <p>
                <i>{error.statusText || error.message}</i>
            </p>
        </div>
    );
}

export default ErrorPage;
