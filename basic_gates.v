// --- 1. 定義這顆晶片，名字叫 BasicGates ---
module BasicGates (
    input a,      // 輸入接腳 A
    input b,      // 輸入接腳 B
    output out_and, // 輸出接腳 (AND結果)
    output out_or,  // 輸出接腳 (OR結果)
    output out_xor  // 輸出接腳 (XOR結果)
);

    // --- 2. 內部的電路連線 (assign) ---
    // assign 的意思是「把線接上去」。這不是軟體的「賦值」，而是「硬體連線」。
    // 只要輸入 a 或 b 一變，輸出就會「立刻」跟著變 (就像電流流過去一樣)。
    
    assign out_and = a & b;  // & 代表 AND 閘
    assign out_or  = a | b;  // | 代表 OR 閘
    assign out_xor = a ^ b;  // ^ 代表 XOR 閘

endmodule


// --- 3. 定義測試平台 (沒有輸入輸出，因為它是封閉的實驗室) ---
module Testbench;

    // 定義測試用的信號線
    // reg (Register): 像是訊號產生器，可以存住數值 (0 或 1) 給晶片用
    // wire: 像是示波器的探針，用來觀察晶片輸出的結果
    reg t_a;
    reg t_b;
    wire t_and, t_or, t_xor;

    // --- 4. 把晶片放到測試板上 (Instantiation) ---
    // 語法: 晶片名 實體名 ( .晶片接腳(測試線), ... );
    BasicGates my_chip (
        .a(t_a), 
        .b(t_b), 
        .out_and(t_and), 
        .out_or(t_or), 
        .out_xor(t_xor)
    );

    // --- 5. 開始測試流程 (Initial Block) ---
    // initial begin ... end 是 Verilog 專門用來跑測試的區塊
    initial begin
        // 這一行是為了讓我們能在終端機看到結果 (Monitor = 監控)
        // %b 代表 binary (二進位), %t 代表 time (時間)
        $monitor("Time: %2t | A: %b | B: %b || AND: %b | OR: %b | XOR: %b", 
                 $time, t_a, t_b, t_and, t_or, t_xor);

        // --- 開始餵訊號 ---
        
        // 時間 0: 給 0, 0
        t_a = 0; t_b = 0;
        #10; // 等待 10 個時間單位 (就像示波器往前跑 10ns)

        // 時間 10: 給 0, 1
        t_a = 0; t_b = 1;
        #10; // 再等 10ns

        // 時間 20: 給 1, 0
        t_a = 1; t_b = 0;
        #10;

        // 時間 30: 給 1, 1
        t_a = 1; t_b = 1;
        #10;

        // 測試結束
        $finish;
    end

endmodule