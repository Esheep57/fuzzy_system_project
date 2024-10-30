# fuzzy_system_project

## 程式目標

本專案旨在解析模糊系統的 XML 文件，進行小樣本訓練和測試，並在訓練後輸出更新過的 XML 文件。主要功能包括：

- 解析 XML 文件中的模糊變數與規則。
- 使用少量數據進行模型訓練與測試。
- 將訓練後的參數更新至 XML 文件並導出。

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
### Commit Message 規範
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
###　注意事項
請依照以上協作流程和 commit message 規範進行開發，以保持專案的結構清晰、紀錄一致。