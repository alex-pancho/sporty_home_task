
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


===

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

