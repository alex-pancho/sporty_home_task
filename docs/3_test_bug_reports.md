
# BUG-001: Past Matches Displayed in Match List and Available for Betting

**ID:** BUG-003

**Priority:** 🛑 **BLOCKER / CRITICAL**

**Severity:** Critical (Financial & Business Logic Vulnerability)

**Status:** Open

**Component:** Match List / Pre-match Validation

#### **Description**

The application displays past (concluded) football matches in the "Upcoming Matches" list. Furthermore, the system allows users to select odds, enter stakes, and successfully place pre-match bets on these past events where the outcome is already determined.

This violates requirement **2.1 (Match List)**: *"Display upcoming football matches."*

#### **Steps to Reproduce**

1. Navigate to the betting application.
2. Observe the match list on the main dashboard.
3. Locate a match with a kickoff timestamp/date that is in the past (e.g., a match from yesterday or earlier today).
4. Click on any odds button (1/X/2) for this past match.
5. Enter a valid stake (e.g., €10.00) in the bet slip.
6. Click "Place Bet".
7. Observe the behavior.

#### **Expected Result**

* Past matches should **not** be displayed in the match list.
* If a match has already started or ended, its odds must be disabled/locked, and placing a bet should be strictly blocked both on the UI and API levels.

#### **Actual Result**

* Past matches are visible in the list alongside genuine upcoming matches.
* Odds remain active, and the user can successfully place a bet and receive a success receipt for an event that has already concluded.


#### **Supporting Evidence**

* **Requirement Violated:** 2.1 Match List (Should only display *upcoming* football matches).
* **Example:** Match "Manchester Utd vs Chelsea" dated `Fri, Feb 27` allows active selection and successful bet submission.

#### **Risk/Impact**

* **Extreme Financial Loss:** Users can exploit this bug to place guaranteed winning bets on matches that have already finished.
* **Compliance & Licensing:** Allowing bets on past events violates global gambling regulations and legal frameworks.
* **Data Corruption:** Corrupts the integrity of the betting ledger and user history metrics.

*Note: This must be fixed on the backend/API side immediately by filtering out matches where `kickoff_time < CURRENT_TIMESTAMP` and rejecting any incoming bets for such match IDs on the server side.*

======


# BUG-002: User Balance Not Updating Real-Time After Bet Placement

**ID:** BUG-002

**Priority:** 🔴 **CRITICAL**

**Severity:** High (UI/UX & Financial Feedback)

**Status:** Open

**Component:** Header / Balance Display

#### **Description**

The user's balance in the header does not update automatically after a successful bet placement. The balance remains unchanged until the user manually refreshes the browser page.

#### **Steps to Reproduce**

1. Check the current balance in the application header.
2. Select a match outcome and enter a valid stake (e.g., €10.00).
3. Click "Place Bet" and wait for the "Bet Placed Successfully" receipt modal.
4. Close the receipt modal.
5. Observe the balance displayed in the application header.

#### **Expected Result**

The balance in the header should update immediately after the bet is successfully placed (Balance = Previous Balance - Stake) without requiring a page refresh.

#### **Actual Result**

The balance in the header remains at the previous value after the bet is placed. The correct (updated) balance only appears after a full page reload.
![screen01](<img/2026-06-25 15_59_52-Sports Betting QA.png>)
![screen02](<img/2026-06-25 16_01_41-Sports Betting QA.png>)

#### **Environment**

**Tester:** Oleksandr Panchenko

**Date:** 2026-06-25  

**Test Environment:** https://qae-assignment-tau.verisk.app/?user-id=candidate-c9ywt7uhfX 

**Browser:** Chrome 149.0.7827.197

#### **Risk/Impact**

* **User Experience:** Causes confusion and lack of transparency regarding the user's financial status.
* **Trust:** Users may think the transaction failed or that the system is broken if their balance does not reflect their actions.
* **Data Consistency:** The UI state is out of sync with the actual server-side account state, which is a significant functional flaw.

#### **Technical details**

The response from the [API](https://qae-assignment-tau.vercel.app/api/place-bet) contains the correct data:
```
balance: 104.5
```
in response
![screen02](<img/2026-06-25 16_01_41-Sports Betting QA.png>)

======


# BUG-003: Incorrect Team Order Displayed in Success Receipt

**ID:** BUG-001

**Priority:** 🔴 **CRITICAL**

**Severity:** High (Data Integrity & User Trust)

**Component:** Bet Placement / Receipt Modal

#### **Description**

After successfully placing a bet on the "Home" team, the match title in the "Bet Placed Successfully" receipt modal displays the teams in the reverse order (Away vs. Home) instead of the correct match format (Home vs. Away).

**Please note:** that this error is not related to the type of bet or the teams selected and occurs in all cases.

#### **Steps to Reproduce**

1. Navigate to the betting application.
2. Locate the match: **Manchester Utd vs. Chelsea**.
3. Click the "1" (Home Win / Manchester Utd) odds button.
4. Enter a valid stake (e.g., €10.00).
5. Click "Place Bet".
6. Observe the "Match" field in the success receipt modal.

#### **Expected Result**

The "Match" field in the receipt should display the teams in the original order as they appear in the fixture list: **Manchester Utd vs. Chelsea**.

#### **Actual Result**

The "Match" field in the receipt displays an inverted order: **Chelsea vs. Manchester Utd**.

#### **Environment**

**Tester:** Oleksandr Panchenko

**Date:** 2026-06-25  

**Test Environment:** https://qae-assignment-tau.verisk.app/?user-id=candidate-c9ywt7uhfX 

**Browser:** Chrome 149.0.7827.197 

#### **Supporting Evidence**

* **Selected Match:** Manchester Utd vs. Chelsea (Home selection: Manchester Utd).
* **Receipt Data:**
* **Bet ID:** #B-26936
* **Actual Display:** Chelsea vs. Manchester Utd

#### **Risk/Impact**

* **User Confusion:** Users may believe they have placed a bet on the incorrect outcome or the wrong match, leading to unnecessary support tickets.
* **Compliance/Trust:** Inaccurate transaction records are unacceptable in betting applications and severely undermine system reliability.
* **Data Integrity:** Indicates a potential logic flaw in how match data is serialized or mapped in the response object.

#### **Technical details**

The response from the [API](https://qae-assignment-tau.vercel.app/api/place-bet) contains the correct data:
```
matchId: "premier-league-manutd-chelsea",
message: "Bet placed successfully",
selection: "HOME",
```
in request and response

======


# BUG-004: Lack of Validation for Invalid Odds Filter Range

**ID:** BUG-004

**Priority:** 🔴 **HIGH**

**Component:** Filters / Odds

**Description:**
The application fails to validate the odds range filter. When the "Min" value is greater than the "Max" value, the filter is applied without any error feedback, leading to an empty or unpredictable state.

**Steps to Reproduce:**

1. Navigate to the Match List.
2. Open the Odds filter.
3. Enter **1.69** in the "Min" field.
4. Enter **1.59** in the "Max" field.
5. Apply the filter.

**Expected Result:**
The system should display a clear error message (e.g., "Min odds cannot be greater than Max odds") and prevent the filter from being applied.

**Actual Result:**
The filter is applied, and the system fails to display an error message.

# BUG-005: Incorrect Filtering Logic for Boundary Values (Off-by-one error)

**ID:** BUG-005

**Priority:** 🔴 **HIGH**

**Component:** Filters / Odds

**Description:**
The odds filter incorrectly excludes matches that exactly match the "Min" value provided by the user. It seems the filter is using an exclusive comparison (`>`) instead of an inclusive one (`>=`), which contradicts the requirement that the range must be inclusive.

**Steps to Reproduce:**

1. Identify a match with odds of **1.70**.
2. Open the Odds filter.
3. Enter **1.70** in the "Min" field.
4. Apply the filter.

**Expected Result:**
Matches with odds of **1.70** should be visible in the list (Inclusive range).

**Actual Result:**
Matches with odds of **1.70** are hidden/filtered out. (They only appear if the "Min" is set to 1.69 or lower).

======

# DOC-001: Documentation Inconsistency - Minimum Stake Requirement

**ID:** DOC-001

**Priority:** 🟡 **LOW** 

**Type:** Documentation / Requirement Error

#### **Description**

There is a discrepancy between the stated requirement for the minimum stake in the test plan documentation and the actual implementation of the application.

* **Requirement 4.4 / Stake Validation:** Specifies "Minimum €1.01".
* **Application Behavior:** Currently accepts/enforces a minimum of "€1.00".

#### **Steps to Reproduce**

1. Review the test plan documentation section **4.4 UI Error Messaging** and **Stake Validation**.
2. Compare the text "Minimum €1.01" against the actual system behavior (which uses "€1.00" as the threshold).

#### **Expected Result**

The documentation and the application logic must be synchronized. If the business rule is €1.00, the documentation must be updated to reflect this value to avoid confusion during testing.

#### **Actual Result**

The documentation explicitly states "€1.01", creating ambiguity for the testing process and potential future compliance issues.

======

# BUG-006: Incorrect Payout Calculation

**ID:** BUG-006

**Priority:** 🔴 **CRITICAL**

**Severity:** High (Financial Impact)

**Component:** Bet Slip / Payout Calculation

### **Description**

The potential payout displayed in the bet slip is calculated incorrectly. For a stake of €1.00 with odds of 2.45, the system shows €2.00, but the correct payout should be €2.45.

**Formula:**
```
Payout = Stake × Odds
€1.00 × 2.45 = €2.45 ✅ (correct)
€1.00 × 2.45 = €2.00 ❌ (actual display)
```

### **Steps to Reproduce**

1. Open application
2. Select any match with odds of 2.45 (or similar)
3. Enter stake: €1.00
4. Observe "Potential Payout" field

### **Expected Result**

Potential Payout should display: **€2.45**

### **Actual Result**

Potential Payout displays: **€2.00**

### **Impact**

- 🔴 **CRITICAL Financial Impact:** Users see incorrect payout before placing bet
- User confusion: "Why is my payout only €2.00 instead of €2.45?"
- Trust issue: Makes system look unreliable
- Could affect betting decisions

### **Root Cause (Hypothesis)**

- Rounding error in calculation
- Math.round() instead of proper decimal handling
- Truncation instead of multiplication
- Display formatter issue

### **Technical Details**

```
Expected: stake * odds = 1.00 * 2.45 = 2.45
Actual: 1.00 * 2.00 = 2.00

Difference: 0.45 (€0.45 discrepancy!)
```

### **Recommendation**

- Use proper decimal arithmetic (not floating point)
- Verify calculation logic: `payout = stake * odds`
- Check rounding rules (should round to 2 decimals, not truncate)
- Add unit tests for payout calculation


======

# BUG-007: `POST /api/reset-balance` returns reset balance but does not update the actual account balance

**Severity:** Critical

**Priority:** Critical

**Component:** Backend API

### Description

According to the API specification, `POST /api/reset-balance` is a test endpoint that resets the user's balance to the initial value (**125.50**).

The endpoint response indicates that the balance has been successfully reset and returns `125.50`. However, a subsequent call to `GET /api/balance` still returns the previous balance (`120.00`), meaning the account state has not actually been updated.

As a result, the API response does not reflect the real system state.

### Preconditions

* Initial balance is **125.50**.
* Place a successful bet with a stake of **5.50**.
* Current balance becomes **120.00**.

### Steps to Reproduce

1. Call `GET /api/balance` and verify the balance is **120.00**.
2. Call `POST /api/reset-balance`.
3. Verify that the response body contains **125.50**.
4. Call `GET /api/balance`.

### Expected Result

The refresh operation should reset the user's balance to **125.50**.

Example:

```text
POST /api/reset-balance → balance = 125.50
GET  /api/balance       → balance = 125.50
```

### Actual Result

The refresh endpoint reports a successful reset but the account balance remains unchanged.

```text
POST /api/reset-balance → balance = 125.50
GET  /api/balance       → balance = 120.00
```

### Business Impact

The endpoint reports a successful balance reset without actually updating the persisted account state. This creates a discrepancy between the API response and the actual system state.

Although this endpoint is intended for testing, it demonstrates that the balance update operation is not persisted. A similar defect in production balance operations (e.g., deposits or refunds) would have a critical financial impact by confirming a successful operation without updating the user's actual available funds.

**The endpoint violates the principle that the returned resource representation must reflect the persisted system state.**

### Evidence

```text
POST /api/reset-balance
Response:
{
    "balance": 125.50
}

GET /api/balance
Response:
{
    "balance": 120.00
}
```
**Specification Violation**

The API specification states:

"Balance reset successfully"

and returns a balance of 125.50.

However, the persisted balance remains 120.00, meaning the implementation does not satisfy the contract defined by the API.
