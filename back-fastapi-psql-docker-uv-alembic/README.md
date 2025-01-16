# FastAPI, postgres, Docker(fastapi, postgres), uv, sqlalchemy, alembic
## Requirements
- Ansible Requirements
- uv
- docker


## Usage

1. Configure the environment variables in the template's `.env.yml` file
2. Run the playbook using `ansible-playbook playbook.yml -i inventory.ini`

## After execute ansible-playbook
please run following command for finish the setup

```shell
docker compose build
```