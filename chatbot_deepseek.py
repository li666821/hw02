import openai
import sys
import getpass

_BASE_URL = "https://api.deepseek.com/v1"

def chat_with_deepseek(user_input):
    print("欢迎使用DeepSeek Chatbot！")
    print(f"正在初始化...")
    
    # 安全获取API密钥
    api_key = getpass.getpass("请输入DeepSeek API密钥: ")
    if not api_key:
        print("API密钥不能为空！")
        return
    
    # 初始化OpenAI客户端
    try:
        client = openai.OpenAI(
            api_key=api_key,
            base_url=_BASE_URL
        )
        print("初始化成功，正在发送请求...")
    except Exception as e:
        print(f"初始化失败: {e}")
        return
    
    # 初始化对话历史
    messages = [
        {"role": "system", "content": "你是一个 helpful 的助手。"}
    ]
    
    # 添加用户消息到对话历史
    messages.append({"role": "user", "content": user_input})
    
    try:
        # 调用DeepSeek模型
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            temperature=0.7,
            max_tokens=1024
        )
        
        # 获取模型回复
        assistant_reply = response.choices[0].message.content
        result = f"\n用户: {user_input}\nDeepSeek: {assistant_reply}\n"
        print(result)
        
        # 将结果写入文件
        with open('result.txt', 'w', encoding='utf-8') as f:
            f.write(result)
        
    except Exception as e:
        error_msg = f"\n错误: {e}\n"
        print(error_msg)
        with open('result.txt', 'w', encoding='utf-8') as f:
            f.write(error_msg)

if __name__ == "__main__":
    # 如果有命令行参数，使用第一个参数作为用户输入
    if len(sys.argv) > 1:
        user_input = ' '.join(sys.argv[1:])
    else:
        user_input = "你好"  # 默认输入"你好"
    
    chat_with_deepseek(user_input)
