class LogicGateSimulator:

    def __init__(self):
        print("--- 模擬器已啟動 ---")

    def and_gate(self, a, b):
        return a & b 
    def or_gate(self, a, b):
        return a | b
    def xor_gate(self, a, b):
        return a ^ b
    def not_gate(self, a):
        if a == 1:
            return 0
        else:
            return 1

if __name__ == "__main__":
    my_tool = LogicGateSimulator()

    input_combinations = [
        (0, 0),
        (0, 1),
        (1, 0),
        (1, 1)
    ]

    print("\n=== AND Gate Truth Table ===")
    print("A | B | Output")
    print("-------------")

    for inputs in input_combinations:
        a = inputs[0] # 抓出第一位數字
        b = inputs[1] # 抓出第二位數字
        
        result = my_tool.and_gate(a, b)
        print(f"{a} | {b} |   {result}")

    print("\n=== XOR Gate Truth Table ===")
    print("A | B | Output")
    print("-------------")
    for inputs in input_combinations:
        a = inputs[0]
        b = inputs[1]             
        result = my_tool.xor_gate(a, b)
        print(f"{a} | {b} |   {result}")