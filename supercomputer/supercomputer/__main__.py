"""Define the command-line interface for the supercomputer program."""

# TODO: import the typer package for creating command-line arguments


# TODO: import the compute module from the supercomputer package


def main(
    # TODO: Add a required argument called "function" with no default value
    start: int = typer.Option(1, min=1, max=100000),
    stop: int = typer.Option(10, min=1, max=100000),
):
    """Compute the mapping of a list of numbers."""
    # display the debugging output for the program's command-line arguments
    typer.echo("")
    typer.echo(
        f"Using a range of values between and inclusive {start} and an exclusive {stop}! 💻"
    )
    typer.echo("")
    typer.echo(f"The name of the function is {function}")
    typer.echo("")
    # TODO: construct the requested function from the compute module
    # Reference: https://stackoverflow.com/questions/3061/calling-a-function-of-a-module-by-using-its-name-a-string
    # TODO: apply the requested function to all of the generated data
    # Reference: https://realpython.com/python-map-function/
    # display debugging information with the function's output
    typer.echo(f"  This is the output from the {function} function:")
    typer.echo("")
    # display the output from the computation
    print("  " + str(list(result)))
    typer.echo("")

    # display a final message and some extra spacing
    typer.echo("Wow, computing with higher-order functions is fun! 😃")
    typer.echo("")


if __name__ == "__main__":
    # TODO: Call the main function to start the parsing of the
    # command-line arguments and then the execution of the program
    typer.run(main)
