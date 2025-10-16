import time
def timer(func):
    # func 就是我们要装饰的原始函数
    def new_function():
        start_time = time.time()
        result = func()  # 执行原始函数
        end_time = time.time()
        print(f"执行时间: {end_time - start_time}")
        return result
    return new_function

"""
@timer
def say_hello():
    print("Hello!")

# 这完全等价于：say_hello = timer(say_hello)
say_hello()


def say_hello():
    print("Hello!")

# 手动装饰：用新的函数替换旧的函数
say_hello1 = timer(say_hello)
say_hello1()  # 现在会同时打印时间和"Hello"
"""


def bad_decorator1(func):
    def wrapper():
        print(f"装饰器执行，装饰函数: {func.__name__}")
        func()
        return func  # 直接返回原函数
    
    return wrapper

@bad_decorator1 
def my_function():
    print("原函数执行")

# 问题：装饰逻辑只在导入时执行一次，调用时没有装饰效果
#my_function()  # 只输出: "原函数执行"


def hire_employee(employee_role):
    """公司HR（外层函数）：招聘员工"""
    
    # 公司为员工准备的资源
    company_resources = f"{employee_role}的专用资源"
    salary = 5000  # 基本工资
    print("at the beginnning")
    def employee_work(*tasks, **special_requests):
        """员工（内层函数）：具体工作"""
        print(f"[{employee_role}] 使用{company_resources}")
        print(f"处理任务: {tasks}")
        bonus = special_requests.get('bonus', 0)
        total_income = salary + bonus
        return f"完成工作，总收入: {total_income}"
    
    return employee_work  # 返回可以工作的员工

# 招聘不同岗位的员工
developer = hire_employee("Python开发")
tester = hire_employee("测试工程师")
devops = hire_employee("DevOps工程师")

# 分配工作
developer("写代码", "调试", bonus=1000)
print(type(developer))  
print(developer.__name__)
#tester("功能测试", "性能测试")
#devops("部署", "监控", environment="production")
