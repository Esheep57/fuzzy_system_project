# Fuzzy System Project

## 專案目標

本專案旨在解析模糊系統的 XML 文件，進行小樣本訓練和測試，並在訓練後輸出更新過的 XML 文件。主要功能包括：

- **解析 XML 文件中的模糊變數與規則**：
  - 支援多種形狀類型（如 TrapezoidShape、TriangularShape、GaussianShape、LeftGaussianShape、RightGaussianShape）。
- **導入訓練資料的 Excel 檔案**：
  - 使用少量數據（約40筆）進行模型訓練與測試。
- **更新並導出 XML 文件**：
  - 將訓練後的參數更新至 XML 文件並導出。

## 開發環境

- **語言**：Python 3.8
- **工具**：VS Code、GitHub Desktop
- **平台**：Windows Intel（Wintel）

## 專案結構

```
fuzzy_system_project/
├── README.md
├── requirements.txt
├── gitattributes
├── LICENSE
├── main.py
├── src/
│   ├── __init__.py
│   ├── models.py
│   └── parser.py
├── data/
│   ├── cimodel.xml
│   └── training_data.xlsx
└── tests/
    └── test_parser.py
```

- **README.md**：專案說明文件。
- **requirements.txt**：專案所需的 Python 套件。
- **gitattributes**：Git 屬性設定文件。
- **gitignore**：指定 Git 忽略的文件和目錄。
- **LICENSE**：專案許可證文件。
- **main.py**：主程式入口。
- **src/**：主要的程式碼目錄。
  - **models.py**：定義數據模型（如模糊變數、模糊術語、規則等）。
  - **parser.py**：負責解析 XML 文件。
- **data/**：存放 XML 文件和其他數據文件。
  - **cimodel.xml**：模糊系統的 XML 模型文件。
  - **training_data.xlsx**：訓練資料的 Excel 文件。
- **tests/**：測試程式碼目錄。
  - **test_parser.py**：針對解析器的測試用例。

## 專案結構設置

- 使用 `venv` 環境進行開發。
- 創建了基本的專案目錄結構，包括 `src/`、`data/`、`tests/` 等目錄。
- 添加了必要的文件如 `README.md`、`LICENSE`、`.gitignore` 等。
- 安裝必要的 Python 套件：
  - 使用 `requirements.txt` 管理依賴，並成功安裝了 `lxml`、`dataclasses`、`pandas`、`openpyxl` 等套件。

## 開發者協作工作流

為了確保專案的整體性和代碼品質，建議所有開發者遵循以下協作流程。此專案為內部開發，因此只有組內工作人員可以進行改寫，無需代碼審查流程。開發者在進行新功能開發或修正時應採用分支開發，並在完成後合併至主分支。

### 1. 分支開發

每位開發者在進行新功能或修正時，應從 `main` 分支創建新的分支以便追蹤更改。以下為建立新分支的示例：

```bash
git checkout -b feature-xml-parser
```

### 2. 完成開發後合併至 main
 當功能開發或修正完成後，開發者可以將分支直接合併到 main，無需經過代碼審查。

- 切換回 main 分支：
```bash
git checkout main
```
- 拉取最新的 main 分支代碼，確保與遠端同步：
```bash
git pull origin main
```
- 合併分支到 main：
```bash
git merge feature-xml-parser
```
- 推送最新的 main 分支至 GitHub：
```bash
git push origin main
```
### 3. 同步最新代碼
每位開發者應定期從 main 分支拉取最新的代碼，以確保與專案保持同步。建議每次開始新的開發任務時，先更新 main 分支。
```bash
git checkout main
git pull origin main
```
## Commit Message 規範
為了保持提交記錄的清晰和統一，請遵循以下的 commit message 格式，並根據專案需求制定專屬描述。此專案的提交記錄應包含具體功能或更改的簡要描述，以便未來查閱和維護。

### Commit Message 類別
- 新增功能：feat: 描述新功能的簡短說明。
- 修正錯誤：fix: 描述所修正的問題。
- 更新訓練參數：update: 更新模型訓練或測試參數。
- XML 文件調整：xml: 對 XML 文件進行的解析或結構更改。
- 代碼重構：refactor: 調整代碼以改善性能或可讀性，但不影響功能。
- 格式調整：style: 僅調整代碼格式、縮排或註解，不影響功能。
- 測試代碼：test: 新增或修改測試用例和相關代碼。
- 更新文件：docs: 更新或新增說明文件
### Commit Message 範例
- feat: 增加 XML 文件解析功能
- fix: 修正模型參數初始化錯誤
- update: 調整模型訓練過程中的學習率
- xml: 新增模糊變數定義至 XML 文件
- refactor: 優化模糊規則的執行效率
- style: 調整註解格式與代碼縮排
- test: 新增 XML 解析功能的測試用例
- docs: 更新 README 文件中的協作流程
##　注意事項
請依照以上協作流程和 commit message 規範進行開發，以保持專案的結構清晰、紀錄一致。

## 工作進度

### 專案進展

- **解析模糊系統的 XML 文件**：
  - 支援多種形狀類型（如 TrapezoidShape、TriangularShape、GaussianShape、LeftGaussianShape、RightGaussianShape）。
  - 定義數據模型 (`models.py`) 並實作解析器 (`parser.py`)。
  - 實作主程式 (`main.py`) 來解析並顯示模糊變數、模糊術語、規則及訓練資料。
  - 解決導入形狀類別時遇到的錯誤，確保正確設置 `__init__.py`。

- **導入訓練資料的 Excel 檔案**：
  - 已完成基本的導入功能，確認能夠讀取並顯示訓練資料。
  - 確保 Excel 檔案結構正確，包含必要的欄位。
  - 計劃實作數據預處理以確保數據質量。

### 接下來的工作計劃

1. **導入訓練資料的 Excel 檔案**：
   - **進度**：已完成基本的導入功能，確認能夠讀取並顯示訓練資料。
   - **後續步驟**：
     - 確保 Excel 檔案結構正確，包含必要的欄位。
     - 實作數據預處理（如有需要），確保數據質量。

2. **選擇和實作適合小樣本的模型訓練算法**：
   - **目標**：由於資料量較少，選擇適合少樣本學習的演算法，如基於規則的優化方法、遺傳算法、貝葉斯優化等。
   - **計劃**：
     - 調研適合的演算法。
     - 實作並整合選定的演算法到專案中。

3. **訓練模糊系統**：
   - **目標**：使用導入的訓練資料來調整模糊變數的參數或規則，以提升系統的準確性和效能。
   - **計劃**：
     - 開發訓練模組，根據訓練資料優化模糊系統參數。
     - 測試訓練結果，確保模型表現符合預期。

4. **測試模型**：
   - **目標**：使用測試資料來評估模型的表現，確保其在實際應用中的可靠性。
   - **計劃**：
     - 收集或生成測試資料。
     - 執行測試，並分析模型的準確性和穩定性。

5. **更新並導出 XML 文件**：
   - **目標**：將訓練後的模糊系統參數更新回 XML 文件，並導出以供後續使用。
   - **計劃**：
     - 開發 XML 更新模組，將新的參數寫回 `cimodel.xml`。
     - 確認更新後的 XML 文件結構和內容正確無誤。

6. **撰寫和更新專案文檔**：
   - **目標**：確保專案文檔（如 `README.md`）完整，涵蓋專案介紹、安裝指南、使用說明和開發指南等。
   - **計劃**：
     - 更新 `README.md`，添加專案的最新進展和使用說明。
     - 撰寫用戶和開發者指南，方便未來的維護和擴展。
     