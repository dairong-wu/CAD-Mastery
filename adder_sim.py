from logic_gates import LogicGateSimulator

class FullAdder:
    def __init__(self):
        self.gate = LogicGateSimulator()

    def compute(self, a, b, cin):
        """
        Input: a, b, cin (0 或 1)
        Output: (sum_val, cout_val)
        """
        
        # sum = A XOR B XOR Cin
        axb = self.gate.xor_gate(a, b)
        sum_val = self.gate.xor_gate(axb, cin)

        # cout = (A AND B) OR (Cin AND (A XOR B))
        ab_and = self.gate.and_gate(a, b)
        cin_and_axb = self.gate.and_gate(cin, axb)
        cout_val = self.gate.or_gate(ab_and, cin_and_axb)

        return sum_val, cout_val

if __name__ == "__main__":
    my_adder = FullAdder()

    test_cases = [
        (0, 0, 0),
        (0, 0, 1),
        (0, 1, 0),
        (0, 1, 1),
        (1, 0, 0),
        (1, 0, 1),
        (1, 1, 0),
        (1, 1, 1)
    ]

    print("\n=== Full Adder Truth Table ===")
    print("A | B | Cin || Sum | Cout")
    print("-------------------------")

    for t in test_cases:
        a = t[0]
        b = t[1]
        cin = t[2]

        s, c = my_adder.compute(a, b, cin)

        print(f"{a} | {b} |  {cin}  ||  {s}  |  {c}")