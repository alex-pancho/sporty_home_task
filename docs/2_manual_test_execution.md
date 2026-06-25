# Manual Test Execution Report

**Tester:** Oleksandr Panchenko
**Date:** 2026-06-26  
**Test Environment:** https://qae-assignment-tau.verisk.app/?user-id=candidate-c9ywt7uhfX 
**Browser:** Chrome 149.0.7827.197

## Test Execution Summary

| Test Case | Status | Notes |
|-----------|--------|-------|
| TC-001: Happy Path | ❌ FAIL | [BUG-001], [BUG-002], [BUG-003] |
| TC-002: Min Stake | ✅ PASS  | |
| TC-003: Max Stake | ✅ PASS | |
| TC-004: Insufficient Balance | ✅ PASS | |
| TC-005: Error Handling | ✅ PASS |  |
| TC-006: Odds Selection | ❌ FAIL | [BUG-004], [BUG-005] |

## Exploratory Testing Notes

### Quick Checks Performed
- [✅] Decimal separator input behavior (e.g., €10.5, €10.50)
- [✅] Removing bet from slip (X button)
- [✅] Clearing entire slip (Remove All button)
- [❌] Balance updates after bet placement
- [✅] Match list display (teams, odds, date)
- [✅] Bet receipt accuracy (all fields match placement)
- [✅] Modal close behavior (X button, backdrop click)

## Summary

**Total Defects Found:** 5
- Critical: 2
- High: 2
- Medium: 0
- Low: 1

**Test Cases Passed:** [4/6]  
**Test Cases Failed:** [2/6]

**Blocker Issues:** [Yes/No] — YES [BUG-001], [BUG-002], [BUG-003]

**Quality Gate:** FAIL — Cannot release with BUG-001 (financial/legal risk)

## Recommendations by Component

**Frontend (UI Layer):**
- [ ] BUG-002: Sync header balance after successful API response
- [ ] BUG-003: Verify team order in receipt modal (use homeTeam, awayTeam fields correctly)
- [ ] BUG-004: Add odds filter validation before apply
- [ ] BUG-005: Use >= for min filter, not >

**Backend (API Layer):**
- [ ] BUG-001: Filter /api/matches to exclude kickoffDate < NOW
- [ ] BUG-001: Add API validation to reject bets on past matches (409 Conflict)
- [ ] Verify response data mapping for matchId -> teams order
