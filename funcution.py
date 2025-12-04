#斐波那契数列的函数
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
#打印前10个斐波那契数
for num in fibonacci(10):
    print(num)
#输出结果:

# 贝尔曼方程函数
def bellman_equation(state, action, reward, next_state, alpha, gamma, Q):
    """
    贝尔曼方程更新Q值
    state: 当前状态
    action: 当前动作
    reward: 当前奖励
    next_state: 下一个状态
    alpha: 学习率
    gamma: 折扣因子
    Q: Q值表，字典形式 {(state, action): value}
    """
    max_next_Q = max(Q.get((next_state, a), 0) for a in range(len(Q)))  # 假设动作空间是连续的整数
    Q[(state, action)] = Q.get((state, action), 0) + alpha * (reward + gamma * max_next_Q - Q.get((state, action), 0))
    return Q
# 示例使用贝尔曼方程函数
Q = {}
Q = bellman_equation(state=0, action=1, reward=10, next_state=2, alpha=0.1, gamma=0.9, Q=Q)
print(Q)
#输出结果:

