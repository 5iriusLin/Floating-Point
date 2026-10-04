# 最後一次手動執行

## 本次準備狀態

所有 Q0～Q6 C++ 程式已可建置；Q7 為文字揭露。建置、入口檢查、Q1 短程 kernel smoke check、來源查證與產生碼檢查已完成。助手已按本人後續授權，以 GCC 16.2.0 實際跑完整批次與 benchmark，保存到帶 assistant 後綴的目錄；詳見 `docs/assistant_validation.md`。本人仍需明天親自跑與截圖，Word 的本人結果欄保留待填。

## Windows 與 WSL 主實驗

先在專案根目錄 PowerShell 記錄 Windows 環境：

```powershell
./experiments/q0_environment/collect_windows.ps1
```

Windows 資訊放入新的 `results/q0-windows/日期時間/`，早先 Q0 原始紀錄保留。WSL 版本輸出的中文編碼已修正。

然後在 WSL Ubuntu 執行：

```bash
cd /mnt/c/Users/ALAN/Desktop/floating-point-hw2
bash scripts/run_all.sh
```

script 會重新編譯並依序跑 Q0、Q1、Q2 兩種路徑、Q3 兩種旗標、Q4、Q5 四種 rounding modes、Q6。每次結果放入新建的 `results/linux-YYYYMMDD-HHMMSS/`，不覆寫舊紀錄；命令、stderr、退出碼、flags、來源雜湊、assembly 與函式庫依賴一併保存。正式 benchmark 中不插入截圖操作。

預設 Q1 是 5000000 iterations、7 repeats、2 warmups。若想完整重跑較長的版本：

```bash
HW2_ITERATIONS=20000000 HW2_REPEATS=9 bash scripts/run_all.sh
```

保留第一次結果並說明重跑理由。若時間波動大，記錄背景負載與電源，不挑數據。script 若失敗，查看最後的 exit 記錄及 build.txt；失敗結果也要保留。新增結果目录後即開始採集，請等待 completion.txt；建置失敗時不會執行實驗。

## Mac 選用比較

把整個專案（包含 experiments、scripts）帶到 Mac。在專案根目錄執行：

```bash
CXX=g++-16 bash scripts/run_all.sh
```

會放入 `results/darwin-YYYYMMDD-HHMMSS/`。兩平台使用 GNU GCC 16.2.0；Mac 的完整版本輸出仍需實機保存。Q5 候選 B 必須另核對來源、確切版本、flags 與實際結果，不能只憑安裝同版本就宣稱完成。以 `CXX=/完整路徑/g++-16` 可明確選擇 compiler。Mac script 尚未在實體 Mac 驗證；遇到 unsupported compiler flag 或缺少 developer tools，先保留 build.txt，不自行改掉 Q5 的對照旗標。

## 只建置或檢查，不跑實驗

```bash
bash scripts/build_all.sh
bash scripts/check_build.sh
```

第二行只做入口與短程 kernel 檢查，不能當成正式實驗。若用 CMake，先 `source scripts/compiler_env.sh`，再 `cmake -S . -B build/cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_COMPILER="$CXX"`，再 `cmake --build build/cmake -j2`。

## 整理實際結果

```bash
python3 scripts/summarize_q1.py results/linux-YYYYMMDD-HHMMSS
```

只有讀入本人執行產生的 Q1 原始紀錄後才生成 summary.csv 與 summary.md；無數據或任一原始執行失敗時拒絕產生摘要。這些檔案是計算後的摘要，原始紀錄保留。

## 截圖清單

| 題目 | 需要的畫面 |
|---|---|
| Q0 | Windows／WSL、OS、compiler、三種型態輸出 |
| Q1 | flags／參數、三型態同 kernel sample／summary、精度案例、assembly loop |
| Q2 | std／libm 兩路徑、特殊值／errno／flags、sqrt assembly、函式庫版本 |
| Q3 | 同输入的 strict／fast output、兩版關鍵 assembly |
| Q4 | 精確中點 hexfloat、九位輸出、mode 与鄰近值 |
| Q5 | 同 binary 或同 compiler／flags／source 的證據、不同 mode 或 ABI output |
| Q6 | 三個 underflow 案例與 exception flags、rounding mode／MXCSR |

跑完後可一次整理結果檔案的畫面截圖，標明檔案來源；若要終端當場執行截圖，保留命令與輸出。截圖不能取代完整原始資料。所有 Word 的結果欄仍待實際數據，不應直接提交目前準備稿。
