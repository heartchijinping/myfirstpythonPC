def print_welcome():
    print("Hello, Git!")
    print("这是我的第一个Python项目")

def safe_operation(func):
    try:
        func()
        print("操作成功完成")
        print("我们在学习Git分支管理")
    except Exception as e:
        print(f"发生错误：{e}")

def main():
    safe_operation(print_welcome)

if __name__ == "__main__":
    main()
