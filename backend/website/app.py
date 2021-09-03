import click
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


index_vars = dict(
    title="Beam",
    description="A file sharing service.",
    heading="Beam - File Sharing Made Easy",
)


@app.route("/")
def index():
    return render_template("index.html", **index_vars)


@click.option(
    "-h",
    "--host",
    default="0.0.0.0",
)
@click.option("-p", "--port", default=5000, type=int)
@click.command()
def start_server(host, port):
    app.run(host=host, port=port)


if __name__ == "__main__":
    start_server()
