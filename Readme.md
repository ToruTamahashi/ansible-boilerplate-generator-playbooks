# Ansible Project Automation Suite

A collection of Ansible playbooks for automating various project setups and configurations.


## Requirements

- Ansible
- Python 3.x

## Installation

1. Clone the repository:
```bash
git clone git@github.com:ToruTamahashi/ansible-playbooks.git
```

2. Install Ansible:
```bash
# For macOS
brew install ansible

# For Ubuntu/Debian
sudo apt install ansible
```

## Usage

Each project template is contained in its own directory with a dedicated playbook and configuration files. Follow these general steps:

1. Choose the project template you want to use
2. Configure the environment variables in the template's `.env.yml` file
3. Run the playbook using `ansible-playbook playbook.yml -i inventory.ini`




