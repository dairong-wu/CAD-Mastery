class TimingAnalyzer:
    def __init__(self, t_setup, t_hold):
        # 定義這個晶片的物理限制 (單位通常是 ns 或 ps)
        self.t_setup = t_setup
        self.t_hold = t_hold

    def check_timing(self, clock_edge_time, data_arrival_time, data_change_time):
        """
        模擬 STA 檢查
        clock_edge_time: Clock 上升緣發生的時間點
        data_arrival_time: Data 變穩定的時間點 (開始 Stable)
        data_change_time: Data 結束穩定的時間點 (開始下一次變化)
        """
        print(f"\n--- Checking Timing at Clock = {clock_edge_time} ---")

        # 1. 檢查 Setup Time (Data 必須在 Clock 之前多久就到了?)
        # 公式: (Clock時間 - Data到達時間) 必須 >= T_setup
        setup_slack = clock_edge_time - data_arrival_time
        
        if setup_slack >= self.t_setup:
            print(f"[PASS] Setup Check. (Slack: {setup_slack} >= {self.t_setup})")
        else:
            print(f"[FAIL] Setup Violation! Data arrived too late. (Slack: {setup_slack} < {self.t_setup})")
            print("   -> Physics: Internal capacitor didn't charge fully!")

        # 2. 檢查 Hold Time (Data 在 Clock 之後維持了多久?)
        # 公式: (Data改變時間 - Clock時間) 必須 >= T_hold
        hold_slack = data_change_time - clock_edge_time
        
        if hold_slack >= self.t_hold:
            print(f"[PASS] Hold Check.  (Slack: {hold_slack} >= {self.t_hold})")
        else:
            print(f"[FAIL] Hold Violation! Data changed too soon. (Slack: {hold_slack} < {self.t_hold})")
            print("   -> Physics: Transmission gate wasn't fully closed yet!")

if __name__ == "__main__":
    # 假設我們的一個 D-FF 物理特性是：Setup需要 2ns, Hold需要 1ns
    analyzer = TimingAnalyzer(t_setup=2, t_hold=1)

    # 案例 A: 成功 (Safe)
    # Clock在 10ns 觸發
    # Data 在 5ns 就來了 (比 10 早 5ns > 2ns) -> Setup Pass
    # Data 到 15ns 才走 (比 10 晚 5ns > 1ns) -> Hold Pass
    analyzer.check_timing(clock_edge_time=10, data_arrival_time=5, data_change_time=15)

    # 案例 B: Setup 失敗 (太晚來)
    # Data 在 9ns 才來 (只比 10 早 1ns < 2ns)
    analyzer.check_timing(clock_edge_time=10, data_arrival_time=9, data_change_time=15)

    # 案例 C: Hold 失敗 (太早走)
    # Data 在 10.5ns 就走了 (只維持了 0.5ns < 1ns)
    analyzer.check_timing(clock_edge_time=10, data_arrival_time=5, data_change_time=10.5)