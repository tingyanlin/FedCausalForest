
### 資料夾結構

FedCausalForest
  ├── default/
│   ├── main.py
│   ├── utils.py
│   └── config/
│       ├── settings.json
│       └── database.json
├── playbooks/
│   ├── README.md
│   └── guide.md
└── requirements.txt



### Ansible
[Ansible官方文檔](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/apt_module.html)

#### 安裝Ansible
```bash
# 安裝 Ansible 在 Ubuntu 上
sudo apt install ansible

# 安裝 Ansible 在 Python 環境中
pip install ansible
```

#### 執行以下命令
```bash
ansible-playbook main.yml
```
