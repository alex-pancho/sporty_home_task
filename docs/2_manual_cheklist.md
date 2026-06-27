| Functional Requirement | check result | bug id |
|---|---|---|
| 2.1 Match List |  |  |
| Display upcoming football matches. | **FAIL** | [BUG-001] |
| Each match shows: |  |  |
| home team vs away team | PASS  |  |
| kickoff date/time label | PASS  |  |
| three selectable odds buttons: 1 , X , 2 | PASS |  |
| Selecting a new odds button replaces the previous selection. | PASS |  |
| User clicks on odds to select outcome for betting | PASS  | |
| Clicking new odds replaces previous selection | PASS | |
| 2.2 Bet Slip | | 
| Right-side fixed bet slip.| PASS | |
| Shows one active selection at a time.| PASS | |
| Shows entered stake, available balance, and computed potential payout.| PASS | |
| Includes: Place Bet| PASS | |
| Includes: Remove All| PASS | |
| per-selection remove ( x )| PASS | |
| 2.3 Place Bet Interaction|  | |
| On submit, button enters loading state ( Placing... ).| PASS | |
| After submit, the UI must show an in-progress state and resolve to one final outcome (success or failure).| PASS | |
| On success: stake is deducted | **FAIL** | [BUG-002] |
| On success: success receipt modal appears| PASS | |
| On failure: error modal appears with retry option| PASS | |
| 2.4 Success Receipt| PASS | |
| Receipt must show:| PASS | |
| Bet ID| PASS | |
| Match details| **FAIL**  | [BUG-003]  |
| Selection | PASS | |
| Stake| PASS | |
| Odds at placement| PASS | |
| Potential payout| PASS | |
| Placement timestamp| PASS | |
| Closing receipt returns user to main flow without active selection| PASS | |
| 2.5 Error Modal |  | |
| Modal title: Something went wrong | PASS | |
| Modal body explains that the bet could not be processed and suggests trying again. | PASS | |
| Actions: Rebet (primary): on click it closes the modal and retries placement. | PASS | |
| Actions: Close (secondary): closes modal and clears current selection/stake. | PASS | |
| top-right X : same behavior as Close . | PASS | |
| 2.6 Filters |  | |
| Date filter supports single day or date range (inclusive). | PASS | |
| Odds filter supports min/max range (inclusive) and must reject invalid ranges with clear feedback. |  **FAIL**  | [BUG-004], [BUG-005] |
| 3. Business Rules |  | |
| Stake min (per bet) €1.00  | PASS | |
| Stake max (per bet) €100.00  | PASS | |
| Stake precision: Up to 2 decimal places| PASS | |
| Minimum odds:1.01   | REMARK: now it's 1.00 | [DOC-001]  |
| Maximum odds:1000.00   | REMARK: now it's 10.00 | |
| 4. Validation Rules |  | |
| Stake Validation |  | |
| Required to place bet| PASS | |
| Must be numeric | PASS | |
| Minimum €1.01 | REMARK: now it's 1.00  | [DOC-001] |
| Maximum €100.00 | PASS | |
| Max 2 decimal places | PASS | |
| Must not exceed available balance | PASS | |
