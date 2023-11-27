import click

@click.command()
@click.argument('num1', type=int)
@click.argument('num2', type=int)
def main(num1, num2):
    """Simple program that adds two numbers."""
    result = num1 + num2
    click.echo(f"The sum of {num1} and {num2} is {result}")

if __name__ == '__main__':
    main()