#### 專案結構
```bash
FedCausalForest
├── packages/
│   ├── linux_packages.yml # Ubuntu 套件設定
│   └── python_packages.yml # Python 套件設定
│
├── playbooks/
│   ├── unused/
│   │   └── deploy_fate_environment
│   │
│   ├── fate_steup.yml
│   ├── image_setup.yml # 設置 docker images
│   ├── main.yml
│   ├── mysql_setup.yml # 設置 mysql
│   ├── network_setup # 設置 docker network
│   └── setup_environment.yml # 設置 anaconda 開發環境
│
├── scripts/
│   └── causal_random_forest/
│       ├── data/ # 放置資料集、輸出結果
│       ├── analysis.py # 資料分析程式
│       ├── csusal_random_forest.py # 因果森林程式
│       ├── config.py # 程式參數設定
│       └── main.py
│ 
└── vars/
    ├── common.yml
    ├── conda_config.yml
    ├── docker_config.yml
    ├── fate_config.yml
    ├── mysql_config.yml
    └── redis_config.yml
```