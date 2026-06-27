# Test Plan: Single Bet Placement Feature

## Overview
This test plan covers the core betting functionality: match selection, stake entry, and bet placement with success/error scenarios.

Users can place a single bet on a sports event outcome. This is the core betting functionality
that allows customers to wager money on match results with odds.

**Platform**: Desktop web application

**Sport**: Soccer/Football only

**Event Type**: Upcoming/Pre-match events only (no live betting)

**Bet Type**: Single bet only (no accumulator/multi-bets)

**Feature Scope:**
- Desktop web application (Chrome)
- Soccer/Football only
- Pre-match bets only (no live betting)
- Single bets only (no accumulators)

**Test Environment:** https://qae-assignment-tau.vercel.app/?user-id=candidate-c9ywt7uhfX 

## Test Scenarios (Prioritized)

### 1. **TC-001: Happy Path - Successful Bet Placement**
**Priority:** 🔴 **CRITICAL**

**Risk Rationale:**
- This is the core happy path. If a user cannot successfully place a bet, the feature is broken.
- Validates the entire flow: match selection → stake entry → API call → balance deduction → receipt.
- High business impact: directly tied to revenue.

**Preconditions:**
- User is authenticated and on the application
- At least one upcoming match is displayed
- User balance ≥ €1.00

**Steps:**
1. Observe initial balance displayed in header
2. Click on a match's "1" (Home Win) odds button
3. Enter stake: €10.00
4. Click "Place Bet"
5. Wait for loading state to resolve
6. Observe success receipt modal

**Expected Result:**
- Bet slip shows selection with correct odds
- "Place Bet" button shows loading state ("Placing...")
- Success receipt displays:
  - Bet ID (non-empty string)
  - Match details (teams + date)
  - Selection: HOME
  - Stake: €10.00
  - Odds at placement
  - Potential payout (calculated as stake × odds)
  - Placement timestamp
- Header balance decreases by €10.00
- Closing receipt returns to empty bet slip (no active selection)

**Test Data:**
- Match: Any upcoming match
- Stake: €10.00
- Selection: HOME

### 2. **TC-002: Stake Validation - Boundary: Minimum Stake (€1.00)**
**Priority:** 🔴 **CRITICAL**

**Risk Rationale:**
- Minimum stake is a hard business rule (€1.00)
- Boundary testing catches off-by-one errors in validation logic
- If minimum is not enforced, company loses revenue threshold control
- Both UI and API must validate

**Preconditions:**
- User is on the application
- A match is selected in the bet slip

**Steps:**
1. Select a match outcome
2. Enter stake: €0.99
3. Attempt to click "Place Bet"
4. Observe UI feedback

**Expected Result:**
- "Place Bet" button is disabled OR
- Error message appears: "Minimum stake is €1.00"
- No bet should be placed

**Alternative (if €1.00 is accepted):**
- Stake €1.00 is accepted
- Bet can be placed successfully

### 3. **TC-003: Stake Validation - Boundary: Maximum Stake (€100.00)**
**Priority:** 🔴 **CRITICAL**

**Risk Rationale:**
- Maximum stake is a hard business rule (€100.00)
- Protects against accidental over-betting or fraud
- Boundary condition: €100.00 should pass, €100.01 should fail
- Both UI and API validation required

**Preconditions:**
- User balance ≥ €100.00
- A match is selected

**Steps:**
1. Select a match outcome
2. Enter stake: €100.01
3. Attempt to click "Place Bet"
4. Observe UI feedback

**Expected Result:**
- "Place Bet" button is disabled OR
- Error message appears: "Maximum stake is €100.00"
- API call is NOT made

**Follow-up (Positive):**
- Clear stake field
- Enter stake: €100.00
- Click "Place Bet"
- Bet should be placed successfully

### 4. **TC-004: Insufficient Balance Validation**
**Priority:** 🔴 **CRITICAL**

**Risk Rationale:**
- Critical business rule: user cannot bet more than available balance
- Prevents negative balance / over-betting
- Must block at UI level to prevent API calls

**Preconditions:**
- User balance is known (default €125.50)
- A match is selected

**Steps:**
1. Check current balance in header
2. Enter stake equal to: current_balance + €1.00 (e.g., €126.50)
3. Attempt to click "Place Bet"
4. Observe UI feedback

**Expected Result:**
- "Place Bet" button is disabled OR
- Error message appears: "Insufficient balance"
- API call is NOT made
- No bet is placed

### 5. **TC-005: Error Handling - API Failure & Retry Flow**
**Priority:** 🟡 **HIGH**

**Risk Rationale:**
- Error handling is critical for user trust
- User must be able to recover gracefully (Rebet or Close)
- Tests that error modal displays correct information and actions work

**Preconditions:**
- User can trigger an API error (e.g., concurrent bet in progress, server error)
- A match is selected and valid stake is entered

**Steps:**
1. Enter valid stake (e.g., €10.00)
2. Click "Place Bet"
3. Wait for error modal to appear (may require special test data or timing)

**Expected Result:**
- Loading state is shown ("Placing...")
- Error modal appears with:
  - Title: "Something went wrong"
  - Body explains bet could not be processed
  - "Rebet" button (primary action)
  - "Close" button (secondary action)
  - Top-right X button
- Balance is NOT deducted (no partial state)

**Follow-up: Test Rebet Action**
1. Click "Rebet" button
2. Modal closes
3. Bet slip shows previous stake and selection still active
4. Retry placement

**Follow-up: Test Close Action**
1. Click "Close" button
2. Modal closes
3. Bet slip is cleared (no active selection, stake empty)

### 6. **TC-006: Odds Selection Replacement (Single Bet Only)**
**Priority:** 🟡 **HIGH**

**Risk Rationale:**
- UI must support switching selections before bet placement
- Bet slip should only show ONE active selection at a time
- Confirms single-bet-only constraint is enforced

**Preconditions:**
- User is on the application
- A match is displayed

**Steps:**
1. Click on match "1" (Home Win) odds button
2. Observe bet slip shows HOME selection with that odds value
3. On the SAME match, click "X" (Draw) odds button
4. Observe bet slip updates

**Expected Result:**
- After step 2: Bet slip displays:
  - Match details
  - Selection: HOME with home odds
  - Odds value matches button clicked
- After step 4: Bet slip displays:
  - Same match
  - Selection: DRAW with draw odds (HOME selection is REPLACED)
  - Previous selection is NO LONGER shown
- Only ONE selection is active in bet slip at all times

## Test Execution Order

Run in this priority order:

1. **TC-001** → Validates core happy path works
2. **TC-002** → Validates minimum stake rule
3. **TC-003** → Validates maximum stake rule
4. **TC-004** → Validates insufficient balance check
5. **TC-005** → Validates error recovery (if errors are reproducible)
6. **TC-006** → Validates UI state management

## Out of Scope (Intentionally Not Tested Here)

- Multi-bet / Accumulator functionality
- Live betting
- Mobile-specific UX
- Other sports
- Odds filtering/date filtering (separate feature)
- Payment/deposit flows
- Account settings

## Success Criteria

A feature passes if:
- ✅ Happy path (TC-001) works end-to-end
- ✅ All validation boundaries (TC-002, TC-003, TC-004) are enforced
- ✅ Error states are recoverable (TC-005)
- ✅ UI state is correct after interactions (TC-006)

## Notes for Tester

- **API Testing:** Use `/api/docs` to understand request/response formats
- **Headers:** All API calls require `x-user-id` header
- **Balance Reset:** Use `POST /api/reset-balance` if you need to restore balance during testing
- **Stake Format:** Accept up to 2 decimal places (€10.00, not €10.000)
- **Odds Format:** Decimal odds (e.g., 2.45), not fractional
