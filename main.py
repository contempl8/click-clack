import click

@click.group()
def cli():
    pass

@click.command()
@click.option('--speed',default=100,help='The fast speed')
@click.option('-d','--distance',default=298.65,required=True,show_default=True, 
              type=click.FloatRange(0.0,525.5))
@click.argument('noise',type=click.STRING)
@click.argument('heat',type=click.Choice(['mild','medium','Hot','Hotter','HOTTEREST'],case_sensitive=True))
def fast(speed,noise,heat,distance):
    click.echo("You chose to go fast")
    click.echo(f'This speed: {speed}, this noise: {noise}, and this heat: {heat}')
    click.echo(f'Your distance: {distance}')

@click.command()
def slow():
    click.echo("You chose to go slow")

@click.command()
def hello():
    click.echo("Print Hello")

cli.add_command(fast)
cli.add_command(slow)
cli.add_command(hello)

if __name__ == "__main__":
    cli()
