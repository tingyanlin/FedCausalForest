### 1. 專案結構
```bash
FedCausalForest
├── default/
│   ├── config.yml # 參數設定
│   └── packages.yml # Ubuntu 與 anaconda 套件設定
│
├── playbooks/
│   ├── setup_environment.yml # 設置 anaconda 開發環境
│   └── setup_nodes.yml # 設置 docker 節點
│
├── scripts/
│   └── python/
│       ├── data/ # 放置資料集、輸出結果
│       ├── analysis.py # 資料分析程式
│       ├── csusal_random_forest.py # 因果森林程式
│       ├── config.py # 程式參數設定
│       └── main.py
│ 
└── main.yml
```

### 2. Ansible [Ansible官方文檔](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/apt_module.html)
#### 安裝Ansible
```bash
# 安裝 Ansible 在 Ubuntu 上
sudo apt install ansible

# 安裝 Ansible 在 Python 環境中
pip install ansible
```

### 執行以下命令
```bash
ansible-playbook main.yml
```

### 3. EconML [EconML官方文檔](https://econml.azurewebsites.net/)
