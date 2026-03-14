# hw02
利用大模型生成学术论文导读，以及通过API调用大模型完成对话式应用。编写一个可运行的Chat bot实例代码，体验从读论文到用模型的完整链路。

## Chatbot示例代码

### 采用的API/平台
- 使用DeepSeek的OpenAI兼容接口
- API基础URL: https://api.deepseek.com/v1
- 模型: deepseek-chat

### 运行环境
- Python 3.7+
- Windows 10/11 或其他支持Python的操作系统

### 依赖安装
```bash
# 安装openai库
pip install openai

# 或使用requirements.txt
pip install -r requirements.txt
```

### 如何配置API Key
由于环境变量可能会被其他设置覆盖，本示例采用直接在脚本中配置API密钥的方式：

1. 打开 `chatbot_new.py` 文件
2. 找到以下行并替换为你的DeepSeek API密钥：
   ```python
   _MY_API_KEY = 'sk-449e0d8a65844be4826fe4326687a1f0'
   ```

### 运行命令
```bash
# 默认发送"你好"消息
python chatbot_new.py

# 发送自定义消息
python chatbot_new.py 你的问题

# 示例
python chatbot_new.py 你是谁
python chatbot_new.py 什么是机器学习
```

### 示例输入/输出
**示例1: 询问"你是谁"**
```
欢迎使用DeepSeek Chatbot！
正在初始化...
初始化成功，正在发送请求...

用户: 你是谁
DeepSeek: 你好！我是DeepSeek，由深度求索公司创造的AI助手！😊

我是一个纯文本模型，虽然不支持多模态识别功能，但我有文件上传功能，可以帮你处理图像、txt、pdf、ppt、word、excel等各种文件，从中读取文字信息进行分析处理。我完全免费使用，拥有128K的上下文长度，还支持联网搜索功能（需要你在Web/App中手动点开联网搜索按键）。

你可以通过官方应用商店下载我的App来使用我。我很乐意为你解答问题、协助处理文档、进行对话交流等等！

有什么我可以帮助你的吗？无论是学习、工作还是日常问题，我都很愿意为你提供帮助！✨
```

**示例2: 询问"你好"**
```
欢迎使用DeepSeek Chatbot！
正在初始化...
初始化成功，正在发送请求...

用户: 你好
DeepSeek: 你好！很高兴见到你！😊 有什么我可以帮助你的吗？无论是回答问题、聊天，还是需要协助处理任务，我都很乐意为你提供帮助！
```

### 注意事项
1. **API密钥获取**：请确保你已经从DeepSeek官网获取了有效的API密钥
2. **API费用**：API调用可能会产生费用，请根据DeepSeek的 pricing 计划了解详情
3. **网络连接**：确保你的网络连接正常，能够访问DeepSeek API服务
4. **环境变量问题**：如果之前设置过 `DEEPSEEK_API_KEY` 环境变量，可能会影响脚本运行，请确保该环境变量未被设置为错误值
5. **脚本修改**：如需使用其他模型或API，请修改脚本中的 `_BASE_URL` 和 `model` 参数
6. **响应时间**：API调用可能需要几秒钟时间，请耐心等待
7. **错误处理**：如果遇到认证失败等错误，请检查API密钥是否正确，以及是否有足够的余额
8. **结果输出**：脚本会将完整的对话结果写入 `result.txt` 文件，以便查看完整输出

### 故障排除
- **认证失败错误**：请检查API密钥是否正确，是否有足够的余额
- **网络错误**：请检查网络连接，确保能够访问DeepSeek API服务
- **环境变量冲突**：请确保没有设置错误的 `DEEPSEEK_API_KEY` 环境变量
- **依赖问题**：请确保已正确安装openai库

