# 配置Tailwind自定义颜色和字体，匹配应用内风格
def setup_tailwind_config():
    config = {
        "theme": {
            "extend": {
                "colors": {
                    "primary": "#3b82f6",  # 应用主色调
                    "secondary": "#64748b",  # 次要颜色
                    "neutral": "#f1f5f9",  # 中性色
                    "dark": "#1e293b",  # 深色
                    "success": "#10b981",  # 成功色
                    "danger": "#ef4444",  # 错误色
                },
                "fontFamily": {
                    "sans": ["Inter", "system-ui", "sans-serif"],
                },
            }
        }
    }
    return config

# 初始化表单数据
def init_form_data():
    """
    初始化远程仓库设置表单的默认数据
    包含仓库类型、URL、分支和认证方式等信息
    """
    return {
        "repoType": "github",
        "repoUrl": "",
        "branch": "main",
        "authType": "ssh",
        "token": "",
        "username": "",
        "password": "",
        "autoPull": False,
        "autoPush": False
    }

# 验证仓库URL格式
def validate_repo_url(url):
    # 检查是否为空
    if not url:
        return False, "仓库URL不能为空"
    
    # 简单验证URL格式（支持HTTPS和SSH）
    import re
    https_pattern = r"^https?://.*\.git$"
    ssh_pattern = r"^git@.*\.git$"
    
    if re.match(https_pattern, url) or re.match(ssh_pattern, url):
        return True, "URL格式有效"
    else:
        return False, "无效的仓库URL格式，请使用HTTPS或SSH格式"

# 测试仓库连接
def test_repo_connection(url):
    # 这里是连接测试逻辑
    # 实际应用中会调用Git命令或相关库
    print(f"正在测试与仓库 {url} 的连接...")
    # 模拟连接成功
    return True, "连接测试成功"

# 保存仓库配置
def save_repo_config(config):
    """
    保存远程仓库配置到文件
    参数: config - 包含仓库配置信息的字典
    返回: 保存结果（布尔值）和消息
    """
    try:
        import json
        with open("repo_config.json", "w") as f:
            json.dump(config, f, indent=2)
        return True, "配置保存成功"
    except Exception as e:
        return False, f"保存失败: {str(e)}"
