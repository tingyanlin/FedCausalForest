#### 1. Ansible  [Ansible官方文檔](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/apt_module.html)
##### 安裝Ansible
```bash
# 安裝 Ansible 在 Ubuntu 上
sudo apt install ansible

# 安裝 Ansible 在 Python 環境中
pip install ansible
```

##### 執行以下命令
```
ansible-playbook main.yml
```

```bash
# 查看 federatedai/standalone_fate 功能
ls -l /data/projects/fate/


# 查看 party id
docker exec -it standalone_fate_<party_id> env | grep FATE_PARTY_ID

# 查看 container 設定 如 Party ID, Role
docker inspect --format '{{.Config.Env}}' <container name>
```
#### 3. EconML  [EconML官方文檔](https://econml.azurewebsites.net/)


