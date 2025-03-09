
### 資料夾結構
```python
FedCausalForest
├── default/
│   ├── config.yml
│   └── packages.yml
│
├── playbooks/
│   ├── setup_environment.yml 
│   └── setup_nodes.yml # 設置 docker 節點
├── scripts/
│   ├── python/
│       ├── 
│       ├── 
│
└── main.yml
```


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
