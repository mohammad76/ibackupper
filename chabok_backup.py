import json
import os
from datetime import datetime
from random import randint

import boto3
import click
from pathlib import Path


@click.group()
def cli():
    pass


@click.command()
@click.option('--access_key', prompt='Your access key', help='s3 access key')
@click.option('--secret_key', prompt='Your secret key', help='s3 secret key')
@click.option('--endpoint_url', prompt='Your endpoint address', help='s3 endpoint address')
def set_config(access_key, secret_key, endpoint_url):
    home = str(Path.home())
    config = open(f"{home}/.chabok_deploy.json", "w")
    config.write(json.dumps({
        "access_key": access_key,
        "secret_key": secret_key,
        "endpoint_url": endpoint_url,
    }))
    config.close()
    click.echo('Initialized the config')


@click.command()
def get_config():
    home = str(Path.home())
    config = open(f"{home}/.chabok_deploy.json", "r")
    click.echo(json.load(config))
    config.close()


@click.command()
@click.option('--path', prompt='Your path', help='path for backup')
def backup(path):
    home = str(Path.home())
    config_file = open(f"{home}/.chabok_deploy.json", "r")
    config = json.load(config_file)
    backup_name = str(datetime.date(datetime.now())) + str(
        randint(0, 999999)) + ".tar.gz"

    if path:
        os.system(f"cd /tmp && tar -Pczf {backup_name} {path}")
        session = boto3.session.Session()
        s3_client = session.client(
            service_name='s3',
            aws_access_key_id=config['access_key'],
            aws_secret_access_key=config['secret_key'],
            endpoint_url=config['endpoint_url'],
        )
        object_name = f"{backup_name}"
        backup_path = "/tmp/" + backup_name
        s3_client.upload_file(backup_path, 'services-backups', object_name)
        os.remove(backup_path)

    config_file.close()


cli.add_command(set_config)
cli.add_command(get_config)
cli.add_command(backup)

if __name__ == '__main__':
    cli()
