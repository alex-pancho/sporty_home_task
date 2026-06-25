# Manual Test Execution Report

**Tester:** Oleksandr Panchenko
**Date:** 2026-06-26  
**Test Environment:** https://qae-assignment-tau.verisk.app/?user-id=candidate-c9ywt7uhfX 
**Browser:** Chrome 149.0.7827.197

## Test Execution Summary

| Test Case | Status | Notes |
|-----------|--------|-------|
| TC-001: Happy Path | ❌ FAIL | [Brief note] |
| TC-002: Min Stake | ✅ PASS  | [Brief note] |
| TC-003: Max Stake | ✅ PASS / ❌ FAIL | [Brief note] |
| TC-004: Insufficient Balance | ✅ PASS / ❌ FAIL | [Brief note] |
| TC-005: Error Handling | ✅ PASS / ❌ FAIL | [Brief note] |
| TC-006: Odds Selection | ✅ PASS / ❌ FAIL | [Brief note] |

## Exploratory Testing Notes

### Quick Checks Performed
- [✅] Decimal separator input behavior (e.g., €10.5, €10.50)
- [✅] Removing bet from slip (X button)
- [✅] Clearing entire slip (Remove All button)
- [❌] Balance updates after bet placement
- [✅] Match list display (teams, odds, date)
- [✅] Bet receipt accuracy (all fields match placement)
- [✅] Modal close behavior (X button, backdrop click)

### Observations
```
[Document any observations that don't fit into test cases]
Example:
- Balance updates correctly and immediately in header
- Bet receipt displays timestamp in UTC
- Decimal values with trailing zero (€10.0) are accepted
```

## Defect Reports



**Total Defects Found:** [X]
- Critical: [X]
- High: [X]
- Medium: [X]
- Low: [X]

**Test Cases Passed:** [X/6]  
**Test Cases Failed:** [X/6]

**Blocker Issues:** [Yes/No] — [If yes, list which ones block feature release]

**Recommendation:** [READY FOR RELEASE / NEEDS FIXES / DO NOT RELEASE]

## Notes for Developer/Automation

- [Any observations about test data needs]
- [Any flakiness or timing issues noticed]
- [Any assumptions made during testing]