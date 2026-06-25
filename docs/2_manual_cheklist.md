| Functional Requirement | check result | bug id |
|---|---|---|
| 2.1 Match List |  |  |
| Display upcoming football matches. | **FAIL** | [BUG-001] |
| Each match shows: |  |  |
| home team vs away team | pass  |  |
| kickoff date/time label | pass  |  |
| three selectable odds buttons: 1 , X , 2 | pass |  |
| Selecting a new odds button replaces the previous selection. | pass |  |
| User clicks on odds to select outcome for betting | pass  | |
| Clicking new odds replaces previous selection | pass | |
| 2.2 Bet Slip | | 
| Right-side fixed bet slip.| pass | |
| Shows one active selection at a time.| pass | |
| Shows entered stake, available balance, and computed potential payout.| pass | |
| Includes: Place Bet| pass | |
| Includes: Remove All| pass | |
| per-selection remove ( x )| pass | |
| 2.3 Place Bet Interaction|  | |
| On submit, button enters loading state ( Placing... ).| pass | |
| After submit, the UI must show an in-progress state and resolve to one final outcome (success or failure).| pass | |
| On success: stake is deducted | **FAIL** | [BUG-002] |
| On success: success receipt modal appears| pass | |
| On failure: error modal appears with retry option| pass | |
| 2.4 Success Receipt| pass | |
| Receipt must show:| pass | |
| Bet ID| pass | |
| Match details| **FAIL**  | [BUG-003]  |
| Selection | pass | |
| Stake| pass | |
| Odds at placement| pass | |
| Potential payout| pass | |
| Placement timestamp| pass | |
| Closing receipt returns user to main flow without active selection| pass | |
| 2.5 Error Modal |  | |
| Modal title: Something went wrong | pass | |
| Modal body explains that the bet could not be processed and suggests trying again. | pass | |
| Actions: Rebet (primary): on click it closes the modal and retries placement. | pass | |
| Actions: Close (secondary): closes modal and clears current selection/stake. | pass | |
| top-right X : same behavior as Close . | pass | |
| 2.6 Filters |  | |
| Date filter supports single day or date range (inclusive). | pass | |
| Odds filter supports min/max range (inclusive) and must reject invalid ranges with clear feedback. |  **FAIL**  | [BUG-004], [BUG-005] |
| 3. Business Rules |  | |
| Stake min (per bet) €1.00  | pass | |
| Stake max (per bet) €100.00  | pass | |
| Stake precision: Up to 2 decimal places| pass | |
| Minimum odds:1.01   | REMARK: now it's 1.00 | [DOC-001]  |
| Maximum odds:1000.00   | REMARK: now it's 10.00 | |
| 4. Validation Rules |  | |
| Stake Validation |  | |
| Required to place bet| pass | |
| Must be numeric | pass | |
| Minimum €1.01 | REMARK: now it's 1.00  | [DOC-001] |
| Maximum €100.00 | pass | |
| Max 2 decimal places | pass | |
| Must not exceed available balance | pass | |
